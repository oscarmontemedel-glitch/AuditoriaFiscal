"""
=========================================================
SAF v10.0
Clasificador Inteligente de Archivos
=========================================================

Clasifica automáticamente los archivos del
expediente de auditoría.

La clasificación se realiza por palabras clave
contenidas en el nombre del archivo.

=========================================================
"""


def clasificar_archivo(nombre):

    nombre = str(nombre).lower().strip()

    reglas = [

        ("cfdi", "CFDI"),

        ("libro mayor", "LIBRO MAYOR"),
        ("libromayor", "LIBRO MAYOR"),
        ("mayor", "LIBRO MAYOR"),

        ("diario", "DIARIO"),

        ("balanza", "BALANZA"),

        ("aux", "AUXILIAR"),
        ("auxiliar", "AUXILIAR"),

        ("ingresos", "INGRESOS"),
        ("dm ingresos", "INGRESOS"),

        ("iva", "IVA"),

        ("isr", "ISR"),

        ("saldo", "SALDO A FAVOR"),

        ("determinacion", "DETERMINACIÓN"),
        ("determinación", "DETERMINACIÓN")

    ]

    for palabra, categoria in reglas:

        if palabra in nombre:

            return categoria

    return "OTRO"