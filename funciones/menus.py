import os
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu_bienvenida():
    limpiar_pantalla()
    print(f"{5*'-'} BIENVENIDO A PEDALEANDO-ANDO {5*'-'}")
    print("1. Ingresar usuario")
    print("2. Registrarse")
    print("3. Salir")

#MENUS USUSARIO
def menu_principal_cliente():
    limpiar_pantalla()
    print(f"{5*'-'} MENÚ PRINCIPAL USUARIO {'-'*5}")
    print("1  Comprar Bicicletas")
    print("2  Comprar Accesorios y Repuestos")
    print("3  Salir")
    

#MENUS ADMINISTRADOR    
def menu_principal_admin():
    limpiar_pantalla()
    print(f"{5*'-'} MENÚ PRINCIPAL ADMINISTRADOR {'-'*5}")
    print("1. Modificar Stock de Bicicletas")
    print("2. Modificar Stock de Accesorios")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Exportar registro de trnasacciones")
    print("6. Salir") 
       
def sub_menu_modificar_precio():
    limpiar_pantalla()
    print(f"{5*'-'} MENÚ MODIFICAR PRECIO {'-'*5}")
    print("1. Modificar precio de Bicicleta")
    print("2. Modificar precio de Accesorio")
    print("3. Salir")
    
def sub_menu_eliminar_producto():
    limpiar_pantalla()
    print("1. Eliminar Bicicleta")
    print("2. Eliminar Accesorio")
    print("3. Salir")

def sub_menu_exportar_registros():
    limpiar_pantalla()
    print(f"{5*'-'} EXPORTAR REGISTROS DEL SISTEMA {'-'*5}")
    print("1. Exportar Bicicletas")
    print("2. Exportar Accesorios")
    print("3. Exportar Usuarios")
    print("4. Exportar Transacciones")
    print("5. Salir")