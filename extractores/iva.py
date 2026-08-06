"""
=========================================================
SAF v10.0
Extractor IVA
=========================================================

Responsabilidad

Extraer las diferentes tablas contenidas en la
Integración de IVA.

NO normaliza columnas.
NO cambia tipos.
NO interpreta información fiscal.

Únicamente entrega las tablas limpias.

=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorIVA(ExtractorBase):

    def __init__(self, hojas):

        """
        hojas:
            dict[str, DataFrame]
        """

        self.hojas = hojas

    def obtener(self):

        if not self.hojas:

            print("⚠ No existen hojas de IVA.")

            return {}

        resultado = {}

        print()
        print("=" * 60)
        print("EXTRACTOR IVA")
        print("=" * 60)

        for nombre, df in self.hojas.items():

            df = self.limpiar_dataframe(df)

            if df.empty:

                continue

            resultado[nombre.upper()] = df

            print(

                f"{nombre:<20}"

                f"{len(df):>8} registros"

            )

        print()

        print(

            f"Tablas extraídas : {len(resultado)}"

        )

        return resultado