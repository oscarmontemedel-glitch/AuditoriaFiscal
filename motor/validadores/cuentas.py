"""
=========================================
Validador Cuenta Contable
=========================================
"""

import re


PATRON_CUENTA = re.compile(

    r"^\d{4}-\d{2}-\d{3}$"

)


def cuenta_valida(cuenta):

    if cuenta is None:

        return False

    cuenta = str(cuenta).strip()

    return bool(

        PATRON_CUENTA.match(cuenta)

    )