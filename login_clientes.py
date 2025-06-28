import os
import time
import re

# Base de datos de usuarios (en memoria)
usuarios_db = {
    "12345678": {"password": "admin123", "nombre": "Usuario Demo"},
    "87654321": {"password": "test456", "nombre": "Cliente Test"}
}

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_header():
    """Muestra el encabezado del sistema"""
    print("="*60)
    print("              SISTEMA DE BICICLETERIA")
    print("                 ACCESO AL SISTEMA")
    print("="*60)

def validar_dni(dni):
    """Valida que el DNI tenga formato correcto (solo números, 8 dígitos)"""
    return re.match(r'^\d{8}$', dni) is not None

def validar_password(password):
    """Valida que la contraseña tenga al menos 6 caracteres"""
    return len(password) >= 6

def mostrar_menu_principal():
    """Muestra el menú principal de login"""
    limpiar_pantalla()
    mostrar_header()
    print("\nMENU PRINCIPAL:")
    print("1. Loguearse")
    print("2. Registrarse")
    print("0. Salir")
    print("-" * 60)

def login():
    """Maneja el proceso de login"""
    limpiar_pantalla()
    mostrar_header()
    print("\nINICIAR SESION")
    print("-" * 60)
    
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        dni = input("Ingrese su DNI (8 digitos): ").strip()
        
        if not validar_dni(dni):
            print("ERROR: El DNI debe tener exactamente 8 digitos numericos.")
            intentos += 1
            if intentos < max_intentos:
                print(f"Intentos restantes: {max_intentos - intentos}")
                time.sleep(2)
            continue
        
        password = input("Ingrese su contraseña: ").strip()
        
        if dni in usuarios_db and usuarios_db[dni]["password"] == password:
            print(f"\nBienvenido/a {usuarios_db[dni]['nombre']}!")
            print("Login exitoso!")
            print("Redirigiendo al sistema principal...")
            time.sleep(3)
            return True
        else:
            intentos += 1
            print("ERROR: DNI o contraseña incorrectos.")
            if intentos < max_intentos:
                print(f"Intentos restantes: {max_intentos - intentos}")
                time.sleep(2)
    
    print("\nDemasiados intentos fallidos. Acceso bloqueado.")
    time.sleep(3)
    return False

def registrarse():
    """Maneja el proceso de registro"""
    limpiar_pantalla()
    mostrar_header()
    print("\nREGISTRO DE NUEVO USUARIO")
    print("-" * 60)
    
    # Solicitar DNI
    while True:
        dni = input("Ingrese su DNI (8 digitos): ").strip()
        
        if not validar_dni(dni):
            print("ERROR: El DNI debe tener exactamente 8 digitos numericos.")
            continue
        
        if dni in usuarios_db:
            print("ERROR: Este DNI ya esta registrado en el sistema.")
            opcion = input("¿Desea intentar loguearse? (s/n): ").lower()
            if opcion == 's':
                return login()
            else:
                continue
        
        break
    
    # Solicitar nombre
    while True:
        nombre = input("Ingrese su nombre completo: ").strip()
        if len(nombre) >= 2:
            break
        print("ERROR: El nombre debe tener al menos 2 caracteres.")
    
    # Solicitar contraseña
    while True:
        password = input("Ingrese una contraseña (minimo 6 caracteres): ").strip()
        
        if not validar_password(password):
            print("ERROR: La contraseña debe tener al menos 6 caracteres.")
            continue
        
        confirmar_password = input("Confirme su contraseña: ").strip()
        
        if password != confirmar_password:
            print("ERROR: Las contraseñas no coinciden.")
            continue
        
        break
    
    # Guardar usuario
    usuarios_db[dni] = {
        "password": password,
        "nombre": nombre
    }
    
    print(f"\nRegistro exitoso!")
    print(f"Usuario: {nombre}")
    print(f"DNI: {dni}")
    print("Ya puede iniciar sesion con sus credenciales.")
    
    # Preguntar si quiere loguearse inmediatamente
    opcion = input("\n¿Desea iniciar sesion ahora? (s/n): ").lower()
    if opcion == 's':
        return login()
    
    input("\nPresione Enter para continuar...")
    return False

def mostrar_usuarios_demo():
    """Muestra usuarios de demo para pruebas"""
    print("\n" + "="*60)
    print("USUARIOS DE PRUEBA DISPONIBLES:")
    print("-" * 60)
    print("DNI: 12345678 | Contraseña: admin123")
    print("DNI: 87654321 | Contraseña: test456")
    print("="*60)

def main():
    """Función principal del sistema de login"""
    print("Inicializando sistema...")
    time.sleep(1)
    
    while True:
        mostrar_menu_principal()
        mostrar_usuarios_demo()
        
        try:
            opcion = input("\nSeleccione una opcion (0-2): ").strip()
            
            if opcion == "1":
                if login():
                    # Aquí podrías llamar al menú principal de la bicicletería
                    limpiar_pantalla()
                    print("="*60)
                    print("         ACCESO CONCEDIDO AL SISTEMA")
                    print("="*60)
                    print("\nAqui se cargaria el menu principal de la bicicleteria...")
                    print("(Integrar con el codigo del menu de la tienda)")
                    input("\nPresione Enter para cerrar sesion...")
                    
            elif opcion == "2":
                registrarse()
                
            elif opcion == "0":
                limpiar_pantalla()
                mostrar_header()
                print("\nGracias por usar el sistema!")
                print("Cerrando aplicacion...")
                time.sleep(2)
                break
                
            else:
                print("ERROR: Opcion no valida. Seleccione 0, 1 o 2.")
                time.sleep(2)
                
        except KeyboardInterrupt:
            print("\n\nSaliendo del sistema...")
            break
        except Exception as e:
            print(f"ERROR inesperado: {e}")
            time.sleep(2)

# Ejecutar el programa
if __name__ == "__main__":
    main()