"""
=========================================================
SAF v8.0
Adaptador Balanza de Comprobación
=========================================================
"""

import pandas as pd


class AdaptadorBalanza:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("BALANZA")

        if not hojas:

            print("⚠ No se encontró Balanza.")

            return pd.DataFrame()

        registros = []

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

            col_cuenta = buscar("CUENTA")

            col_descripcion = buscar(
                "DESCRIPCIÓN DE LA CUENTA",
                "DESCRIPCION DE LA CUENTA"
            )

            col_inicial = buscar("SALDO INICIAL")

            col_cargos = buscar("TOTAL DE CARGOS")

            col_abonos = buscar("TOTAL DE ABONOS")

            col_final = buscar("SALDO FINAL")

            for _, fila in df.iterrows():

                cuenta = fila.get(col_cuenta)

                if pd.isna(cuenta):
                    continue

                registros.append({

                    "CUENTA": cuenta,

                    "DESCRIPCION": fila.get(col_descripcion),

                    "SALDO_INICIAL": fila.get(col_inicial),

                    "CARGOS": fila.get(col_cargos),

                    "ABONOS": fila.get(col_abonos),

                    "SALDO_FINAL": fila.get(col_final),

                    "HOJA": nombre_hoja

                })

        balanza = pd.DataFrame(registros)

        print()
        print("===================================")
        print("ADAPTADOR BALANZA")
        print("===================================")
        print(f"Cuentas : {len(balanza)}")

        return balanza