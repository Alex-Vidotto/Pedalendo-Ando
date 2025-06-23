from funciones import *
from funciones_db import *

crear_tabla_usuarios()
crear_tabla_bicicletas()
#crear_tabla_accesorios()

lista_atributos_usuario = ["nombre", "apellido", "correo", "telefono"]
lista_atributos_bicicleta = ["marca", "modelo", "rodado", "precio", "cantidad"]
dni = None

while True:
    menu_bienvenida()
    match input("Ingrese una opcion: "):
        case "1":
            try:
                dni = int(input("Ingrese su dni: "))
                usuario = buscar_usuario(dni)
                if usuario is not None:
                    print(f"Bienvenido {usuario[1]} {usuario[2]}")
                    break
            except ValueError:
                print("DNI invalido")
                continue
        case "2":
            try:
                dni = int(input("Ingrese su dni: "))
                if buscar_usuario(dni) is not None:
                    print(f"El usuario con DNI: {dni} ya existe") 
                    continue                 
                lista_atributos_usuario = [dni] + solicitud_atributos_registro(lista_atributos_usuario)
                registrar_usuario(lista_atributos_usuario)
            except ValueError:
                print("DNI invalido")
                continue
        case "3":
            print("Saliendo")
            break
        case _:
            print("Opcion no valida")
        
while dni != None:
    menu_principal()
    match input("Ingrese una opcion: "):
        case "1":
            print("Ingresar un nuevo producto")
            nueva_lista_atributos = solicitud_atributos_registro(lista_atributos_bicicleta)
            resultado = modificar_cantidad_bicicleta(nueva_lista_atributos[0], nueva_lista_atributos[1], nueva_lista_atributos[4])
            if resultado == False:
                registrar_becicleta(nueva_lista_atributos)
            
            
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
            
            
conexion.close()