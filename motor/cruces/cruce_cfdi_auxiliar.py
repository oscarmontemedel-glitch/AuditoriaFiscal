"""
=========================================================
SAF v13.0
Cruce CFDI vs Auxiliar
=========================================================
"""

from motor.cruces.cruce_base import CruceBase


class CruceCFDIAuxiliar(CruceBase):

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        if modelo.auxiliar.empty:
            return

        print()
        print("===================================")
        print("CRUCE CFDI vs AUXILIAR")
        print("===================================")

        total_cfdi = modelo.cfdi.total_monto()

        columnas = modelo.auxiliar.columnas_numericas()

        if not columnas:

            print("No existen columnas numéricas en Auxiliar.")
            return

        total_auxiliar = modelo.auxiliar.total_columna(

            columnas[0]

        )

        diferencia = abs(

            total_cfdi -

            total_auxiliar

        )

        print(f"CFDI       : {total_cfdi:,.2f}")
        print(f"Auxiliar   : {total_auxiliar:,.2f}")
        print(f"Diferencia : {diferencia:,.2f}")

        if diferencia > 1:

            hallazgos.agregar(

                regla="Cruce CFDI vs Auxiliar",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="AUXILIAR",

                hoja="-",

                evidencia=f"{diferencia:,.2f}",

                observacion="El importe del Auxiliar no coincide con CFDI."

            )

        cfdi = modelo.cfdi.dataframe()

        for _, fila in cfdi.iterrows():

            uuid = str(

                fila.get("UUID", "")

            ).strip()

            if uuid == "":
                continue

            if not modelo.auxiliar.contiene(uuid):

                hallazgos.agregar(

                    regla="UUID sin Auxiliar",

                    riesgo="MEDIO",

                    prioridad="MEDIA",

                    archivo="AUXILIAR",

                    hoja="-",

                    evidencia=uuid,

                    observacion="UUID no localizado en el Auxiliar."

                )

        print("Cruce terminado.")