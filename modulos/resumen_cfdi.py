"""
=========================================================
SAF v13.0
Resumen CFDI
=========================================================
"""

import pandas as pd


class ResumenCFDI:

    def __init__(self, modelo):

        self.modelo = modelo

    def ejecutar(self):

        if self.modelo.cfdi.empty:

            return pd.DataFrame()

        cfdi = self.modelo.cfdi.dataframe()

        resumen = pd.DataFrame({

            "Concepto": [

                "Total CFDI",

                "RFC Emisores",

                "RFC Receptores",

                "UUID",

                "Importe Total"

            ],

            "Valor": [

                self.modelo.cfdi.total,

                cfdi["RFC_EMISOR"].nunique() if "RFC_EMISOR" in cfdi.columns else 0,

                cfdi["RFC_RECEPTOR"].nunique() if "RFC_RECEPTOR" in cfdi.columns else 0,

                cfdi["UUID"].nunique() if "UUID" in cfdi.columns else 0,

                self.modelo.cfdi.total_monto()

            ]

        })

        return resumen