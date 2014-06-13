__author__ = 'alex'

class Coche:
    def __init__(self,varMatricula,varCondicio):
        self.varMatricula = varMatricula
        self.varCondicio = varCondicio
    def CheckMatricula(self,varMatricula):
        with open('coches.txt',mode='r',encoding='utf-8')as archivo:
            for linia in archivo:
                matricula, marca, model,diners,disponible= linia.split(',',4)
                Disponible = disponible.strip("\n")

                if varMatricula.upper() == matricula.upper() and Disponible == "SI":


                    print(linia)


                    return True

    def CheckCochesDisponibles(self,varCondicio):
        with open('coches.txt',mode='r',encoding='utf-8')as archivo:
            for linia in archivo:
                matricula, marca, model,diners,disponible= linia.split(',',4)
                Disponible = disponible.strip("\n")

                if Disponible == varCondicio:
                    print("==============================")
                    print("Matricula: "+matricula)
                    print("Marca: "+marca)
                    print("Modelo: "+model)
                    print("Coste: "+diners+" €")
                    print("==============================")
    def CheckCochesAlquilados(self):
        with open('alquileres.txt',mode='r',encoding='utf-8')as archivo:
            for linia in archivo:
                matricula, nif, fecha_alqu,fecha_ret,importe,disponible= linia.split(',',5)
                Disponible = disponible.strip("\n")

                if Disponible == "NO":
                    print("==============================")
                    print("Matricula: "+matricula)
                    print("Nif cliente: "+nif)
                    print("Fecha de alquiler: "+fecha_alqu)
                    print("Fecha de retorno: "+fecha_ret+" €")
                    print("Coste: "+importe+" €")
                    print("==============================")

                #(matricula+","+marca+","+model+diners+"NO"+"\n")