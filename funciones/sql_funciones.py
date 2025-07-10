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
        producto TEXT NOT NULL,
        marca_modelo TEXT NOT NULL,
        cantidad TEXT NOT NULL,
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

def buscar_atributo_bicicleta(marca, modelo, atributo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT {atributo} FROM bicicletas WHERE marca = ? AND modelo = ?''', (marca, modelo,))
    resultado = cursor.fetchone()
    if not resultado:
        return None
    return resultado[0]

   
def modificar_cantidad_bicicleta(marca, modelo, cantidad):
    marca_modelo = (f"{marca} {modelo}")
    if cantidad == 0:
        return False
    
    precio = buscar_atributo_bicicleta(marca, modelo, "precio")
    if precio is None:
        return False
    precio = precio
    cantidad_actual = buscar_atributo_bicicleta(marca, modelo, "cantidad")
    cantidad_nueva = cantidad + cantidad_actual
    if cantidad_nueva < 0:
        print("Error: La cantidad no puede ser negativa.")
        return False
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE bicicletas SET cantidad = ? WHERE marca = ? AND modelo = ?''', (cantidad_nueva, marca, modelo))
    if cursor.rowcount == 0:
        return False
    if cantidad < 0:
        cantidad = -1 * (cantidad)
        monto = precio * (cantidad) #TRAEMOS A POSITIVO LA CANTIDAD PARA CALCULAR EL MONTO
        registrar_transaccion("venta", "bicicleta", marca_modelo, cantidad, monto)
    else:
        monto = precio * cantidad
        registrar_transaccion("compra","bicicleta", marca_modelo, cantidad, (monto))
    conexion.commit()
    return monto

def buscar_atributo_accesorio(nombre, atributo):
    cursor = conexion.cursor()
    cursor.execute(f'''SELECT {atributo} FROM accesorios WHERE nombre = ?''', (nombre,))
    resultado = cursor.fetchone()
    if not resultado:
        return None
    return resultado[0]


def modificar_cantidad_accesorio(nombre, cantidad):
    if cantidad == 0:
        return False
    
    cantidad_actual = buscar_atributo_accesorio(nombre, "cantidad")
    cantidad_nueva = cantidad + cantidad_actual
    precio = buscar_atributo_accesorio(nombre, "precio")
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE accesorios SET cantidad = ? WHERE nombre = ?''', (cantidad_nueva, nombre))
    if cursor.rowcount == 0:
        return False
    if cantidad < 0:
        cantidad = -1 * cantidad
        monto = precio * (cantidad) #TRAEMOS A POSITIVO LA CANTIDAD PARA CALCULAR EL MONTO
        registrar_transaccion("venta", "accesorios", nombre, cantidad, monto)
    else:
        monto = precio * cantidad
        registrar_transaccion("compra", "accesorios", nombre, cantidad, (monto)) #RESTAMOS CADA VEZ QUE COMPRAOMOS PRODUCTOS
    conexion.commit()
    return monto


def eliminar_producto_accesorio_bd(nombre):
    conexion.execute('''DELETE FROM accesorios WHERE nombre = ?''', (nombre,))
    conexion.commit()
    return mostrar_tabla("accesorios")


def eliminar_producto_bicicleta_bd(marca, modelo):
    conexion.execute('''DELETE FROM bicicletas WHERE marca = ? AND modelo = ?''', (marca, modelo))
    conexion.commit()
    return mostrar_tabla("bicicletas")

#FUNCIONES DE TRANSACIONES

def registrar_transaccion(tipo_operacion, producto, marca_modelo, cantidad, monto):
    if tipo_operacion == "compra":
        monto = (-1 * monto)
    fecha = date.today() #registra la fecha de la transacion
    conexion.execute('''INSERT INTO transacciones (fecha, tipo_operacion, producto, marca_modelo, cantidad, monto) VALUES (?,?,?,?,?,?)''', (fecha, tipo_operacion, producto, marca_modelo, cantidad, monto))
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
    if columnas[0] == "id":
        columnas = columnas[1:]
    columnas = ", ".join(columnas)
    parametros = ", ".join(["?"] * len(valores))
    conexion.execute(f'''INSERT INTO {nombre_tabla} ({columnas}) VALUES ({parametros})''', valores)
    conexion.commit()
    return True