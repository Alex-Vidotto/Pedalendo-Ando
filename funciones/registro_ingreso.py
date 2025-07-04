import re
import time
from funciones.sql_funciones import *
from funciones.menus import *
from funciones.registrar_producto import *

def ingresar_sistema():
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        try:
            dni = int(input("Ingrese su DNI: ").strip())
            usuario = buscar_usuario(dni)        
            if usuario is not None:
                print(f"Bienvenido/a {usuario[1]} {usuario[2]}!")
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
            if atributo == "nombre" or atributo == "apellido":
                if not dato.isalpha(): # funcion que controla que sean letras
                    print(f"El {atributo_usuario[atributo]} tienen que ser letras.")
                    continue
                
            if atributo == "telefono":
                if not dato.isdigit() and len(dato) < 8: # revisa que solo sean digitos y  que tengan mas de 8 numeros
                    print(f"El {atributo_usuario[atributo]} debe ser numeros.")
                    continue
                    
            if atributo == "DNI":
                if not dato.isdigit() and len(dato) < 8:# controla que todos sean numeros, al ser un str no podra ingresas -123 y que sean 8 como minimo
                    print("El DNI debe estar en formato numero.")
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
    print(f"Usuario {usuario[1]} {usuario[2]} registrado correctamente.")
    time.sleep(2)
    return usuario[0]

def exportar_archivos_csv():
    while True:
                sub_menu_exportar_registros()
                match input("Elija una opción: "):
                    case "1":
                        exportar_csv("bicicletas")
                        time.sleep(4)
                    case "2":
                        exportar_csv("accesorios")
                        time.sleep(4)
                    case "3":
                        exportar_csv("usuarios")
                        time.sleep(4)
                    case "4":
                        exportar_csv("transacciones")
                        time.sleep(4)
                    case "5":
                        print("Volviendo al menu principal.")
                        time.sleep(3)
                        break
                    case _:
                        print("Opcion no disponible")



def admin():
    #BUCLE ADMIN        
    while True:
        menu_principal_admin()
        match input("Elija una opción: "):
            case "1":
                mostrar_tabla("bicicletas")
                producto_bicicleta()
                time.sleep(4)
            case "2":
                mostrar_tabla("accesorios")
                producto_accesorio()
                time.sleep(4)
            case "3":
                sub_menu_modificar_precio()
                match input("Elija una opción: "):
                    case "1":
                        mostrar_tabla("bicicletas")
                        dato = modificar_precio_bicicleta()
                        time.sleep(2)
                    case "2":
                        mostrar_tabla("accesorios")
                        dato = modificar_precio_accesorio()
                        time.sleep(2)
                    case "3":
                        print("Volviendo al menu principal.")
                        time.sleep(3)
                        continue
                    case _:
                        print("Opcion no disponible")
                        time.sleep(3)
            case "4":
                sub_menu_eliminar_producto()
                match input("Elija una opción: "):
                    case "1":
                        dato = eliminar_producto_bicicleta()
                        time.sleep(2)
                    case "2":
                        dato = eliminar_producto_accesorio()
                        time.sleep(2)
                    case "3":
                        print("Volviendo al menu principal.")
                        time.sleep(3)
                        continue
                    case _:
                        print("Opcion no disponible")
                        time.sleep(3)
            case "5":
                exportar_archivos_csv()
                time.sleep(3)
            case "6":
                limpiar_pantalla()
                print("Saliendo del sistema...")
                time.sleep(3)
                dni = 0
                break
            case _:
                print("Opcion no disponible")
                time.sleep(2)

def usuario():
    #BUCLE USUARIO        
    while True:
        menu_principal_cliente()
        match input("Elija una opción: "):
            case "1":
                mostrar_tabla("bicicletas")
                comprar_bicicleta()
                time.sleep(4)
            case "2":
                mostrar_tabla("accesorios")
                comprar_accesorio()
                time.sleep(4)
            case "3":
                print("Saliendo del sistema...")
                time.sleep(2)
                break
            case _:
                print("Opcion no disponible")
                time.sleep(2)
