"""
=========================================
Validador Importes
=========================================
"""

import pandas as pd


def convertir_numero(valor):

    try:

        return float(

            str(valor)

            .replace(",", "")

            .replace("$", "")

        )

    except Exception:

        return 0


def importe_valido(valor):

    return convertir_numero(

        valor

    ) > 0


def es_cero(valor):

    return convertir_numero(

        valor

    ) == 0


def es_negativo(valor):

    return convertir_numero(

        valor

    ) < 0