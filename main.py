from funciones.menus import *
from funciones.registro_ingreso import *
from funciones.registrar_producto import *
from funciones.sql_funciones import *

crear_tablas()

while True:
    limpiar_pantalla()
    menu_bienvenida()
    
    match input("Elija una opción: "):
        case "1":
            dato = ingresar_sistema()
            if dato == "error":
                continue
            break
        case "2":
            dato = registrar_usuario_bd()
            break
        case "3":
            dato = [0]  # Valor por defecto para salir del bucle
            limpiar_pantalla()
            break
        case _:
            print("Opcion no disponible")
            continue

dni = dato[0]
        
while dni == 41877605:
    limpiar_pantalla()
    menu_principal_admin()
    match input("Elija una opción: "):
        case "1":
            producto_bicicleta()
            mostrar_catalogo("bicicletas")
            time.sleep(4)
        case "2":
            producto_accesorio()
            time.sleep(4)
        case "3":
            sub_menu_modificar_precio()
            match input("Elija una opción: "):
                case "1":
                    dato = modificar_precio_bicicleta()
                    time.sleep(2)
                case "2":
                    dato = modificar_precio_accesorio()
                    time.sleep(2)
                case "3":
                    continue
                case _:
                    print("Opcion no disponible")
        case "4":
            #dato = modificar_precio_producto()
            break
            if dato is not None:
                print("hola mundo")
                
conexion.close()