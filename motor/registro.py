"""
=========================================================
SAF v13.0
Registro Central del Motor
=========================================================
"""

# =====================================================
# REGLAS
# =====================================================

from motor.reglas.regla_uuid import ReglaUUID
from motor.reglas.regla_rfc import ReglaRFC
from motor.reglas.regla_cfdi import ReglaCFDI
from motor.reglas.regla_libro import ReglaLibroMayor
from motor.reglas.regla_balanza import ReglaBalanza
from motor.reglas.regla_diario import ReglaDiario

# =====================================================
# CRUCES
# =====================================================

from motor.cruces.cruce_cfdi_ingresos import CruceCFDIIngresos
from motor.cruces.cruce_cfdi_libro import CruceCFDILibro
from motor.cruces.cruce_cfdi_auxiliar import CruceCFDIAuxiliar
from motor.cruces.cruce_libro_balanza import CruceLibroBalanza
from motor.cruces.cruce_uuid_libro import CruceUUIDLibro


def obtener_reglas():

    return [

        ReglaUUID(),

        ReglaRFC(),

        ReglaCFDI(),

        ReglaLibroMayor(),

        ReglaBalanza(),

        ReglaDiario()

    ]


def obtener_cruces():

    return [

        CruceCFDIIngresos(),

        CruceCFDILibro(),

        CruceCFDIAuxiliar(),

        CruceLibroBalanza(),

        CruceUUIDLibro()

    ]