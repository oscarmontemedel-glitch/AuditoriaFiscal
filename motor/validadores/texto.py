"""
=========================================
Utilerías Texto
=========================================
"""


def limpiar(texto):

    if texto is None:

        return ""

    return (

        str(texto)

        .strip()

        .upper()

    )


def vacio(texto):

    return limpiar(texto) == ""