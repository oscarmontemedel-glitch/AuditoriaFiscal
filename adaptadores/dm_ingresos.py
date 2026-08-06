"""
=========================================================
SAF v8.0
Adaptador DM Ingresos
=========================================================
"""

import pandas as pd


class AdaptadorDMIngresos:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("INGRESOS")

        if not hojas:

            print("⚠ No se encontró DM de Ingresos.")

            return pd.DataFrame()

        movimientos = []

        for nombre_hoja, df in hojas.items():

            if df.empty:
                continue

            columnas = {

                str(c).strip().upper(): c

                for c in df.columns

            }

            def buscar(*nombres):

                for nombre in nombres:

                    if nombre in columnas:

                        return columnas[nombre]

                return None

            col_fecha = buscar("FECHA")

            col_poliza = buscar("PÓLIZA", "POLIZA")

            col_numero = buscar("NUMERO", "NÚMERO")

            col_concepto = buscar("CONCEPTO")

            col_ingreso = buscar("INGRESO", "INGRESOS")

            col_banco = buscar("BANCO")

            for _, fila in df.iterrows():

                movimientos.append({

                    "BANCO": fila.get(col_banco),

                    "POLIZA": fila.get(col_poliza),

                    "NUMERO": fila.get(col_numero),

                    "FECHA": fila.get(col_fecha),

                    "CONCEPTO": fila.get(col_concepto),

                    "INGRESO": fila.get(col_ingreso),

                    "HOJA": nombre_hoja

                })

        resultado = pd.DataFrame(movimientos)

        if resultado.empty:

            return resultado

        resultado.columns = [

            str(c).upper()

            for c in resultado.columns

        ]

        resultado = resultado.dropna(

            how="all"

        )

        print()

        print("===================================")
        print("ADAPTADOR DM INGRESOS")
        print("===================================")

        print(f"Hojas        : {len(hojas)}")
        print(f"Movimientos  : {len(resultado)}")

        return resultado