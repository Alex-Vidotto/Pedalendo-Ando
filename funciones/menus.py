import os
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu_bienvenida():
    print("1. Ingresar usuario")
    print("2. Registrarse")
    print("3. Salir")

#MENUS USUSARIO
def menu_principal_cliente():
    print("MENÚ PRINCIPAL:")
    print("1  Comprar Bicicletas")
    print("2  Comprar Accesorios y Repuestos")
    print("3  Salir")
    

#MENUS ADMINISTRADOR    
def menu_principal_admin():
    print("1. Modificar Stock de Bicicletas")
    print("2. Modificar Stock de Accesorios")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Exportar registro de trnasacciones")
    print("6. Salir") 
       
def sub_menu_modificar_precio():
    print("1. Modificar precio de Bicicleta")
    print("2. Modificar precio de Accesorio")
    print("3. Salir")
    
def sub_menu_eliminar_producto():
    print("1. Eliminar Bicicleta")
    print("2. Eliminar Accesorio")
    print("3. Salir")
