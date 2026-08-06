"""
=========================================
Validador UUID
=========================================
"""

import re

PATRON_UUID = re.compile(
    r"^[0-9A-F]{8}-"
    r"[0-9A-F]{4}-"
    r"[0-9A-F]{4}-"
    r"[0-9A-F]{4}-"
    r"[0-9A-F]{12}$",
    re.IGNORECASE
)


def uuid_valido(uuid):

    if uuid is None:
        return False

    uuid = str(uuid).strip()

    if uuid == "":
        return False

    return bool(

        PATRON_UUID.match(uuid)

    )