"""
=========================================================
SAF v14.0
Modelo Inteligente Auxiliar
=========================================================
"""

import pandas as pd


class ModeloAuxiliar:

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
    # CUENTAS
    # ============================================

    def cuentas(self):

        if "CUENTA" not in self.df.columns:
            return []

        return (

            self.df["CUENTA"]

            .dropna()

            .astype(str)

            .unique()

            .tolist()

        )

    # ============================================
    # BUSCAR CUENTA
    # ============================================

    def por_cuenta(self, cuenta):

        if "CUENTA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[

            self.df["CUENTA"]

            .astype(str)

            ==

            str(cuenta)

        ]

    # ============================================
    # BUSCAR PÓLIZA
    # ============================================

    def por_poliza(self, poliza):

        if "POLIZA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[

            self.df["POLIZA"]

            .astype(str)

            ==

            str(poliza)

        ]

    # ============================================
    # BUSCAR TEXTO
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
    # CONTIENE
    # ============================================

    def contiene(self, texto):

        return not self.buscar(texto).empty

    # ============================================
    # COLUMNAS NUMÉRICAS
    # ============================================

    def columnas_numericas(self):

        resultado = []

        for columna in self.df.columns:

            serie = pd.to_numeric(

                self.df[columna],

                errors="coerce"

            )

            if serie.notna().sum() > 0:

                resultado.append(columna)

        return resultado

    # ============================================
    # TOTAL COLUMNA
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
    # EXISTE COLUMNA
    # ============================================

    def existe_columna(self, columna):

        return columna in self.df.columns