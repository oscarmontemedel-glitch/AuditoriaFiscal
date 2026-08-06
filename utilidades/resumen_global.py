"""
=========================================================
SAF v3.3
Resumen Global
=========================================================
"""

import pandas as pd


def resumen_global(df):

    return pd.DataFrame({

        "Concepto": [

            "Registros",

            "Columnas"

        ],

        "Valor": [

            len(df),

            len(df.columns)

        ]

    })