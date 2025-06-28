dni = 39229474
print("")

while True: 
    print ("1- Loguearse \n2- Registrarse \n0- Salir ")
    opcion = input("Elija la opcion ")
     
    match opcion:
        case "1":
            dni = input("escribir dni ").strip()
            if not dni:
                print("Usuariuo no Registrado")
        
        case "2":
            dni = input("escribir dni: ").strip()
            if not dni:
                print("se debe proporcionar un dni valido")
                continue

            nombre = input("escribe el nombre: ").strip() 
            if not nombre:
                print("se debe proporcionar un nombre valido")
                continue

            apellido = input("escribe apellido: ").strip()
            if not apellido:
                print("se debe proporcionar un apellido valido")
                continue

            email = input ("escribe email: ").strip()
            if not email:
                print("se debe proporcionar email valido")
                continue
     
        case "0":
            #conexion.close()
            print("saliendo. . . ")
            break
        case _:
            print("elige una opcion correcta")
