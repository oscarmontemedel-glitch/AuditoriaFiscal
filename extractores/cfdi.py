"""
=========================================================
SAF v10.0
Extractor CFDI
=========================================================

Responsabilidad

Extraer todas las hojas del archivo de CFDI
y convertirlas en una colección de DataFrames
limpios.

NO normaliza nombres.

NO cambia tipos.

NO hace auditoría.

=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorCFDI(ExtractorBase):

    def __init__(self, hojas):

        """
        hojas:
            dict[str, DataFrame]
        """

        self.hojas = hojas

    def obtener(self):

        if not self.hojas:

            print("⚠ No existen hojas CFDI.")

            return {}

        resultado = {}

        print()
        print("=" * 60)
        print("EXTRACTOR CFDI")
        print("=" * 60)

        for nombre, df in self.hojas.items():

            if df is None:

                continue

            df = self.limpiar_dataframe(df)

            if df.empty:

                continue

            resultado[nombre] = df

            print(

                f"{nombre:<25}"

                f"{len(df):>8} registros"

            )

        print()
        print(

            f"Hojas procesadas : {len(resultado)}"

        )

        return resultado