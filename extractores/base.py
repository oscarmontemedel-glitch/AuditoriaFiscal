"""
=========================================================
SAF v10.0
Clase Base para Extractores
=========================================================

Todos los extractores del SAF deberán heredar de esta clase.

Responsabilidades:

- Abrir hojas del repositorio.
- Limpiar filas vacías.
- Normalizar nombres de columnas.
- Registrar estadísticas.
- Devolver DataFrames limpios.
=========================================================
"""

import pandas as pd


class ExtractorBase:

    def __init__(self, repo):

        self.repo = repo

    # =====================================================
    # Utilidades
    # =====================================================

    def limpiar_dataframe(self, df):

        if df is None:

            return pd.DataFrame()

        df = df.copy()

        df = df.dropna(how="all")

        df.columns = [

            str(c)
            .strip()
            .upper()

            for c in df.columns

        ]

        return df

    # =====================================================
    # Estadísticas
    # =====================================================

    def imprimir_resumen(self, nombre, df):

        print()

        print("=" * 60)
        print(nombre.upper())
        print("=" * 60)

        print(f"Filas     : {len(df)}")
        print(f"Columnas  : {len(df.columns)}")

    # =====================================================
    # Método obligatorio
    # =====================================================

    def obtener(self):

        raise NotImplementedError(
            "El extractor debe implementar obtener()."
        )