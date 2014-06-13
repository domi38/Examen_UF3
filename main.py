__author__ = 'alex'

from Cliente import Cliente
from coche import Coche

print("")
print("-----> BARBIE ALQUILER DE COCHES <-----")
def menu():
    print("")
    print("¿Que desea hacer?")
    print(" 0-.Alquilar coche")
    print(" 1-.Listar coches disponibles ")
    print(" 2-.Listar los coches alquilados en este momento")
    print(" 3-.Añadir un nuevo coche")
    print(" 4-.Concocer los ingresos totales obtenidos en un periodo de fechas")
    print(" 5-.Salir")

eleccion = 0
eleccionMovi = 0
varNombre = ""
menu()

while eleccion != 5:
    eleccion = int(input())

    #ALQUILAR COCHE
    if eleccion == 0:

        print("Introduzca su Dni/Nif:")
        nifIntro=str(input())
        Cliente = Cliente(nifIntro)
        if Cliente.CheckCliente(nifIntro):

            print("Quiere algun coche en concreto?")
            print("")
            print("Introduzca la matrcula del coxe que desea:")
            matricula=str(input())

            Coche = Coche(matricula,"")

            if Coche.CheckMatricula(matricula):

                print("Disponible")

                menu()



        print("NO ENCONTRADO")
        menu()

    if eleccion == 1:

        Condicio = "SI"

        print("Lista de coches disponibles:")

        Coche = Coche("",Condicio)
        Coche.CheckCochesDisponibles(Condicio)

        menu()

    if eleccion == 2:

        Condicio = "NO"

        print("Lista de coches disponibles:")

        Coche = Coche("",Condicio)

        Coche.CheckCochesAlquilados()

        menu()
    


if eleccion == 5:
    print("")
    print("CERRANDO...")
# print("Quiere algun coche en concreto?")
#             print("")
#             print("Introduzca la matrcula del coxe que desea:")
#             matricula=str(input())
#
#             Coche = Coche(matricula)
#
#             if Coche.CheckMatricula(matricula):
#
#                 print("Disponible")
#
#
#             print("Lo sentimos pero el coche que desea no esta disponible en estos momentos.")
#
#         print("Lo sentimos pero no esta registrado como cliente.")
#         menu()