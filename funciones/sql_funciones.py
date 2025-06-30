import sqlite3
from datetime import date

conexion = sqlite3.connect('base_datos_bicicleteria.db')


#CREACION DE LAS TABLAS NECESARIAS PARA EL PROYECTO
def crear_tablas():
    
    conexion.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        dni INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT NOT NULL,
        telefono INTEGER NOT NULL);''')
    
    conexion.execute('''CREATE TABLE IF NOT EXISTS bicicletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        rodado REAL NOT NULL,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL);''')

    conexion.execute('''CREATE TABLE IF NOT EXISTS accesorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL);''')

    conexion.execute('''CREATE TABLE IF NOT EXISTS transacciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha  NOT NULL,
        tipo_operacion TEXT NOT NULL,
        monto REAL NOT NULL);''')
    conexion.commit()

#MOSTRAR CATALOGOS
def mostrar_catalogo(nombre_tabla):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM {nombre_tabla}''')
    lista = cursor.fetchall()
    if not lista:
        print(f"No hay {nombre_tabla} registradas.")
        return None
    else:
        print(f"Catalogo de {nombre_tabla}:")
        for item in lista:
            print(item)
        return True


def buscar_usuario(dni):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM usuarios WHERE dni = ?''',(dni,))
    usuario = cursor.fetchone()
    if not usuario:
        return None
    else:
        return usuario

def registrar_usuario(lista_atributos):
    conexion.execute('''INSERT INTO usuarios (dni, nombre, apellido, correo, telefono) VALUES (?,?,?,?,?)''', lista_atributos)
    conexion.commit()
    return True

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

def precio_bicicleta(marca, modelo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT precio FROM bicicletas WHERE marca = ? AND modelo = ?''',(marca, modelo,))
    precio = cursor.fetchone()
    return precio[0]
 
def cantidad_bicicleta(marca, modelo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT cantidad FROM bicicletas WHERE marca = ? AND modelo = ?''',(marca, modelo,))
    cantidad = cursor.fetchone()
    if not cantidad:
        return None
    return cantidad[0]
   
def modificar_cantidad_bicicleta(marca, modelo, cantidad):
    if cantidad < 0:
        return False
    precio = precio_bicicleta(marca, modelo)
    if precio is None:
        return False
    precio = precio
    cantidad_actual = cantidad_bicicleta(marca, modelo)
    cantidad += cantidad_actual
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE bicicletas SET cantidad = ? WHERE marca = ? AND modelo = ?''', (cantidad, marca, modelo))
    if cursor.rowcount == 0:
        return False
    monto = precio * cantidad
    registrar_transaccion("compra", monto)
    conexion.commit()
    return True

def buscar_accesorio_precio(nombre):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT precio FROM accesorios WHERE nombre = ?''', (nombre,))
    precio = cursor.fetchone()
    return precio[0]

def buscar_accesorio_cantidad(nombre):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT cantidad FROM accesorios WHERE nombre = ?''', (nombre,))
    accesorio = cursor.fetchone()
    if not accesorio:
        return None
    cantidad = accesorio[0]
    return cantidad

def modificar_cantidad_accesorio(nombre, cantidad):
    if cantidad < 0:
        return False
    cantidad_actual = buscar_accesorio_cantidad(nombre)
    cantidad_nueva = cantidad + cantidad_actual
    precio = buscar_accesorio_precio(nombre)
    monto = precio * cantidad
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE accesorios SET cantidad = ? WHERE nombre = ?''', (cantidad_nueva, nombre))
    if cursor.rowcount == 0:
        return False
    registrar_transaccion("compra", monto)
    conexion.commit()
    return True

def registrar_accesorio(lista_atributos):
    conexion.execute('''INSERT INTO accesorios (nombre, cantidad, precio) VALUES (?,?,?)''', lista_atributos)
    conexion.commit()
    precio = float(lista_atributos[2])
    cantidad = int(lista_atributos[1])
    monto = precio * cantidad
    registrar_transaccion("compra", monto)
    return True


#FUNCIONES DE TRANSACIONES

def registrar_transaccion(tipo_operacion, monto):
    fecha = date.today() #registra la fecha de la transacion
    conexion.execute('''INSERT INTO transacciones (fecha, tipo_operacion, monto) VALUES (?,?,?)''', (fecha, tipo_operacion, monto))
    conexion.commit()

