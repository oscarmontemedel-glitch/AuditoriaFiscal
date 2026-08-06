"""
=========================================================
SAF v13.0
Regla UUID
=========================================================
"""


class ReglaUUID:

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        print("Validando UUID...")

        # ==========================================
        # UUID VACÍOS
        # ==========================================

        vacios = modelo.cfdi.uuid_vacios()

        for _, fila in vacios.iterrows():

            hallazgos.agregar(

                regla="UUID Vacío",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="CFDI",

                hoja=fila.get("HOJA", ""),

                evidencia="",

                observacion="CFDI sin UUID."

            )

        # ==========================================
        # UUID DUPLICADOS
        # ==========================================

        duplicados = modelo.cfdi.uuid_duplicados()

        for _, fila in duplicados.iterrows():

            hallazgos.agregar(

                regla="UUID Duplicado",

                riesgo="CRITICO",

                prioridad="CRITICO",

                archivo="CFDI",

                hoja=fila.get("HOJA", ""),

                evidencia=fila.get("UUID", ""),

                observacion="UUID duplicado."

            )

        print("OK")