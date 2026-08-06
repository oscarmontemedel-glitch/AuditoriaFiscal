"""
=========================================================
SAF v10.0
Extractor Auxiliar
=========================================================

Responsabilidad

Extraer los movimientos del Auxiliar Contable.

- Detecta automáticamente la cuenta actual.
- Propaga la cuenta a cada movimiento.
- Devuelve un DataFrame limpio.

NO normaliza columnas.
NO cambia tipos.
NO realiza auditorías.
=========================================================
"""

import pandas as pd

from extractores.base import ExtractorBase


class ExtractorAuxiliar(ExtractorBase):

    def __init__(self, hojas):

        """
        hojas : dict[str, DataFrame]
        """

        self.hojas = hojas

    def obtener(self):

        if not self.hojas:

            print("⚠ No existen hojas del Auxiliar.")

            return pd.DataFrame()

        movimientos = []

        print()
        print("=" * 60)
        print("EXTRACTOR AUXILIAR")
        print("=" * 60)

        for nombre_hoja, df in self.hojas.items():

            df = self.limpiar_dataframe(df)

            if df.empty:
                continue

            cuenta_actual = None

            for _, fila in df.iterrows():

                valores = [

                    "" if pd.isna(v) else str(v).strip()

                    for v in fila.tolist()

                ]

                # -------------------------------------
                # Detectar cambio de cuenta
                # -------------------------------------

                for valor in valores:

                    if valor.upper().startswith("CUENTA"):

                        texto = valor.replace("Cuenta :", "")

                        texto = texto.replace("CUENTA :", "")

                        cuenta_actual = texto.strip()

                        break

                # -------------------------------------
                # Buscar movimiento
                # -------------------------------------

                fecha = None

                for valor in valores:

                    if "/" in valor or "-" in valor:

                        if len(valor) >= 8:

                            fecha = valor

                            break

                if fecha is None:

                    continue

                movimientos.append({

                    "CUENTA": cuenta_actual,

                    "HOJA": nombre_hoja,

                    "REGISTRO": valores

                })

        auxiliar = pd.DataFrame(movimientos)

        self.imprimir_resumen(

            "Extractor Auxiliar",

            auxiliar

        )

        return auxiliar