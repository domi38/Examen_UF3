__author__ = 'alumne'
import re
class ComprovacioDni:
    def validacio_dni(nif):
        numeros="1234567890"
        taula_lletres="TRWAGMYFPDXBIJZSQVHLCKE"
        if (len(nif)==9):
            lletraControl=nif[8].upper()
            dni=nif[:8]
            if (len(dni)==len([n for n in dni if n in numeros])):
                if taula_lletres[int(dni)%23]==lletraControl:
                    print("Nif correcto")
                    return True
                else:
                    print("Error:Nif Introducido no es correcto")
            else:
                print("Error:Nif Introducido no es correcto")
                return False
        else:
            print("Error:Nif Introducido no es correcto")
            return False