"""
=========================================================
Detector Inteligente de Encabezados
=========================================================
"""

PALABRAS_CLAVE = [

    "fecha",

    "rfc",

    "uuid",

    "folio",

    "concepto",

    "cargo",

    "abono",

    "saldo",

    "cuenta",

    "importe",

    "debe",

    "haber",

    "subtotal",

    "iva",

    "isr",

    "total"

]


def detectar_encabezado(df):

    """
    Busca la fila con mayor cantidad de
    palabras clave.
    """

    mejor_fila = 0

    mayor_puntaje = -1

    limite = min(20, len(df))

    for fila in range(limite):

        puntaje = 0

        for valor in df.iloc[fila]:

            texto = str(valor).lower()

            for palabra in PALABRAS_CLAVE:

                if palabra in texto:

                    puntaje += 1

        if puntaje > mayor_puntaje:

            mayor_puntaje = puntaje

            mejor_fila = fila

    return mejor_fila