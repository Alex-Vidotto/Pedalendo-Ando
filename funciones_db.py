import sqlite3
from datetime import date

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
    
def crear_tabla_transacciones():
    conexion.execute('''CREATE TABLE IF NOT EXISTS transacciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha  NOT NULL,
        tipo_operacion TEXT NOT NULL,
        monto REAL NOT NULL);''')
    conexion.commit()
#FUNCIONES DE BUSQUEDA Y/O MODIFICACION DE DATOS
def buscar_usuario(dni):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM usuarios WHERE dni = ?''',(dni,))
    usuario = cursor.fetchone()
    if not usuario:
        return None
    else:
        return usuario

    
def precio_cantidad_bicicleta(marca, modelo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT precio, cantidad FROM bicicletas WHERE marca = ? AND modelo = ?''',(marca, modelo,))
    return cursor.fetchone()

def registrar_usuario(lista_atributos):
    conexion.execute('''INSERT INTO usuarios (dni, nombre, apellido, correo, telefono) VALUES (?,?,?,?,?)''', lista_atributos)
    conexion.commit()
    return lista_atributos[0]

def registrar_bicicleta(lista_atributos):
    conexion.execute('''INSERT INTO bicicletas (marca, modelo, rodado, precio, cantidad) VALUES (?,?,?,?,?)''', lista_atributos)
    conexion.commit()
    precio = float(lista_atributos[3])
    cantidad = int(lista_atributos[4])
    monto = precio * cantidad
    registrar_transaccion("compra", monto)
    return True

def buscar_bicicleta(marca, modelo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM bicicletas WHERE marca = ? AND modelo = ?''', (marca, modelo,))
    bicicleta = cursor.fetchone()
    if not bicicleta:
        return None
    return True 
    
def modificar_cantidad_bicicleta(marca, modelo, cantidad):
    if cantidad < 0:
        return False
    precio_cantidad = precio_cantidad_bicicleta(marca, modelo)
    if precio_cantidad is None:
        return False
    precio = precio_cantidad[0]
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE bicicletas SET cantidad = ? WHERE marca = ? AND modelo = ?''', (cantidad, marca, modelo))
    if cursor.rowcount == 0:
        return False
    monto = precio * cantidad
    registrar_transaccion("compra", monto)
    conexion.commit()
    return True


#FUNCIONES DE TRANSACIONES

def registrar_transaccion(tipo_operacion, monto):
    fecha = date.today() #registra la fecha de la transacion
    conexion.execute('''INSERT INTO transacciones (fecha, tipo_operacion, monto) VALUES (?,?,?)''', (fecha, tipo_operacion, monto))
    conexion.commit()
