"""
=========================================================
SAF v5.0
Consultas al Repositorio
=========================================================
"""

class ConsultasRepositorio:

    def __init__(self, repo):

        self.repo = repo

    def ingresos(self):

        return self.repo.obtener("INGRESOS")

    def cfdi(self):

        return self.repo.obtener("CFDI")

    def auxiliar(self):

        return self.repo.obtener("AUXILIAR")

    def libro_mayor(self):

        return self.repo.obtener("LIBRO MAYOR")

    def iva(self):

        return self.repo.obtener("IVA")

    def diario(self):

        return self.repo.obtener("DIARIO")

    def balanza(self):

        return self.repo.obtener("BALANZA")