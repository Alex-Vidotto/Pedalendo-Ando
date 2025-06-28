import re
from funciones_db import *


def menu_bienvenida():
    print("1. Ingresar usuario")
    print("2. Registrarse")
    print("3. Salir")
    
def menu_principal():
    print("1. Igresar un nuevo producto")
    print("2. Igresar un nuevo accesorio")
    print("3. Modificar precio del service")
    print("4. Modificar el precio del producto")
    print("5. Modificar el precio del accesorio")
    print("6. Salir")

atributo_usuario = {"nombre": "Nombre",
                   "apellido": "Apellido",
                   "correo": "Correo",
                   "telefono": "Telefono"}

atributo_bicicleta = {"rodado": "Rodado",
                      "precio": "Precio",
                      "cantidad": "Cantidad"}

    
def registrar_administrador():
    for atributo in atributo_usuario:
        while True:
            dato = input(f"Ingrese su {atributo_usuario[atributo]}: ").strip()
            dato = dato.lower()  # dato a minúsculas
            if dato == "": # controla que no este vacio el dato ingresado
                print("error: el campo no puede estar vacio")
                continue

            if atributo == "correo":
                patron_correo = r"^[a-z0-9]+@[a-z0-9]+.com$" # El correo tiene que ser ejemplo123@dominio.com
                if not re.match(patron_correo, dato):
                    print("formato de correo incorrecto: ejemplo123@dominio.com")
                    continue
            break
        atributo_usuario[atributo] = dato # remplaza los valores por los datos ingresados
    return list(atributo_usuario.values()) # devuelve los nuevos valores del diccionario en un formato lista
                               
                
                
def solicitad_datos_bicicleta(marca, modelo):
    lista_de_salida = []
    for atributo in atributo_bicicleta: # realiza lo mimsmo que la funcion registrar_administrador pero con los atributos de bicicleta
        while True:
            try:
                dato = int(input(f"Ingrese su {atributo}: ").strip())
                if atributo == None:
                    print("Error: Ingrese un valor numérico válido.")
                    continue
                lista_de_salida.append(dato)
                break
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
    lista_de_salida = [marca, modelo] + lista_de_salida
    registrar_bicicleta(lista_de_salida) # registra la bicicleta directamente en la base de datos
    
    
    
    




def solicitud_atributos_registro(lista_atributos):
    for indice, atributo in enumerate(lista_atributos):
        cada_atributo = input(f"Ingrese su {atributo}: ").lower()
        lista_atributos[indice] = cada_atributo
    return lista_atributos
