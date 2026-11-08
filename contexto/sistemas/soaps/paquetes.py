"""Paquetes de SOAPS publicados en el portal del SNIS que usa este proyecto.

La fecha es la del instalador dentro del .rar. La versión 7.0.1 declara las gestiones de sus reglas actuales.
La versión 1.0.4 ya no está en el portal; su enlace es una copia de la página anterior en Internet Archive.
"""

URL = "https://snis.minsalud.gob.bo/publicaciones?task=download.send&id={id}&catid={catid}&m=0"

PAQUETES = [
    {"version": "1.0.4", "archivo": "SETUP_SOAPS__104_01022013.rar", "fecha": "2013-02-06",
     "url": "https://web.archive.org/web/20150410142113/http://snis.minsalud.gob.bo/documentacion/software-snis/ACTUALIZA_SOAPS_104_01022013.rar",
     "sha256": "1514d8dde129864a4751f95006947b6b96ffa2a9c850379dc107b94f8b2cc929"},
    {"version": "2.0.0", "archivo": "SETUP_SOAPS_200_2582014 1.rar", "id": 506, "catid": 37, "fecha": "2014-08-27",
     "sha256": "d40c7376a9060a98e16eb009f8e2cae3f34940d2767bb3aca39d21d7a8f855cf"},
    {"version": "3.0.1", "archivo": "ACTUALIZA_SOAPS_3.0.1_310120160.rar", "id": 504, "catid": 36, "fecha": "2016-01-31",
     "sha256": "9257025f946679250c74e75df92a3f6e36bc8d6be347ced9e421f3f2199f190d"},
    {"version": "3.0.2", "archivo": "ACTUALIZA_SOAPS_3.0.2_26102016.rar", "id": 505, "catid": 36, "fecha": "2016-10-26",
     "sha256": "692cabd08c0b7e692364f34010048ee8b6bcea426e0fbe391a824f070d575d50"},
    {"version": "4.0.0", "archivo": "SETUP_SOAPS_400.rar", "id": 701, "catid": 15, "fecha": "2018-01-09",
     "sha256": "cd0ed48e1798351d1c67dfeb5a9c6609fe728c850e3249820ecff0ce76deec57"},
    {"version": "4.0.1", "archivo": "Instalador SOAPS 401.rar", "id": 779, "catid": 37, "fecha": "2018-07-03",
     "sha256": "77eb275cb5f3d51f63f54c9cb116d3e6ac36197be6042831de537c4bf12b96d1"},
    {"version": "5.0.1", "archivo": "SETUP_SOAPS_501.rar", "id": 931, "catid": 37, "fecha": "2020-05-11",
     "sha256": "3c5df4e5be1dc26e8fdbb33d81ccbff5f24fca2c79f157ab6acb8191fb66089c"},
    {"version": "6.0.0", "archivo": "SOAPS_600.rar", "id": 970, "catid": 37, "fecha": "2021-06-02",
     "sha256": "b242ed215d1519b6c90aade0ba2f144ae77208d0bb339afa276219180263ca91"},
    {"version": "6.0.1", "archivo": "Instalador SOAPS 601.rar", "id": 990, "catid": 37, "fecha": "2022-06-02",
     "sha256": "0d414c787095ebf958b4b4c76df84807927c436eefa9513b59f89578ca5c4abc"},
    {"version": "7.0.1", "archivo": "SERVIDOR_SOAPS_7.rar", "id": 1217, "catid": 2, "fecha": "2026-08-31",
     "sha256": "1016fd10c25d4f4922c525496500a1a61a6d413cf525c1a078de9241953e54a6", "gestiones": [2025, 2026]},
]
