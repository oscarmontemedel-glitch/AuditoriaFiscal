"""
=========================================
Validador Fechas
=========================================
"""

import pandas as pd


def fecha_valida(fecha):

    try:

        pd.to_datetime(

            fecha,

            errors="raise"

        )

        return True

    except Exception:

        return False