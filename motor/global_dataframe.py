"""
=========================================================
SAF v3.3
DataFrame Global
=========================================================
"""

import pandas as pd


def construir_dataframe_global(repo):

    lista = []

    for tipo in repo.tipos():

        hojas = repo.obtener(tipo)

        for hoja, df in hojas.items():

            copia = df.copy()

            copia.insert(
                0,
                "TIPO_DOCUMENTO",
                tipo
            )

            copia.insert(
                0,
                "HOJA",
                hoja
            )

            lista.append(copia)

    if not lista:

        return pd.DataFrame()

    return pd.concat(

        lista,

        ignore_index=True,

        sort=False

    )