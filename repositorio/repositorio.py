"""
=========================================================
SAF v4.0
Repositorio Central de Datos
=========================================================
"""

class RepositorioDatos:

    def __init__(self):

        self._datos = {}

        self._originales = {}

    # =====================================================
    # Agregar
    # =====================================================

    def agregar(self, tipo, hoja, dataframe):

        tipo = tipo.upper()

        if tipo not in self._datos:

            self._datos[tipo] = {}

        self._datos[tipo][hoja] = dataframe

    # =====================================================
    # Agregar Original
    # =====================================================

    def agregar_original(self, archivo, hojas):

        self._originales[archivo] = hojas

    # =====================================================
    # Obtener Adaptado
    # =====================================================

    def obtener(self, tipo):

        return self._datos.get(

            tipo.upper(),

            {}

        )

    # =====================================================
    # Obtener Original
    # =====================================================

    def obtener_original(self, archivo):

        return self._originales.get(

            archivo,

            {}

        )

    # =====================================================
    # Tipos
    # =====================================================

    def tipos(self):

        return list(

            self._datos.keys()

        )

    # =====================================================
    # Total Tipos
    # =====================================================

    def total_tipos(self):

        return len(

            self._datos

        )

    # =====================================================
    # Total Hojas
    # =====================================================

    def total_hojas(self):

        total = 0

        for hojas in self._datos.values():

            total += len(hojas)

        return total

    # =====================================================
    # Resumen
    # =====================================================

    def resumen(self):

        resumen = []

        for tipo in self._datos:

            hojas = self._datos[tipo]

            registros = 0

            columnas = 0

            for df in hojas.values():

                registros += len(df)

                columnas = max(

                    columnas,

                    len(df.columns)

                )

            resumen.append({

                "Tipo": tipo,

                "Hojas": len(hojas),

                "Registros": registros,

                "Columnas": columnas

            })

        return resumen