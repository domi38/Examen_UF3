__author__ = 'alex'

class Cliente:
    def __init__(self,varNif):
        self.varNif = varNif
    def CheckCliente(self,varNif):
        with open('clientes.txt',mode='r',encoding='utf-8')as archivo:
            for linia in archivo:
                nombre, apellido, nif= linia.split(',',2)
                Nif = nif.strip("\n")

                if varNif.upper() == Nif.upper():
                    return True