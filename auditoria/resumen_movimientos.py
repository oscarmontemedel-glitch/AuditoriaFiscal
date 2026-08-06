"""
=========================================================
SAF v3.4
Resumen de Movimientos
=========================================================
"""

import pandas as pd


def generar_resumen(df):

    return pd.DataFrame({

        "Indicador": [

            "Movimientos",

            "Columnas",

            "RFC encontrados",

            "UUID encontrados"

        ],

        "Valor": [

            len(df),

            len(df.columns),

            df.filter(regex="RFC").count().sum(),

            df.filter(regex="UUID").count().sum()

        ]

    })