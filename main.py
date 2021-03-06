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
        clienteEncontrado=False

        print("Introduzca su Dni/Nif:")
        nifIntro=str(input())
        Cli = Cliente(nifIntro)
        if Cli.CheckCliente(nifIntro):

            clienteEncontrado = True

            print("Quiere algun coche en concreto?")
            print("")
            print("Introduzca la matrcula del coxe que desea:")
            matricula=str(input())

            C = Coche(matricula)

            if C.CheckMatricula(matricula,nifIntro):

                print("Que disfrute del coche!!!")

            else:
                print("Coche no disponible.")

        if clienteEncontrado == False:
            print("NO ENCONTRADO")

        menu()

    if eleccion == 1:

        Condicio = "SI"

        print("Lista de coches disponibles:")

        co = Coche("")
        co.CheckCochesDisponibles(Condicio)

        menu()

    if eleccion == 2:

        Condicio = "NO"

        print("Lista de coches disponibles:")

        Coc = Coche("")

        Coc.CheckCochesAlquilados()

        menu()

    if eleccion == 3:
        print("Rellene los siguientes campos por favor:")
        print("Matricula: ")
        matricula=str(input())
        print("Marca: ")
        marca=str(input())
        print("Modelo: ")
        modelo=str(input())
        print("precio/dia: ")
        precio=str(input())

        with open('coches.txt', mode='a', encoding='utf-8')as archivo:
            archivo.write(matricula+","+marca+","+modelo+","+precio+","+"SI"+"\n")

            print("Coche registrado!!")
            menu()

    if eleccion == 4:
        print("TODO")
        menu()


if eleccion == 5:
    print("")
    print("CERRANDO...")