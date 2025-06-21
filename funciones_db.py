import sqlite3

conexion = sqlite3.connect('base_datos_bicicleteria.db')

def crear_tabla_usuarios():
    conexion.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        dni INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT NOT NULL,
        telefono INTEGER NOT NULL);''')
    conexion.commit()
    
def buscar_usuario(dni):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM usuarios WHERE dni = ?''',(dni,))
    admin = cursor.fetchall()
    if not admin:
        return "No existe el usuario"
    else:
        return print(f"Bienvenido usuario {admin[0][1]} {admin[0][2]}")

def registrar_usuario(lista_atributos):
    conexion.execute('''INSERT INTO usuarios (dni, nombre, apellido, correo, telefono) VALUES (?,?,?,?,?)''', lista_atributos)
    print("Usuario administrador registrado correctamente")
    conexion.commit()


