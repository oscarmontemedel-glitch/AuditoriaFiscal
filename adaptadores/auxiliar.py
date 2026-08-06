"""
=========================================================
SAF v8.0
Adaptador Auxiliar
=========================================================
"""

import pandas as pd


class AdaptadorAuxiliar:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("AUXILIAR")

        if not hojas:

            print("⚠ No se encontró Auxiliar.")

            return pd.DataFrame()

        resultado = []

        for nombre_hoja, df in hojas.items():

            if df.empty:
                continue

            cuenta_actual = ""

            for _, fila in df.iterrows():

                segunda = str(fila.iloc[1]) if len(fila) > 1 else ""

                if segunda.startswith("Cuenta :"):

                    cuenta_actual = segunda.replace(
                        "Cuenta :",
                        ""
                    ).strip()

                    continue

                tipo = fila.get("TIPO")

                if pd.isna(tipo) or str(tipo).strip() == "":

                    continue

                resultado.append({

                    "CUENTA": cuenta_actual,

                    "TIPO": fila.get("TIPO"),

                    "NUMERO": fila.get("NUMERO"),

                    "FECHA": fila.get("FECHA"),

                    "CONCEPTO": fila.get("CONCEPTO"),

                    "SALDO_INICIAL": fila.get("SALDO INICIAL"),

                    "DEBE": fila.get("DEBE"),

                    "HABER": fila.get("HABER"),

                    "SALDO": fila.get("SALDO"),

                    "HOJA": nombre_hoja

                })

        auxiliar = pd.DataFrame(resultado)

        print()
        print("===================================")
        print("ADAPTADOR AUXILIAR")
        print("===================================")
        print(f"Movimientos : {len(auxiliar)}")

        return auxiliar