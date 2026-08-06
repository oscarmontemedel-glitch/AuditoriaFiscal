"""
=========================================================
SAF v13.0
Modelo Central
=========================================================

Construye el Modelo Central de la Suite de Auditoría Fiscal.

=========================================================
"""

from adaptadores.cfdi import AdaptadorCFDI
from adaptadores.libro_mayor import AdaptadorLibroMayor
from adaptadores.auxiliar import AdaptadorAuxiliar
from adaptadores.dm_ingresos import AdaptadorDMIngresos
from adaptadores.iva import AdaptadorIVA
from adaptadores.balanza import AdaptadorBalanza
from adaptadores.diario import AdaptadorDiario

from modelo.modelo_cfdi import ModeloCFDI
from modelo.modelo_libro import ModeloLibro
from modelo.modelo_auxiliar import ModeloAuxiliar
from modelo.modelo_ingresos import ModeloIngresos
from modelo.modelo_balanza import ModeloBalanza
from modelo.modelo_diario import ModeloDiario


class ModeloDatos:

    def __init__(self, repo):

        self.repo = repo

    def cargar(self):

        print()
        print("=" * 60)
        print("CARGANDO MODELO CENTRAL")
        print("=" * 60)

        # ==================================================
        # CFDI
        # ==================================================

        cfdi_df = AdaptadorCFDI(

            self.repo

        ).obtener()

        print(f"CFDI ............... {len(cfdi_df)}")

        # ==================================================
        # LIBRO MAYOR
        # ==================================================

        libro_df = AdaptadorLibroMayor(

            self.repo

        ).obtener()

        print(f"Libro Mayor ........ {len(libro_df)}")

        # ==================================================
        # AUXILIAR
        # ==================================================

        auxiliar_df = AdaptadorAuxiliar(

            self.repo

        ).obtener()

        print(f"Auxiliar ........... {len(auxiliar_df)}")

        # ==================================================
        # INGRESOS
        # ==================================================

        ingresos_df = AdaptadorDMIngresos(

            self.repo

        ).obtener()

        print(f"DM Ingresos ........ {len(ingresos_df)}")

        # ==================================================
        # IVA
        # ==================================================

        iva = AdaptadorIVA(

            self.repo

        ).obtener()

        print(f"IVA ................ {len(iva)}")

        # ==================================================
        # BALANZA
        # ==================================================

        balanza_df = AdaptadorBalanza(

            self.repo

        ).obtener()

        print(f"Balanza ............ {len(balanza_df)}")

        # ==================================================
        # DIARIO
        # ==================================================

        diario_df = AdaptadorDiario(

            self.repo

        ).obtener()

        print(f"Diario ............. {len(diario_df)}")

        print()
        print("=" * 60)
        print("MODELO CENTRAL LISTO")
        print("=" * 60)

        class Modelo:

            pass

        modelo = Modelo()

        # ==================================================
        # MODELOS INTELIGENTES
        # ==================================================

        modelo.cfdi = ModeloCFDI(

            cfdi_df

        )

        modelo.libro = ModeloLibro(

            libro_df

        )

        modelo.auxiliar = ModeloAuxiliar(

            auxiliar_df

        )

        modelo.ingresos = ModeloIngresos(

            ingresos_df

        )

        modelo.balanza = ModeloBalanza(

            balanza_df

        )

        modelo.diario = ModeloDiario(

            diario_df

        )

        # ==================================================
        # DATOS IVA
        # ==================================================

        modelo.iva = iva

        return modelo