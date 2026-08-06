"""
=========================================================
SAF v3.4
Modelo Universal de Movimientos
=========================================================
"""

import pandas as pd


COLUMNAS_BASE = [

    "FECHA",

    "POLIZA",

    "CUENTA",

    "CONCEPTO",

    "RFC",

    "RFC_EMISOR",

    "RFC_RECEPTOR",

    "UUID",

    "CARGO",

    "ABONO",

    "IMPORTE"

]


def construir_movimientos(global_df):

    columnas = []

    for columna in COLUMNAS_BASE:

        if columna in global_df.columns:

            columnas.append(columna)

    base = [

        "TIPO_DOCUMENTO",

        "HOJA"

    ]

    for c in base:

        if c in global_df.columns:

            columnas.insert(0, c)

    movimientos = global_df[

        columnas

    ].copy()

    return movimientos