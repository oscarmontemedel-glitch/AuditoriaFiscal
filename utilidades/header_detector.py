"""
=========================================================
SAF v2.0
Detector Inteligente de Encabezados
=========================================================
"""

import pandas as pd

PALABRAS_CLAVE = {

    "fecha",
    "rfc",
    "uuid",
    "folio",
    "concepto",
    "cargo",
    "abono",
    "saldo",
    "cuenta",
    "importe",
    "debe",
    "haber",
    "subtotal",
    "iva",
    "isr",
    "total",
    "poliza",
    "póliza",
    "numero",
    "tipo"

}


def detectar_fila_encabezado(df: pd.DataFrame) -> int:
    """
    Analiza las primeras 25 filas y determina
    cuál tiene mayor probabilidad de ser el encabezado.
    """

    limite = min(25, len(df))

    mejor_fila = 0
    mejor_puntaje = -1

    for fila in range(limite):

        puntaje = 0

        for valor in df.iloc[fila]:

            texto = str(valor).strip().lower()

            if texto == "nan":
                continue

            for palabra in PALABRAS_CLAVE:

                if palabra in texto:

                    puntaje += 1

        if puntaje > mejor_puntaje:

            mejor_puntaje = puntaje
            mejor_fila = fila

    return mejor_fila