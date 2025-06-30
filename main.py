from funciones.menus import *
from funciones.registro_ingreso import *
from funciones.registrar_producto import *
from funciones.sql_funciones import *

crear_tablas()
dni = 0

while True:
    limpiar_pantalla()
    menu_bienvenida()
    
    match input("Elija una opción: "):
        case "1":
            dni = ingresar_sistema()
            if dni == "error":
                continue
            break
        case "2":
            dni = registrar_usuario_bd()
            dni = int(dni)
            break
        case "3":
            limpiar_pantalla()
            break
        case _:
            print("Opcion no disponible")
            continue

        
while dni == 41877605:
    limpiar_pantalla()
    menu_principal_admin()
    match input("Elija una opción: "):
        case "1":
            producto_bicicleta()
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
                    print("Volviendo al menu principal.")
                    time.sleep(3)
                    continue
                case _:
                    print("Opcion no disponible")
        case "4":
            
            break
            if dato is not None:
                print("hola mundo")
                
conexion.close()