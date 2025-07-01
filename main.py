from funciones.menus import *
from funciones.registro_ingreso import *
from funciones.registrar_producto import *
from funciones.sql_funciones import *

crear_tablas()
dni = 0


while dni == 0:
    #limpiar_pantalla()
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

#BUCLE ADMIN        
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
        case "5":
            limpiar_pantalla()
            exportar_csv("transacciones")
            time.sleep(3)
        case "6":
            limpiar_pantalla()
            print("Saliendo del sistema...")
            time.sleep(3)
            dni = 0
            exit()
        case _:
            print("Opcion no disponible")
            time.sleep(2)


#BUCLE USUARIO        
while dni != 41877605 and dni != 0:
    limpiar_pantalla()
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
            exit()
        case _:
            print("Opcion no disponible")
            time.sleep(2)
conexion.close()