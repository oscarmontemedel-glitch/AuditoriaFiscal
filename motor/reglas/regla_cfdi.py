"""
=========================================================
SAF v13.0
Regla CFDI
=========================================================
"""

class ReglaCFDI:

    def ejecutar(self, modelo, hallazgos):

        if modelo.cfdi.empty:
            return

        print("Validando CFDI...")

        df = modelo.cfdi.dataframe()

        # ==========================================
        # TOTAL <= 0
        # ==========================================

        for _, fila in df.iterrows():

            try:

                total = float(fila.get("TOTAL", 0))

            except Exception:

                total = 0

            if total <= 0:

                hallazgos.agregar(

                    regla="CFDI Total",

                    riesgo="ALTO",

                    prioridad="ALTO",

                    archivo="CFDI",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("UUID", ""),

                    observacion="CFDI con importe menor o igual a cero."

                )

        # ==========================================
        # RFC EMISOR VACÍO
        # ==========================================

        if "RFC_EMISOR" in df.columns:

            vacios = (

                df["RFC_EMISOR"]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            )

            for _, fila in df[vacios].iterrows():

                hallazgos.agregar(

                    regla="RFC Emisor",

                    riesgo="CRITICO",

                    prioridad="CRITICO",

                    archivo="CFDI",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("UUID", ""),

                    observacion="RFC emisor vacío."

                )

        # ==========================================
        # RFC RECEPTOR VACÍO
        # ==========================================

        if "RFC_RECEPTOR" in df.columns:

            vacios = (

                df["RFC_RECEPTOR"]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            )

            for _, fila in df[vacios].iterrows():

                hallazgos.agregar(

                    regla="RFC Receptor",

                    riesgo="CRITICO",

                    prioridad="CRITICO",

                    archivo="CFDI",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("UUID", ""),

                    observacion="RFC receptor vacío."

                )

        # ==========================================
        # FECHA VACÍA
        # ==========================================

        if "FECHA" in df.columns:

            vacios = (

                df["FECHA"]

                .fillna("")

                .astype(str)

                .str.strip()

                == ""

            )

            for _, fila in df[vacios].iterrows():

                hallazgos.agregar(

                    regla="Fecha CFDI",

                    riesgo="MEDIO",

                    prioridad="MEDIA",

                    archivo="CFDI",

                    hoja=fila.get("HOJA", ""),

                    evidencia=fila.get("UUID", ""),

                    observacion="CFDI sin fecha."

                )

        print("OK")