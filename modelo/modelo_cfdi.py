"""
=========================================================
SAF v11.0
Modelo Inteligente CFDI
=========================================================

Encapsula todas las operaciones sobre los CFDI.

Todas las reglas deberán utilizar esta clase y no
trabajar directamente con DataFrames.

=========================================================
"""

import pandas as pd


class ModeloCFDI:

    def __init__(self, dataframe):

        if dataframe is None:

            dataframe = pd.DataFrame()

        self.df = dataframe.copy()

    # =====================================================
    # Propiedades
    # =====================================================

    @property
    def columnas(self):

        return list(self.df.columns)

    @property
    def total(self):

        return len(self.df)

    @property
    def empty(self):

        return self.df.empty

    # =====================================================
    # Filtros
    # =====================================================

    def vigentes(self):

        if "ESTATUS" not in self.df.columns:

            return self.df.iloc[0:0]

        return self.df[

            self.df["ESTATUS"]

            .astype(str)

            .str.upper()

            ==

            "VIGENTE"

        ]

    def cancelados(self):

        if "ESTATUS" not in self.df.columns:

            return self.df.iloc[0:0]

        return self.df[

            self.df["ESTATUS"]

            .astype(str)

            .str.upper()

            ==

            "CANCELADO"

        ]

    # =====================================================
    # UUID
    # =====================================================

    def uuid_vacios(self):

        if "UUID" not in self.df.columns:

            return self.df.iloc[0:0]

        return self.df[

            self.df["UUID"]

            .fillna("")

            .astype(str)

            .str.strip()

            ==

            ""

        ]

    def uuid_duplicados(self):

        if "UUID" not in self.df.columns:

            return self.df.iloc[0:0]

        return self.df[

            self.df["UUID"]

            .duplicated(

                keep=False

            )

        ]

    # =====================================================
    # RFC
    # =====================================================

    def por_rfc_emisor(self, rfc):

        if "RFC_EMISOR" not in self.df.columns:

            return self.df.iloc[0:0]

        return self.df[

            self.df["RFC_EMISOR"]

            ==

            rfc

        ]

    def por_rfc_receptor(self, rfc):

        if "RFC_RECEPTOR" not in self.df.columns:

            return self.df.iloc[0:0]

        return self.df[

            self.df["RFC_RECEPTOR"]

            ==

            rfc

        ]

    # =====================================================
    # Fecha
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
    # Total
    # =====================================================

    def total_monto(self):

        if "TOTAL" not in self.df.columns:

            return 0

        return (

            pd.to_numeric(

                self.df["TOTAL"],

                errors="coerce"

            )

            .fillna(0)

            .sum()

        )

    # =====================================================
    # Utilidad
    # =====================================================

    def dataframe(self):

        return self.df.copy()