"""Compila el lector de respaldos .bak que usa extraer.py.

Uso: python lector/compilar.py [lector/bin/]

Clona BAK-SHELL en una versión fija, le aplica bakshell.patch y compila sus carpetas Mdf/ y Mtf/
con Program.cs. Necesita git y el SDK de .NET 8 (`dotnet`, o la ruta en la variable DOTNET).
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BAKSHELL = "https://github.com/Dankular/BAK-SHELL"
BAKSHELL_COMMIT = "03c4739a1daf836b36f3750dab3db2b3dee52e2c"
CARPETA = Path(__file__).resolve().parent


def main(salida):
    dotnet = os.environ.get("DOTNET") or shutil.which("dotnet") or sys.exit("No se encontró dotnet (SDK .NET 8)")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        fuente = tmp / "bakshell"
        subprocess.run(["git", "clone", "-q", BAKSHELL, str(fuente)], check=True)
        subprocess.run(["git", "-C", str(fuente), "checkout", "-q", BAKSHELL_COMMIT], check=True)
        subprocess.run(["git", "-C", str(fuente), "apply", str(CARPETA / "bakshell.patch")], check=True)
        proyecto = tmp / "lector"
        proyecto.mkdir()
        for carpeta in ("Mdf", "Mtf"):
            shutil.copytree(fuente / carpeta, proyecto / carpeta)
        for archivo in ("Program.cs", "lector.csproj"):
            shutil.copy(CARPETA / archivo, proyecto)
        subprocess.run([dotnet, "build", str(proyecto / "lector.csproj"), "-c", "Release", "-o", str(salida.resolve()),
                        "-v", "quiet", "-nologo", "-clp:ErrorsOnly"], check=True)
    print(f"Lector en {salida / 'lector.dll'}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]) if len(sys.argv) == 2 else CARPETA / "bin")
