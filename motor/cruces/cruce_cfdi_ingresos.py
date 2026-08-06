"""
=========================================================
SAF v13.0
Cruce CFDI vs DM Ingresos
=========================================================
"""

import pandas as pd

from motor.cruces.cruce_base import CruceBase


class CruceCFDIIngresos(CruceBase):

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        if modelo.ingresos.empty:
            return

        print()
        print("===================================")
        print("CRUCE CFDI vs DM INGRESOS")
        print("===================================")

        cfdi = modelo.cfdi.dataframe()

        ingresos = modelo.ingresos.dataframe()

        total_cfdi = modelo.cfdi.total_monto()

        total_ingresos = modelo.ingresos.total_ingresos()

        diferencia = abs(

            total_cfdi -

            total_ingresos

        )

        print(f"CFDI       : {total_cfdi:,.2f}")
        print(f"Ingresos   : {total_ingresos:,.2f}")
        print(f"Diferencia : {diferencia:,.2f}")

        if diferencia > 1:

            hallazgos.agregar(

                regla="Cruce CFDI vs Ingresos",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="DM INGRESOS",

                hoja="-",

                evidencia=f"{diferencia:,.2f}",

                observacion="Los ingresos registrados no coinciden con el total de CFDI."

            )

        if "UUID" in cfdi.columns:

            duplicados = (

                cfdi["UUID"]

                .duplicated(

                    keep=False

                )

            )

            for _, fila in cfdi[duplicados].iterrows():

                hallazgos.agregar(

                    regla="UUID Duplicado",

                    riesgo="ALTO",

                    prioridad="ALTO",

                    archivo="CFDI",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("UUID", ""),

                    observacion="UUID duplicado detectado."

                )

        print("Cruce terminado.")