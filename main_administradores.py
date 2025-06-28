from funciones import *
from funciones_db import *

crear_tabla_usuarios()
crear_tabla_bicicletas()
crear_tabla_transacciones()
#crear_tabla_accesorios()

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
                else:
                    print(f"usuario no encontrado en el sistema con {dni}.")
            except ValueError:
                print("DNI invalido")
                continue
        case "2":
            try:
                dni = int(input("Ingrese su dni: "))
                if buscar_usuario(dni) is not None:
                    print(f"El usuario con DNI: {dni} ya existe") 
                    continue                 
                lista_atributos_usuario = [dni] + registrar_administrador()
                registrar_usuario(lista_atributos_usuario)
            except ValueError:
                print("DNI invalido")
                break
        case "3":
            print("Saliendo")
            break
        case _:
            print("Opcion no valida")
        
while dni != None:
    try:
        menu_principal()
        match input("Ingrese una opcion: "):
            case "1":
                print("Actualizar Stock bicicletas")
                marca = input("Ingrese la marca de la bicicleta: ").strip().lower()
                modelo = input("Ingrese el modelo de la bicicleta: ").strip().lower()
                if buscar_bicicleta(marca, modelo) is None:
                    solicitad_datos_bicicleta(marca, modelo)
                    print(f"Bicicleta registarda correctamente")
                    continue
                cantidad = int(input("Ingrese la cantidad de bicicletas: ").strip())
                modificar_cantidad_bicicleta(marca, modelo, cantidad)
                print(f"Stock actualizado correctamente")
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
    except Exception as e:
        print(f"Error: {e}")
            
conexion.close()