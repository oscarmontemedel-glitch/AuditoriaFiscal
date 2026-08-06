"""
=========================================================
SAF v13.0
Modelo Inteligente Libro Mayor
=========================================================
"""

import pandas as pd


class ModeloLibro:

    def __init__(self, dataframe):

        if dataframe is None:
            dataframe = pd.DataFrame()

        self.df = dataframe.copy()

    # ============================================
    # PROPIEDADES
    # ============================================

    @property
    def empty(self):
        return self.df.empty

    @property
    def total(self):
        return len(self.df)

    @property
    def columnas(self):
        return list(self.df.columns)

    # ============================================
    # DATAFRAME
    # ============================================

    def dataframe(self):
        return self.df.copy()

    # ============================================
    # BUSCAR
    # ============================================

    def buscar(self, texto):

        texto = str(texto).upper()

        mascara = pd.Series(False, index=self.df.index)

        for columna in self.df.columns:

            mascara |= (

                self.df[columna]

                .fillna("")

                .astype(str)

                .str.upper()

                .str.contains(

                    texto,

                    na=False

                )

            )

        return self.df[mascara]

    # ============================================
    # COLUMNAS NUMERICAS
    # ============================================

    def columnas_numericas(self):

        columnas = []

        for c in self.df.columns:

            serie = pd.to_numeric(

                self.df[c],

                errors="coerce"

            )

            if serie.notna().sum() > 0:

                columnas.append(c)

        return columnas

    # ============================================
    # TOTAL
    # ============================================

    def total_columna(self, columna):

        if columna not in self.df.columns:

            return 0

        return (

            pd.to_numeric(

                self.df[columna],

                errors="coerce"

            )

            .fillna(0)

            .sum()

        )

    # ============================================
    # EXISTE
    # ============================================

    def contiene(self, texto):

        return len(

            self.buscar(texto)

        ) > 0