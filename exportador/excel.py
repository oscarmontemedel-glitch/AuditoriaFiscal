"""
=========================================================
SAF v3.2
Exportador Profesional Excel
=========================================================
"""

from pathlib import Path
import pandas as pd


class ExportadorExcel:

    def __init__(self):

        self.carpeta = Path("Reportes")

        self.carpeta.mkdir(exist_ok=True)

    def exportar(self, datos, nombre):

        ruta = self.carpeta / nombre

        with pd.ExcelWriter(
            ruta,
            engine="openpyxl"
        ) as writer:

            # Si recibe un DataFrame
            if isinstance(datos, pd.DataFrame):

                datos.to_excel(
                    writer,
                    sheet_name="Datos",
                    index=False
                )

            # Si recibe un diccionario
            elif isinstance(datos, dict):

                for hoja, df in datos.items():

                    if isinstance(df, pd.DataFrame):

                        df.to_excel(

                            writer,

                            sheet_name=hoja[:31],

                            index=False

                        )

        print(f"✅ {nombre} generado correctamente.")