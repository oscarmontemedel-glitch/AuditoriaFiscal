"""
=========================================================
SAF v2.2
Motor de Tipado Inteligente
=========================================================
"""

import pandas as pd


COLUMNAS_DECIMALES = {

    "TOTAL",
    "SUBTOTAL",
    "IVA",
    "ISR",
    "IMPORTE",
    "CARGO",
    "ABONO",
    "SALDO",
    "SALDO_INICIAL",
    "SALDO_FINAL"

}


COLUMNAS_FECHA = {

    "FECHA"

}


def convertir_decimal(serie):

    serie = (
        serie.astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.strip()
    )

    return pd.to_numeric(
        serie,
        errors="coerce"
    )


def convertir_fecha(serie):

    return pd.to_datetime(

        serie,

        errors="coerce",

        dayfirst=True

    )


def tipar_dataframe(df):

    for columna in df.columns:

        if columna in COLUMNAS_DECIMALES:

            df[columna] = convertir_decimal(
                df[columna]
            )

        elif columna in COLUMNAS_FECHA:

            df[columna] = convertir_fecha(
                df[columna]
            )

    return df