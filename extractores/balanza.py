"""
=========================================================
SAF v10.0
Extractor Balanza de Comprobación
=========================================================

Responsabilidad

Extraer la información de la Balanza de Comprobación.

- Une todas las hojas.
- Elimina filas vacías.
- Conserva el nombre de la hoja origen.

NO normaliza nombres.
NO convierte tipos.
NO realiza auditoría.

=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorBalanza(ExtractorBase):

    def __init__(self, hojas):

        """
        hojas:
            dict[str, DataFrame]
        """

        self.hojas = hojas

    def obtener(self):

        if not self.hojas:

            print("⚠ No existen hojas de Balanza.")

            return pd.DataFrame()

        tablas = []

        print()
        print("=" * 60)
        print("EXTRACTOR BALANZA")
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

        balanza = pd.concat(

            tablas,

            ignore_index=True

        )

        self.imprimir_resumen(

            "Extractor Balanza",

            balanza

        )

        return balanza