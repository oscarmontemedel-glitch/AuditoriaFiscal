"""
=========================================================
SAF v13.0
Regla RFC
=========================================================
"""


class ReglaRFC:

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        print("Validando RFC...")

        df = modelo.cfdi.dataframe()

        # ==========================================
        # RFC EMISOR
        # ==========================================

        if "RFC_EMISOR" in df.columns:

            for _, fila in df.iterrows():

                rfc = str(

                    fila.get("RFC_EMISOR", "")

                ).strip().upper()

                if rfc == "":

                    continue

                if len(rfc) not in (12, 13):

                    hallazgos.agregar(

                        regla="RFC Emisor",

                        riesgo="ALTO",

                        prioridad="ALTO",

                        archivo="CFDI",

                        hoja=fila.get("HOJA", ""),

                        evidencia=rfc,

                        observacion="Longitud incorrecta del RFC emisor."

                    )

        # ==========================================
        # RFC RECEPTOR
        # ==========================================

        if "RFC_RECEPTOR" in df.columns:

            for _, fila in df.iterrows():

                rfc = str(

                    fila.get("RFC_RECEPTOR", "")

                ).strip().upper()

                if rfc == "":

                    continue

                if len(rfc) not in (12, 13):

                    hallazgos.agregar(

                        regla="RFC Receptor",

                        riesgo="ALTO",

                        prioridad="ALTO",

                        archivo="CFDI",

                        hoja=fila.get("HOJA", ""),

                        evidencia=rfc,

                        observacion="Longitud incorrecta del RFC receptor."

                    )

        print("OK")