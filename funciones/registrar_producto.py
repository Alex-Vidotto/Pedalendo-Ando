from funciones.sql_funciones import *


atributo_bicicleta = {"rodado": "Rodado",
                      "precio": "Precio",
                      "cantidad": "Cantidad"}
    
def producto_bicicleta():
    lista_de_salida = []
    marca = input("Ingrese la marca de la bicicleta: ").strip()
    modelo = input("Ingrese el modelo de la bicicleta: ").strip()
    if buscar_bicicleta(marca, modelo) is not None:
        print("La bicicleta ya existe en la base de datos.")
        cantidad = int(input("Ingrese la cantidad de bicicletas compradas: "))
        precio = buscar_atributo_bicicleta(marca, modelo, "precio")
        confirmacion = input(f"Confirmar compra de {cantidad} bicicleta {marca} {modelo}, valiendo cada una ${precio}. [Y/N]: ").lower()
        if confirmacion == "n":
            return print("Operacion cancelada, volviendo al menu..")
        monto =modificar_cantidad_bicicleta(marca, modelo, cantidad)
        return print(f"La cantidad de bicicletas {marca} {modelo} se registro en el stock, total pagado: ${monto} en pesos.")
    
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
    cantidad = int(lista_de_salida[2])
    monto = int(lista_de_salida[1])
    lista_de_salida = [marca, modelo] + lista_de_salida
    marca_modelo = f"{marca} {modelo}"
    registrar("bicicletas",lista_de_salida) # registra la bicicleta directamente en la base de datos
    registrar_transaccion("compra", "bicicleta", marca_modelo, cantidad, monto)
    return print(f"Pago por la bicicleta {marca} {modelo}, pagando un total de ${float(lista_de_salida[2]) * float(lista_de_salida[3])} en pesos.")

def producto_accesorio():
    try:
        nombre = input("Ingrese el nombre del accesorio: ").strip()
        if buscar_atributo_accesorio(nombre, "cantidad") is not None:
            cantidad = int(input("Ingrese la cantidad de accesorios comprados: "))
            precio = buscar_atributo_accesorio(nombre, "precio")
            confirmacion = input(f"Confirmar compra de {cantidad} accesorio {nombre}, valiendo cada una ${precio}. [Y/N]: ").lower()
            if confirmacion == "n":
                return print("Operacion cancelada, volviendo al menu..")
            monto =modificar_cantidad_accesorio(nombre, cantidad)
            return print(f"La cantidad de accesorios {nombre} se registro en el stock, total pagado: ${monto} en pesos.")
        print("El accesorio no figura en el catalogo de la tienda, de entrada al mismo.")
        cantidad = int(input("Ingrese la cantidad de accesorios comprados: "))
        precio = float(input("Ingrese el precio del accesorio: ").strip())

        if cantidad < 0 and precio < 0:
            print("Error: La cantidad y el precio deben ser mayores a 0.")
            return False
        
        monto = precio * cantidad
        registrar_transaccion("compra", "accesorio", nombre, cantidad, monto)
        lista_de_salida = [nombre, cantidad, precio]
        registrar("accesorios",lista_de_salida)
        return print(f"Pago por el accesorio {nombre}, pagando un total de ${float(lista_de_salida[1]) * float(lista_de_salida[2])} en pesos.")
    
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
    if buscar_atributo_accesorio(nombre, "cantidad") is None:
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
    precio = buscar_atributo_bicicleta(marca, modelo, "precio")
    confirmacion = input(f"Confirma la compra de la bicicleta {marca} {modelo}, valiendo cada una ${precio} [Y/N]: ").lower()
    if confirmacion == "n":
        return print("Operacion cancelada, volviendo al menu.")
    resultado = modificar_cantidad_bicicleta(marca, modelo, cantidad)
    if resultado is False:
        return print("Error con uno de los parametros, precio o cantidad.")
    return print(f"Gracias por comprar la marca {marca} modelo {modelo}, total pagado: ${resultado} en pesos.")

def comprar_accesorio():
    nombre = input("Ingrese el nombre del accesorio: ").strip()
    if buscar_accesorio(nombre) is None:
        print(f"No existe el accesorio {nombre} en el catalogo.")
        return False
    cantidad = -1 * int(input(f"Ingrese la cantidad de {nombre} comprados: ")) # se ingresa la cantidad como negativa
    precio = buscar_atributo_accesorio(nombre, "precio")
    confirmacion = input(f"Confirma la compra de {nombre}, valiendo cada uno ${precio} [Y/N]: ").lower()
    if confirmacion == "n":
        return print("Operacion cancelada, volviendo al menu.")
        
    resultado = modificar_cantidad_accesorio(nombre, cantidad)
    if resultado is False:
        return print("El error se debe a uno de los parametros, precio o cantidad.")
    return print(f"Gracias por comprar el accesorio {nombre}, total pagado: ${resultado} en pesos.")