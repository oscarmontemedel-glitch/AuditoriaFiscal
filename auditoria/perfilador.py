"""
=========================================================
SAF v2.3
Perfilador de Datos
=========================================================
"""

import pandas as pd


def perfilar_dataframe(df):

    perfil = []

    for columna in df.columns:

        serie = df[columna]

        perfil.append({

            "Columna": columna,

            "Tipo": str(serie.dtype),

            "Registros": len(serie),

            "Nulos": int(serie.isna().sum()),

            "Duplicados": int(serie.duplicated().sum()),

            "Unicos": int(serie.nunique()),

            "PorcentajeNulos":

                round(

                    serie.isna().mean() * 100,

                    2

                )

        })

    return pd.DataFrame(perfil)