"""
=========================================================
SAF v10.0
Extractor DM Ingresos
=========================================================

Responsabilidad

Extraer todas las hojas pertenecientes al
papel de trabajo de DM Ingresos.

- Une todas las hojas.
- Conserva la hoja origen.
- No modifica columnas.
- No normaliza nombres.
- No cambia tipos.

=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorDMIngresos(ExtractorBase):

    def __init__(self, hojas):

        """
        hojas:
            dict[str, DataFrame]
        """

        self.hojas = hojas

    def obtener(self):

        if not self.hojas:

            print("⚠ No existen hojas de DM Ingresos.")

            return pd.DataFrame()

        tablas = []

        print()
        print("=" * 60)
        print("EXTRACTOR DM INGRESOS")
        print("=" * 60)

        for nombre_hoja, df in self.hojas.items():

            df = self.limpiar_dataframe(df)

            if df.empty:

                continue

            copia = df.copy()

            copia["__HOJA__"] = nombre_hoja

            tablas.append(copia)

            print(

                f"{nombre_hoja:<25}"

                f"{len(copia):>8} registros"

            )

        if not tablas:

            return pd.DataFrame()

        ingresos = pd.concat(

            tablas,

            ignore_index=True,

            sort=False

        )

        self.imprimir_resumen(

            "Extractor DM Ingresos",

            ingresos

        )

        return ingresos