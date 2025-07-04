from funciones.sql_funciones import *


atributo_bicicleta = {"rodado": "Rodado",
                      "precio": "Precio",
                      "cantidad": "Cantidad"}
print("#dios te quiere ")
    
def producto_bicicleta():
    lista_de_salida = []
    marca = input("Ingrese la marca de la bicicleta: ").strip()
    modelo = input("Ingrese el modelo de la bicicleta: ").strip()
    if buscar_bicicleta(marca, modelo) is not None:
        print("La bicicleta ya existe en la base de datos.")
        cantidad = int(input("Ingrese la cantidad de bicicletas compradas: "))
        modificar_cantidad_bicicleta(marca, modelo, cantidad)
        return True
    
    for atributo in atributo_bicicleta: # realiza lo mimsmo que la funcion registrar_administrador pero con los atributos de bicicleta
        while True:
            try:
                dato = float(input(f"Ingrese su {atributo}: ").strip())
                if dato is None:
                    print("Error: Ingrese un numero.")
                    continue
                lista_de_salida.append(dato)
                break
            except ValueError:
                print("Error: Ingrese un caracter numerico.")
                continue
    lista_de_salida = [marca, modelo] + lista_de_salida
    registrar_bicicleta(lista_de_salida) # registra la bicicleta directamente en la base de datos
    return mostrar_tabla("bicicletas")

def producto_accesorio():
    try:
        nombre = input("Ingrese el nombre del accesorio: ").strip()
        if buscar_accesorio_cantidad(nombre) is not None:
            cantidad = int(input("Ingrese la cantidad de accesorios comprados: "))
            modificar_cantidad_accesorio(nombre, cantidad)
            print(f"La cantidad del accesorio {nombre} se registro en el stock.")
            return True
        print("El accesorio no figura en el catalogo de la tienda, de entrada al mismo.")
        cantidad = int(input("Ingrese la cantidad de accesorios comprados: "))
        precio = float(input("Ingrese el precio del accesorio: ").strip())

        if cantidad < 0 and precio < 0:
            print("Error: La cantidad y el precio deben ser mayores a 0.")
            return False
        lista_de_salida = [nombre, cantidad, precio]
        registrar_accesorio(lista_de_salida)
        return mostrar_tabla("accesorios")
    
    except ValueError:
        print("Error: solo se aceptan numeros")
        
def modificar_precio_bicicleta():
    marca = input("Ingrese la marca de la bicicleta: ").strip()
    modelo = input("Ingrese el modelo de la bicicleta: ").strip()
    if buscar_bicicleta(marca, modelo) is None:
        print("La bicicleta no existe en la base de datos.")
        return False
    precio = float(input(f"Ingrese el nuevo precio de {marca} {modelo} bicicleta: ").strip())
    
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE bicicletas SET precio = ? WHERE marca = ? AND modelo = ?''', (precio, marca, modelo))
    conexion.commit()
    print(f"El precio de la bicicleta {marca} {modelo} se actualizo correctamente.")
    return mostrar_tabla("bicicletas")
    
def modificar_precio_accesorio():
    nombre = input("Ingrese el nombre del accesorio: ").strip()
    if buscar_accesorio_cantidad(nombre) is None:
        print("El accesorio no existe en la base de datos.")
        return False
    precio = float(input("Ingrese el nuevo precio del accesorio: ").strip())
    
    cursor = conexion.cursor()
    cursor.execute(f'''UPDATE accesorios SET precio = ? WHERE nombre = ?''', (precio, nombre))
    conexion.commit()
    print(f"El precio del accesorio {nombre} se actualizo correctamente.")
    return mostrar_tabla("accesorios")

def eliminar_producto_bicicleta():
    marca = input("Ingrese la marca de la bicicleta: ").strip()
    modelo = input("Ingrese el modelo de la bicicleta: ").strip()
    if buscar_bicicleta(marca, modelo) is None:
        print("La bicicleta no existe en la base de datos.")
        return False
    eliminar_producto_bicicleta_bd(marca, modelo)
    return mostrar_tabla("bicicletas")

def eliminar_producto_accesorio():
    nombre = input("Ingrese el nombre del accesorio: ").strip()
    if buscar_accesorio(nombre) is None:
        print(f"No existe el accesorio {nombre} en el catalogo.")
        return False
    eliminar_producto_accesorio_bd(nombre)
    return mostrar_tabla("accesorios")

def comprar_bicicleta():
    marca = input("Ingrese la marca de la bicicleta: ").strip()
    modelo = input("Ingrese el modelo de la bicicleta: ").strip()
    if buscar_bicicleta(marca, modelo) is None:
        print(f"No existe la bicicleta {marca} {modelo} en el catalogo.")
        return False
    cantidad = -1 * int(input(f"Ingrese la cantidad de bicicletas {marca} {modelo} compradas: ")) # se ingresa la cantidad como negativa
    resultado = modificar_cantidad_bicicleta(marca, modelo, cantidad)
    if resultado is False:
        return print("Error con uno de los parametros, precio o cantidad.")
    return mostrar_tabla("bicicletas")

def comprar_accesorio():
    nombre = input("Ingrese el nombre del accesorio: ").strip()
    if buscar_accesorio(nombre) is None:
        print(f"No existe el accesorio {nombre} en el catalogo.")
        return False
    cantidad = -1 * int(input(f"Ingrese la cantidad de {nombre} comprados: ")) # se ingresa la cantidad como negativa
    resultado = modificar_cantidad_accesorio(nombre, cantidad)
    if resultado is False:
        return print("El error se debe a uno de los parametros, precio o cantidad.")
    return mostrar_tabla("accesorios")