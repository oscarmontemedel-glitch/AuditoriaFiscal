"""
=========================================================
SAF v10.0
Extractor Libro Mayor
=========================================================

Responsabilidad

- Obtener el Libro Mayor desde el repositorio.
- Unificar todas las hojas.
- Limpiar filas vacías.
- No normaliza columnas.
- No realiza auditoría.

=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorLibroMayor(ExtractorBase):

    def __init__(self, repo):

        super().__init__(repo)

    def obtener(self):

        hojas = self.repo.obtener(

            "LIBRO MAYOR"

        )

        if not hojas:

            print()

            print("⚠ Libro Mayor no encontrado.")

            return pd.DataFrame()

        tablas = []

        for hoja, df in hojas.items():

            df = self.limpiar_dataframe(df)

            if df.empty:

                continue

            df = df.copy()

            df["__HOJA__"] = hoja

            tablas.append(df)

        if not tablas:

            return pd.DataFrame()

        libro = pd.concat(

            tablas,

            ignore_index=True

        )

        self.imprimir_resumen(

            "Extractor Libro Mayor",

            libro

        )

        return libro