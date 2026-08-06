"""
=========================================================
SAF v13.0
Modelo Inteligente Balanza
=========================================================
"""

import pandas as pd


class ModeloBalanza:

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
    # BUSCAR CUENTA
    # =====================================================

    def por_cuenta(self, cuenta):

        if "CUENTA" not in self.df.columns:
            return self.df.iloc[0:0]

        return self.df[
            self.df["CUENTA"]
            .astype(str)
            == str(cuenta)
        ]

    # =====================================================
    # SALDO FINAL
    # =====================================================

    def saldo_final(self):

        if "SALDO_FINAL" not in self.df.columns:
            return 0

        return (
            pd.to_numeric(
                self.df["SALDO_FINAL"],
                errors="coerce"
            )
            .fillna(0)
            .sum()
        )

    # =====================================================
    # CARGOS
    # =====================================================

    def total_cargos(self):

        if "CARGOS" not in self.df.columns:
            return 0

        return (
            pd.to_numeric(
                self.df["CARGOS"],
                errors="coerce"
            )
            .fillna(0)
            .sum()
        )

    # =====================================================
    # ABONOS
    # =====================================================

    def total_abonos(self):

        if "ABONOS" not in self.df.columns:
            return 0

        return (
            pd.to_numeric(
                self.df["ABONOS"],
                errors="coerce"
            )
            .fillna(0)
            .sum()
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
    # TOTAL DE UNA COLUMNA
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