"""
=========================================================
SAF v8.0
Suite de Auditoría Fiscal
=========================================================
"""

from config import VERSION, ARCHIVO_ZIP

from utilidades.logger import Logger
from lectores.leer_zip import analizar_zip
from auditoria.inspector import inspeccionar_zip
from exportador.excel import ExportadorExcel

from modelo.modelo_datos import ModeloDatos

from modulos.auditoria_ingresos import AuditoriaIngresos
from modulos.resumen_cfdi import ResumenCFDI
from auditoria.auditor_uuid import AuditorUUID

# ==========================================================
# MOTOR
# ==========================================================

from motor.motor_reglas import MotorReglas


# ==========================================================
# INICIALIZACIÓN
# ==========================================================

logger = Logger()
excel = ExportadorExcel()

logger.escribir("=" * 70)
logger.escribir(f"SAF v{VERSION}")
logger.escribir("=" * 70)


# ==========================================================
# ANALIZAR ZIP
# ==========================================================

logger.escribir("")
logger.escribir("Analizando expediente...")

resultado = analizar_zip(

    ARCHIVO_ZIP

)

logger.escribir(f"Excel encontrados : {len(resultado['excel'])}")
logger.escribir(f"PDF encontrados   : {len(resultado['pdf'])}")
logger.escribir(f"CSV encontrados   : {len(resultado['csv'])}")
logger.escribir(f"XML encontrados   : {len(resultado['xml'])}")


# ==========================================================
# INSPECCIÓN
# ==========================================================

logger.escribir("")
logger.escribir("Inspeccionando expediente...")

inventario, perfiles, repo = inspeccionar_zip(

    ARCHIVO_ZIP,

    resultado["excel"]

)


# ==========================================================
# REPORTES BASE
# ==========================================================

logger.escribir("")
logger.escribir("Generando reportes base...")

excel.exportar(

    inventario,

    "Inventario.xlsx"

)

excel.exportar(

    perfiles,

    "Perfil_Datos.xlsx"

)

logger.escribir("Inventario generado correctamente.")
logger.escribir("Perfil de datos generado correctamente.")


# ==========================================================
# MODELO CENTRAL
# ==========================================================

logger.escribir("")
logger.escribir("Construyendo Modelo Central...")

modelo = ModeloDatos(

    repo

).cargar()

logger.escribir("Modelo Central listo.")


# ==========================================================
# AUDITORÍA DE INGRESOS
# ==========================================================

logger.escribir("")
logger.escribir("Ejecutando Auditoría de Ingresos...")

auditoria_ingresos = AuditoriaIngresos(

    repo

)

resultado_ingresos = auditoria_ingresos.ejecutar()

excel.exportar(

    resultado_ingresos,

    "Auditoria_Ingresos.xlsx"

)

logger.escribir("Auditoría de Ingresos terminada.")


# ==========================================================
# RESUMEN CFDI
# ==========================================================

logger.escribir("")
logger.escribir("Generando Resumen CFDI...")

resumen_cfdi = ResumenCFDI(

    modelo

).ejecutar()

excel.exportar(

    resumen_cfdi,

    "Resumen_CFDI.xlsx"

)

logger.escribir("Resumen CFDI terminado.")


# ==========================================================
# AUDITOR UUID
# ==========================================================

logger.escribir("")
logger.escribir("Ejecutando Auditor UUID...")

auditor_uuid = AuditorUUID(

    repo

)

resultado_uuid = auditor_uuid.ejecutar()

excel.exportar(

    resultado_uuid,

    "UUID_Auditoria.xlsx"

)

logger.escribir("Auditor UUID terminado.")


# ==========================================================
# MOTOR DE REGLAS
# ==========================================================

logger.escribir("")
logger.escribir("Ejecutando Motor de Reglas...")

motor = MotorReglas(

    modelo

)

hallazgos = motor.ejecutar()

excel.exportar(

    hallazgos,

    "Hallazgos.xlsx"

)

logger.escribir("Motor de Reglas terminado.")


# ==========================================================
# RESUMEN FINAL
# ==========================================================

logger.escribir("")
logger.escribir("=" * 70)
logger.escribir("RESUMEN DE EJECUCIÓN")
logger.escribir("=" * 70)

logger.escribir(f"Excel procesados : {len(resultado['excel'])}")
logger.escribir(f"PDF procesados   : {len(resultado['pdf'])}")
logger.escribir(f"CSV procesados   : {len(resultado['csv'])}")
logger.escribir(f"XML procesados   : {len(resultado['xml'])}")

logger.escribir("")
logger.escribir("Reportes generados:")

logger.escribir("   ✓ Inventario.xlsx")
logger.escribir("   ✓ Perfil_Datos.xlsx")
logger.escribir("   ✓ Auditoria_Ingresos.xlsx")
logger.escribir("   ✓ Resumen_CFDI.xlsx")
logger.escribir("   ✓ UUID_Auditoria.xlsx")
logger.escribir("   ✓ Hallazgos.xlsx")

logger.escribir("")
logger.escribir("Proceso terminado correctamente.")