"""
=========================================
Validador RFC
=========================================
"""

import re


PATRON_RFC = re.compile(

    r"^[A-Z&Ñ]{3,4}"

    r"[0-9]{6}"

    r"[A-Z0-9]{3}$",

    re.IGNORECASE

)


def rfc_valido(rfc):

    if rfc is None:
        return False

    rfc = str(rfc).strip().upper()

    if rfc == "":
        return False

    return bool(

        PATRON_RFC.match(rfc)

    )