"""
=========================================================
SAF v13.0
Modelo Inteligente DM Ingresos
=========================================================
"""

import pandas as pd


class ModeloIngresos:

    def __init__(self, dataframe):

        if dataframe is None:
            dataframe = pd.DataFrame()

        self.df = dataframe.copy()

    # =====================================================
    # PROPIEDADES
    # =====================================================

    @property
    def empty(self):
        return self.df.empty

    @property
    def total(self):
        return len(self.df)

    @property
    def columnas(self):
        return list(self.df.columns)

    # =====================================================
    # DATAFRAME
    # =====================================================

    def dataframe(self):
        return self.df.copy()

    # =====================================================
    # TOTAL INGRESOS
    # =====================================================

    def total_ingresos(self):

        if "INGRESO" not in self.df.columns:
            return 0

        return (
            pd.to_numeric(
                self.df["INGRESO"],
                errors="coerce"
            )
            .fillna(0)
            .sum()
        )

    # =====================================================
    # FILTRAR POR BANCO
    # =====================================================

    def por_banco(self, banco):

        if "BANCO" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[
            self.df["BANCO"]
            .fillna("")
            .astype(str)
            .str.upper()
            ==
            str(banco).upper()
        ]

    # =====================================================
    # FILTRAR POR PÓLIZA
    # =====================================================

    def por_poliza(self, poliza):

        if "POLIZA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[
            self.df["POLIZA"]
            .fillna("")
            .astype(str)
            ==
            str(poliza)
        ]

    # =====================================================
    # FILTRAR POR FECHA
    # =====================================================

    def por_fecha(self, fecha):

        if "FECHA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[
            self.df["FECHA"] == fecha
        ]

    # =====================================================
    # BUSCAR TEXTO
    # =====================================================

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

    # =====================================================
    # COLUMNAS NUMÉRICAS
    # =====================================================

    def columnas_numericas(self):

        columnas = []

        for columna in self.df.columns:

            serie = pd.to_numeric(
                self.df[columna],
                errors="coerce"
            )

            if serie.notna().sum() > 0:
                columnas.append(columna)

        return columnas

    # =====================================================
    # TOTAL DE COLUMNA
    # =====================================================

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

    # =====================================================
    # EXISTE TEXTO
    # =====================================================

    def contiene(self, texto):

        return len(
            self.buscar(texto)
        ) > 0