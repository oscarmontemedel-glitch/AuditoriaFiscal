"""
=========================================================
SAF v9.0
Adaptador Diario General
=========================================================
"""

import re
import pandas as pd


class AdaptadorDiario:

    def __init__(self, repo):

        self.repo = repo

    def obtener(self):

        hojas = self.repo.obtener("DIARIO")

        if not hojas:

            print("⚠ No se encontró Diario General.")

            return pd.DataFrame()

        movimientos = []

        for nombre_hoja, df in hojas.items():

            if df.empty:
                continue

            tipo_actual = ""
            poliza_actual = ""
            fecha_actual = ""

            for _, fila in df.iterrows():

                valores = []

                for v in fila.tolist():

                    if pd.isna(v):
                        continue

                    texto = str(v).strip()

                    if texto != "":
                        valores.append(texto)

                if not valores:
                    continue

                # ==========================================
                # Detectar encabezado de póliza
                # ==========================================

                if len(valores) >= 3:

                    if (
                        re.fullmatch(r"[A-Z]{2}", valores[0])
                        and valores[1].isdigit()
                    ):

                        tipo_actual = valores[0]

                        poliza_actual = valores[1]

                        fecha_actual = valores[2]

                        continue

                # ==========================================
                # Buscar cuenta contable
                # ==========================================

                cuenta = None

                for valor in valores:

                    if re.fullmatch(r"\d{4}-\d{2}-\d{3}", valor):

                        cuenta = valor

                        break

                if cuenta is None:
                    continue

                descripcion = ""

                if len(valores) > 1:

                    descripcion = " | ".join(valores[1:])

                movimientos.append({

                    "TIPO": tipo_actual,

                    "POLIZA": poliza_actual,

                    "FECHA": fecha_actual,

                    "CUENTA": cuenta,

                    "DESCRIPCION": descripcion,

                    "HOJA": nombre_hoja

                })

        diario = pd.DataFrame(movimientos)

        print()
        print("===================================")
        print("ADAPTADOR DIARIO")
        print("===================================")

        print(f"Movimientos : {len(diario)}")

        return diario