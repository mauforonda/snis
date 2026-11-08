"""Extrae de los paquetes de SOAPS las tablas que usa construir.py.

Uso: python extraer.py lector/bin/lector.dll intermedios/ ../fuentes/*.rar

Para cada paquete de paquetes.py: .rar → instalador Setup Factory (.exe) → respaldos .bak → JSONL y SQL
en intermedios/<versión>/. Los instaladores recientes guardan los respaldos dentro de bases_vacias.zip.
Los respaldos se leen con el lector que compila lector/compilar.py.
Necesita unrar y .NET 8 (`dotnet`, o la ruta en la variable DOTNET).
"""

import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import pefile
from refinery.units.formats.archive.xtsf import xtsf

from paquetes import PAQUETES

# Tablas y procedimientos que se buscan en cada respaldo. Las opcionales no existen en todas las versiones.
TABLAS = {
    "BDEstadistica": [
        "SE_REPORTE", "SE_REPORTE_GRU", "SE_REPORTE_FIL", "SE_REPORTE_FILGRU", "SE_REPORTE_FILCOL",
        "SE_COLUMNAS", "SE_CUADERNO", "SE_INTERVALOS", "SE_CIE10", "ad_RelacionaTablas", "ad_listagenericaE",
    ],
    "BDSnis": ["t_Formsubvar"],
}
OPCIONALES = {
    "BDEstadistica": ["SE_REPORTE_GRU_n", "SE_REPORTE_FIL_n", "SE_REPORTE_FILGRU_n", "SE_REPORTE_FILCOL_N",
                      "cancer_en_sus_distintas_formas", "casos_otros_accidentes", "hechos_transito_accidentes"],
    "BDSnis": ["t_sexo"],
}


class SetupFactory(xtsf):
    """Extractor de Setup Factory que salta el ejecutable auxiliar situado antes de los archivos del programa."""

    __module__ = xtsf.__module__

    def _saltar_ejecutable(self, reader):
        if bytes(reader.peek(2)) == b"MZ":
            pe = pefile.PE(data=bytes(reader.getbuffer()[reader.tell():]), fast_load=True)
            firma = pe.OPTIONAL_HEADER.DATA_DIRECTORY[4]
            reader.seekrel(max(pe.get_overlay_data_start_offset() or 0, firma.VirtualAddress + firma.Size))

    def _parse_script_v7(self, script_bytes, compression, reader):
        self._saltar_ejecutable(reader)
        yield from super()._parse_script_v7(script_bytes, compression, reader)

    def _parse_script_v8(self, script_bytes, compression, version, reader):
        self._saltar_ejecutable(reader)
        yield from super()._parse_script_v8(script_bytes, compression, version, reader)


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def respaldos(instalador, destino):
    """Escribe BDEstadistica.bak y BDSnis.bak del instalador en destino."""
    encontrados = {}
    for entrada in SetupFactory().unpack(bytearray(instalador.read_bytes())):
        nombre = Path(entrada.path.replace("\\", "/")).name
        if nombre.lower() == "bases_vacias.zip":
            with zipfile.ZipFile(io.BytesIO(entrada.get_data())) as z:
                for interno in z.namelist():
                    if (base := Path(interno).stem.lower()) in ("bdestadistica", "bdsnis"):
                        encontrados[base] = z.read(interno)
        elif nombre.lower() in ("bdestadistica.bak", "bdsnis.bak"):
            encontrados[Path(nombre).stem.lower()] = entrada.get_data()
    for base, nombre in (("bdestadistica", "BDEstadistica"), ("bdsnis", "BDSnis")):
        if base not in encontrados:
            sys.exit(f"{instalador.name} no contiene {nombre}.bak")
        (destino / f"{nombre}.bak").write_bytes(encontrados[base])


def extraer(rar, paquete, lector, dotnet, salida):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "rar").mkdir()
        subprocess.run(["unrar", "x", "-o+", "-inul", str(rar.resolve()), f"{tmp / 'rar'}/"], check=True)
        instalador = next((tmp / "rar").rglob("*.exe"))
        print(f"{paquete['version']}: leyendo {instalador.name}", flush=True)
        respaldos(instalador, tmp)

        for base, tablas in TABLAS.items():
            destino = salida / paquete["version"] / base
            if destino.exists():
                shutil.rmtree(destino)
            buscadas = tablas + OPCIONALES[base]
            patron = "^(" + "|".join(buscadas) + ")$"
            subprocess.run([dotnet, str(lector.resolve()), str(tmp / f"{base}.bak"), str(destino), patron, patron],
                           check=True, stdout=subprocess.DEVNULL)
            if faltan := [t for t in tablas if not (destino / f"{t}.jsonl").exists()]:
                sys.exit(f"{paquete['version']} {base}: no se extrajo {', '.join(faltan)}")


def main(lector, salida, rars):
    if not lector.is_file():
        sys.exit(f"No existe {lector}; compílelo con python lector/compilar.py")
    dotnet = os.environ.get("DOTNET") or shutil.which("dotnet") or sys.exit("No se encontró dotnet (.NET 8)")
    por_suma = {p["sha256"]: p for p in PAQUETES}
    for rar in rars:
        if (paquete := por_suma.get(sha256(rar))) is None:
            sys.exit(f"{rar}: no es un paquete de paquetes.py (SHA-256 distinta)")
        extraer(rar, paquete, lector, dotnet, salida)
    print(f"Tablas intermedias en {salida}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    main(Path(sys.argv[1]), Path(sys.argv[2]), [Path(a) for a in sys.argv[3:]])
