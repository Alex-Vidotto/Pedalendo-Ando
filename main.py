from funciones.menus import *
from funciones.registro_ingreso import *
from funciones.registrar_producto import *
from funciones.sql_funciones import *

crear_tablas()
dni = 0

                
while True:
    menu_bienvenida()
    
    match input("Elija una opción: "):
        case "1":
            dni = ingresar_sistema()
            if dni == "error":
                continue
            if dni == 41877605:
                admin()
                continue
            usuario()
        case "2":
            dni = registrar_usuario()
            dni = int(dni)
            if dni == 41877605:
                admin()
                continue
            usuario()
        case "3":
            print("Saliendo del sistema...")
            time.sleep(2)
            limpiar_pantalla()
            break
        case _:
            print("Opcion no disponible")
            time.sleep(2)
            limpiar_pantalla()
            continue


conexion.close()