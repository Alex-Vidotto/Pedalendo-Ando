from funciones import *
from funciones_db import *

crear_tabla_usuarios()
lista_atributos = ["nombre", "apellido", "correo", "telefono"]
DNI = None

while True:
    try:
        menu_bienvenida()
        match input("Ingrese una opcion: "):
            case "1":
                DNI = int(input("Ingrese su DNI: "))
                buscar_usuario(DNI)
                break
            case "2":
                DNI = input("Ingrese su DNI: ")
                for indice, atributo in enumerate(lista_atributos, start=1):
                    cada_atributo = input(f"Ingrese su {atributo}: ").lower()

                    lista_atributos[indice - 1] = cada_atributo
                lista_atributos = [DNI] + lista_atributos
                registrar_usuario(lista_atributos)
            case "3":
                print("Saliendo")
                break
            case _:
                print("Opcion no valida")
    except Exception as e:
            print(f"Error: {e}. Por favor, intente nuevamente.")
        
while DNI != None:
    menu_principal()
    match input("Ingrese una opcion: "):
        case "1":
            print("Ingresar un nuevo producto")
            pass
        case "2":
            print("Ingresar un nuevo accesorio")
            pass
        case "3":
            print("Modificar precio del service")
            pass
        case "4":
            print("Modificar el precio del producto")
            pass
        case "5":
            print("Modificar el precio del accesorio")
            pass
        case "6":
            print("Saliendo")
            break
        case _:
            print("Opcion no valida")