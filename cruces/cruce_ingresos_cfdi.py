"""
=========================================================
SAF v5.1
Cruce DM Ingresos vs CFDI
=========================================================
"""

import pandas as pd


class CruceIngresosCFDI:

    def __init__(self):

        pass


    def ejecutar(self, ingresos, cfdi):

        resumen = []

        total_ingresos = 0
        total_cfdi = 0

        # ===========================
        # DM INGRESOS
        # ===========================

        for hoja, df in ingresos.items():

            columnas = [c.upper() for c in df.columns]

            if "INGRESO" in columnas:

                col = df.columns[columnas.index("INGRESO")]

                total_ingresos += pd.to_numeric(

                    df[col],

                    errors="coerce"

                ).fillna(0).sum()

        # ===========================
        # CFDI
        # ===========================

        for hoja, df in cfdi.items():

            columnas = [c.upper() for c in df.columns]

            posibles = [

                "TOTAL",

                "IMPORTE",

                "MONTO"

            ]

            for nombre in posibles:

                if nombre in columnas:

                    col = df.columns[columnas.index(nombre)]

                    total_cfdi += pd.to_numeric(

                        df[col],

                        errors="coerce"

                    ).fillna(0).sum()

                    break

        diferencia = total_ingresos - total_cfdi

        resumen.append({

            "Concepto": "Total DM Ingresos",

            "Valor": total_ingresos

        })

        resumen.append({

            "Concepto": "Total CFDI",

            "Valor": total_cfdi

        })

        resumen.append({

            "Concepto": "Diferencia",

            "Valor": diferencia

        })

        return pd.DataFrame(resumen)