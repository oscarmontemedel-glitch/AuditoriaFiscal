"""
=========================================================
SAF v13.0
Modelo Inteligente Diario General
=========================================================
"""

import pandas as pd


class ModeloDiario:

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
    # FILTRAR POR CUENTA
    # =====================================================

    def por_cuenta(self, cuenta):

        if "CUENTA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[
            self.df["CUENTA"]
            .fillna("")
            .astype(str)
            ==
            str(cuenta)
        ]

    # =====================================================
    # FILTRAR POR FECHA
    # =====================================================

    def por_fecha(self, fecha):

        if "FECHA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[
            self.df["FECHA"]
            ==
            fecha
        ]

    # =====================================================
    # CUENTAS
    # =====================================================

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

    # =====================================================
    # PÓLIZAS
    # =====================================================

    def polizas(self):

        if "POLIZA" not in self.df.columns:
            return []

        return (
            self.df["POLIZA"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

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

        resultado = []

        for columna in self.df.columns:

            serie = pd.to_numeric(
                self.df[columna],
                errors="coerce"
            )

            if serie.notna().sum() > 0:
                resultado.append(columna)

        return resultado

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