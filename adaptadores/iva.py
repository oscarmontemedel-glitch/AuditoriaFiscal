"""
=========================================================
SAF v8.0
Adaptador IVA
=========================================================
"""

import pandas as pd


class AdaptadorIVA:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("IVA")

        if not hojas:

            print("⚠ No se encontró Integración IVA.")

            return {}

        resultado = {}

        mapa = {

            "RET": "retenciones",

            "FISCAL": "fiscal",

            "AUX IVA": "auxiliar",

            "IVA IMP": "importacion",

            "TC": "tipo_cambio",

            "INTEGRACION": "integracion"

        }

        print()
        print("===================================")
        print("ADAPTADOR IVA")
        print("===================================")

        for hoja, df in hojas.items():

            nombre = hoja.upper().strip()

            clave = mapa.get(

                nombre,

                nombre.lower()

            )

            copia = df.copy()

            copia.columns = [

                str(c).strip().upper()

                for c in copia.columns

            ]

            copia = copia.dropna(

                how="all"

            )

            resultado[clave] = copia

            print(

                f"{clave:15} {len(copia):>8} registros"

            )

        return resultado