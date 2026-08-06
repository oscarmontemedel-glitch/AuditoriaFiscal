"""
=========================================================
SUITE DE AUDITORÍA FISCAL
Configuración General
Versión: 1.0.0
=========================================================
"""

from pathlib import Path

# =====================================================
# VERSION
# =====================================================

VERSION = "1.0.0"

# =====================================================
# RUTAS
# =====================================================

BASE_DIR = Path(__file__).parent

DATOS_DIR = BASE_DIR / "Datos"

REPORTES_DIR = BASE_DIR / "Reportes"

# =====================================================
# ARCHIVOS
# =====================================================

ARCHIVO_ZIP = DATOS_DIR / "DIKEN.zip"

LOG_FILE = REPORTES_DIR / "auditoria.log"

REPORTE_EXCEL = REPORTES_DIR / "Reporte_Auditoria_Fiscal.xlsx"

DASHBOARD = REPORTES_DIR / "Dashboard.xlsx"

# =====================================================
# FORMATOS SOPORTADOS
# =====================================================

FORMATOS_EXCEL = (
    ".xlsx",
    ".xls"
)

FORMATOS_PDF = (
    ".pdf",
)

FORMATOS_XML = (
    ".xml",
)

FORMATOS_CSV = (
    ".csv",
)

# =====================================================
# COLUMNAS IMPORTANTES
# =====================================================

COLUMNAS_RFC = [
    "RFC",
    "RFC EMISOR",
    "RFC RECEPTOR",
    "RFC_PROVEEDOR",
    "RFCCLIENTE"
]

COLUMNAS_UUID = [
    "UUID",
    "FOLIO FISCAL"
]

COLUMNAS_FECHA = [
    "FECHA",
    "FECHA TIMBRADO",
    "FECHA POLIZA",
    "FECHA PÓLIZA"
]

COLUMNAS_IMPORTE = [
    "IMPORTE",
    "TOTAL",
    "MONTO"
]

COLUMNAS_CARGO = [
    "CARGO",
    "DEBE"
]

COLUMNAS_ABONO = [
    "ABONO",
    "HABER"
]

# =====================================================
# OPCIONES
# =====================================================

MOSTRAR_LOG_CONSOLA = True

EXPORTAR_LOG = True

EXPORTAR_REPORTE = True