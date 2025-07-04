import sqlite3
from datetime import date, datetime
import os
import csv

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
def mostrar_tabla(nombre_tabla):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM {nombre_tabla}''')
    lista = cursor.fetchall()
    titulos = [descripcion[0] for descripcion in cursor.description]
    if not lista:
        print(f"No hay {nombre_tabla} registradas.")
        return None
    else:
        suma = 1
        tabla = []
        for titulo in titulos:
            tabla.append(titulo.upper())
        for fila in lista:
            for dato in fila:
                tabla.append(dato)
        for contenido in tabla:
            print(contenido, end=" | ")
            if (suma % (len(titulos))) == 0:
                print("\n")
            suma += 1
        return True

def contenido_tabla(nombre_tabla):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM {nombre_tabla}''')
    fila = cursor.fetchall()
    return fila

def columnas_tabla(nombre_tabla):
    cursor = conexion.cursor()
    cursor.execute(f'''PRAGMA table_info({nombre_tabla})''')
    columnas = [columna[1] for columna in cursor.fetchall()]
    return columnas

def buscar_usuario(dni):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM usuarios WHERE dni = ?''',(dni,))
    usuario = cursor.fetchone()
    if not usuario:
        return None
    else:
        return usuario

def registrar_usuario(lista_columna):
    conexion.execute('''INSERT INTO usuarios (dni, nombre, apellido, correo, telefono) VALUES (?,?,?,?,?)''', lista_columna)
    conexion.commit()
    return True

def registrar_bicicleta(lista_columna):
    conexion.execute('''INSERT INTO bicicletas (marca, modelo, rodado, precio, cantidad) VALUES (?,?,?,?,?)''', lista_columna)
    conexion.commit()
    precio = float(lista_columna[3])
    cantidad = int(lista_columna[4])
    monto = precio * cantidad
    registrar_transaccion("compra", monto)
    return True

def buscar_bicicleta(marca, modelo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM bicicletas WHERE marca = ? AND modelo = ?''', (marca, modelo,))
    bicicleta = cursor.fetchone()
    if not bicicleta:
        return None
    return bicicleta

def buscar_accesorio(nombre):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT * FROM accesorios WHERE nombre = ?''', (nombre,))
    accesorio = cursor.fetchone()
    if not accesorio:
        return None
    return accesorio

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
    if cantidad == 0:
        return False
    
    precio = precio_bicicleta(marca, modelo)
    if precio is None:
        return False
    precio = precio
    cantidad_actual = cantidad_bicicleta(marca, modelo)
    cantidad_nueva = cantidad + cantidad_actual
    if cantidad_nueva < 0:
        print("Error: La cantidad no puede ser negativa.")
        return False
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE bicicletas SET cantidad = ? WHERE marca = ? AND modelo = ?''', (cantidad_nueva, marca, modelo))
    if cursor.rowcount == 0:
        return False
    if cantidad < 0:
        monto = precio * (-1*cantidad) #TRAEMOS A POSITIVO LA CANTIDAD PARA CALCULAR EL MONTO
        registrar_transaccion("venta", monto)
    else:
        monto = precio * cantidad
        registrar_transaccion("compra", (monto))
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
    if cantidad == 0:
        return False
    
    cantidad_actual = buscar_accesorio_cantidad(nombre)
    cantidad_nueva = cantidad + cantidad_actual
    precio = buscar_accesorio_precio(nombre)
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE accesorios SET cantidad = ? WHERE nombre = ?''', (cantidad_nueva, nombre))
    if cursor.rowcount == 0:
        return False
    if cantidad < 0:
        monto = precio * (-1*cantidad) #TRAEMOS A POSITIVO LA CANTIDAD PARA CALCULAR EL MONTO
        registrar_transaccion("venta", monto)
    else:
        monto = precio * cantidad
        registrar_transaccion("compra", (monto)) #RESTAMOS CADA VEZ QUE COMPRAOMOS PRODUCTOS
    conexion.commit()
    return True

def registrar_accesorio(lista_columna):
    conexion.execute('''INSERT INTO accesorios (nombre, cantidad, precio) VALUES (?,?,?)''', lista_columna)
    conexion.commit()
    precio = float(lista_columna[2])
    cantidad = int(lista_columna[1])
    monto = precio * cantidad
    registrar_transaccion("compra", monto)
    return True

def eliminar_producto_accesorio_bd(nombre):
    conexion.execute('''DELETE FROM accesorios WHERE nombre = ?''', (nombre,))
    conexion.commit()
    return mostrar_tabla("accesorios")


def eliminar_producto_bicicleta_bd(marca, modelo):
    conexion.execute('''DELETE FROM bicicletas WHERE marca = ? AND modelo = ?''', (marca, modelo))
    conexion.commit()
    return mostrar_tabla("bicicletas")

#FUNCIONES DE TRANSACIONES

def registrar_transaccion(tipo_operacion, monto):
    if tipo_operacion == "compra":
        monto = (-1 * monto)
    fecha = date.today() #registra la fecha de la transacion
    conexion.execute('''INSERT INTO transacciones (fecha, tipo_operacion, monto) VALUES (?,?,?)''', (fecha, tipo_operacion, monto))
    conexion.commit()

def exportar_csv(nombre_archivo):
    columnas = columnas_tabla(nombre_archivo)
    fila = contenido_tabla(nombre_archivo)
    fecha = datetime.now().strftime("%d-%H-%M-%S")
    with open(f'{nombre_archivo}_{fecha}.csv', 'w',newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(columnas)  
        writer.writerows(fila)    
    print(f"Datos exportados a {nombre_archivo}_{fecha}.csv correctamente.")
    

    
def registrar(nombre_tabla, valores):
    columnas = columnas_tabla(nombre_tabla)
    parametros = ", ".join(["?"] * len(valores))
    conexion.execute(f'''INSERT INTO {nombre_tabla} ({columnas}) VALUES ({parametros})''', valores)
    conexion.commit()
    return True