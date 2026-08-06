"""
Logger de la Suite de Auditoría Fiscal
"""

from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self):

        carpeta = Path("Reportes")

        carpeta.mkdir(exist_ok=True)

        self.archivo = carpeta / "auditoria.log"

        with open(
            self.archivo,
            "w",
            encoding="utf-8"
        ) as f:

            f.write("")
    
    def escribir(self, mensaje):

        hora = datetime.now().strftime("%H:%M:%S")

        linea = f"[{hora}] {mensaje}"

        print(linea)

        with open(
            self.archivo,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(linea + "\n")