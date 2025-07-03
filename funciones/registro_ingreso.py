import re
import time
from funciones.sql_funciones import *
from funciones.menus import *

def ingresar_sistema():
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        try:
            dni = int(input("Ingrese su DNI: ").strip())
            usuario = buscar_usuario(dni)        
            if usuario is not None:
                print(f"\nBienvenido/a {usuario[1]} {usuario[2]}!")
                print("Igresando....")
                time.sleep(3)
                return dni
            else:
                intentos += 1
                print("ERROR: DNI incorrectos.")
                if intentos < max_intentos:
                    print(f"Intentos restantes: {max_intentos - intentos}")
                    time.sleep(2)
        except ValueError:
            print("El DNI no debe tener caracteres que no sean numericos.")
            time.sleep(2)
    print("\nDemasiados intentos fallidos, volviendo al menu principal.")
    time.sleep(3)
    return "error"

atributo_usuario = {"DNI":"dni",
                    "nombre": "Nombre",
                    "apellido": "Apellido",
                    "correo": "Correo",
                    "telefono": "Telefono"}

def registrar_usuario_bd():
    for atributo in atributo_usuario:
        while True:
            dato = input(f"Ingrese su {atributo_usuario[atributo]}: ").strip()
            dato = dato.lower()  # dato a minúsculas
            
            if dato == "": # controla que no este vacio el dato ingresado
                print("error: el campo no puede estar vacio")
                continue
            if atributo == "DNI":
                if not dato.isdigit():# controla que todos sean numeros, al ser un str no podra ingresas -123
                    print("El DNI debe ser numérico.")
                    continue
            
            if atributo == "correo":
                patron_correo = r"^[a-z0-9]+@[a-z0-9]+.com$" # El correo tiene que ser ejemplo123@dominio.com
                if not re.match(patron_correo, dato):
                    print("formato de correo incorrecto: ejemplo123@dominio.com")
                    continue
            break
        atributo_usuario[atributo] = dato # remplaza los valores por los datos ingresados
    usuario = list(atributo_usuario.values()) # guarda los datos en forma de lista
    
    registrar_usuario(usuario)
    return usuario[0]

def exportar_archivos_csv():
    while True:
                sub_menu_exportar_registros()
                match input("Elija una opción: "):
                    case "1":
                        exportar_csv("bicicletas")
                    case "2":
                        exportar_csv("accesorios")
                    case "3":
                        exportar_csv("usuarios")
                    case "4":
                        exportar_csv("transacciones")
                    case "5":
                        print("Volviendo al menu principal.")
                        break
                    case _:
                        print("Opcion no disponible")

