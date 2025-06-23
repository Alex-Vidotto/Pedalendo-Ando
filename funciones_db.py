import sqlite3

conexion = sqlite3.connect('base_datos_bicicleteria.db')


#CREACION DE LAS TABLAS NECESARIAS PARA EL PROYECTO
def crear_tabla_usuarios():
    conexion.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        dni INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT NOT NULL,
        telefono INTEGER NOT NULL);''')
    conexion.commit()
    
def crear_tabla_bicicletas():
    conexion.execute('''CREATE TABLE IF NOT EXISTS bicicletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        rodado REAL NOT NULL,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL);''')
    conexion.commit()
    
def crear_tabla_accesorios():
    conexion.execute('''CREATE TABLE IF NOT EXISTS accesorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL);''')
    conexion.commit()
        
#FUNCIONES DE BUSQUEDA Y/O MODIFICACION DE DATOS
def buscar_usuario(dni):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM usuarios WHERE dni = ?''',(dni,))
    admin = cursor.fetchone()
    if not admin:
        return None
    else:
        return admin

    
def precio_cantidad_bicicleta(marca, modelo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT precio, cantidad FROM bicicletas WHERE marca = ? AND modelo = ?''',(marca, modelo,))
    return cursor.fetchone()

def registrar_usuario(lista_atributos):
    conexion.execute('''INSERT INTO usuarios (dni, nombre, apellido, correo, telefono) VALUES (?,?,?,?,?)''', lista_atributos)
    conexion.commit()
    return True

def registrar_becicleta(lista_atributos):
    conexion.execute('''INSERT INTO bicicletas (marca, modelo, rodado, precio, cantidad) VALUES (?,?,?,?,?)''', lista_atributos)
    conexion.commit()
    return True
    
def modificar_cantidad_bicicleta(marca, modelo, cantidad):
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE bicicletas SET cantidad = ? WHERE marca = ? AND modelo = ?''', (cantidad, marca, modelo))
    if cursor.rowcount == 0:
        return False
    else:
        conexion.commit()
        return True


