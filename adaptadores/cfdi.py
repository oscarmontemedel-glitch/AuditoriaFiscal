"""
=========================================================
SAF v6.1
Adaptador CFDI
=========================================================
"""

import pandas as pd


class AdaptadorCFDI:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("CFDI")

        if not hojas:

            return pd.DataFrame()

        lista = []

        for nombre_hoja, df in hojas.items():

            columnas = {

                c.upper(): c

                for c in df.columns

            }

            if "UUID" not in columnas:

                continue

            salida = pd.DataFrame()

            salida["UUID"] = df[columnas["UUID"]]

            if "RFC EMISOR" in columnas:
                salida["RFC_EMISOR"] = df[columnas["RFC EMISOR"]]
            else:
                salida["RFC_EMISOR"] = ""

            if "RFC RECEPTOR" in columnas:
                salida["RFC_RECEPTOR"] = df[columnas["RFC RECEPTOR"]]
            else:
                salida["RFC_RECEPTOR"] = ""

            if "FECHA" in columnas:
                salida["FECHA"] = df[columnas["FECHA"]]
            else:
                salida["FECHA"] = ""

            if "TOTAL" in columnas:
                salida["TOTAL"] = pd.to_numeric(
                    df[columnas["TOTAL"]],
                    errors="coerce"
                ).fillna(0)
            else:
                salida["TOTAL"] = 0

            if "ESTATUS" in columnas:
                salida["ESTATUS"] = df[columnas["ESTATUS"]]
            else:
                salida["ESTATUS"] = ""

            salida["HOJA"] = nombre_hoja

            lista.append(salida)

        if not lista:

            return pd.DataFrame()

        cfdi = pd.concat(

            lista,

            ignore_index=True

        )

        cfdi = cfdi.drop_duplicates()

        return cfdi