import os
import time

# Base de datos de bicicletas
catalogo_bicicletas = {
    1: {"modelo": "Mountain Pro X1", "tipo": "Montaña", "rodado": "29\"", "precio": 85000},
    2: {"modelo": "Urban City 2024", "tipo": "Urbana", "rodado": "26\"", "precio": 45000},
    3: {"modelo": "Speed Racer", "tipo": "Ruta", "rodado": "28\"", "precio": 120000},
    4: {"modelo": "Kids Adventure", "tipo": "Infantil", "rodado": "20\"", "precio": 35000},
    5: {"modelo": "Electric Boost", "tipo": "Eléctrica", "rodado": "27.5\"", "precio": 180000},
    6: {"modelo": "BMX Freestyle", "tipo": "BMX", "rodado": "20\"", "precio": 55000},
    7: {"modelo": "Comfort Cruise", "tipo": "Paseo", "rodado": "26\"", "precio": 38000},
    8: {"modelo": "Trail Master", "tipo": "Montaña", "rodado": "27.5\"", "precio": 95000}
}

# Base de datos de accesorios y repuestos
catalogo_accesorios = {
    1: {"producto": "Casco de Seguridad", "categoria": "Protección", "precio": 8500},
    2: {"producto": "Luces LED Delanteras", "categoria": "Iluminación", "precio": 3200},
    3: {"producto": "Candado de Seguridad", "categoria": "Seguridad", "precio": 4800},
    4: {"producto": "Bomba de Aire", "categoria": "Herramientas", "precio": 2500},
    5: {"producto": "Kit de Reparación", "categoria": "Herramientas", "precio": 1800},
    6: {"producto": "Cubiertas MTB 29\"", "categoria": "Repuestos", "precio": 5200},
    7: {"producto": "Cámara de Aire", "categoria": "Repuestos", "precio": 800},
    8: {"producto": "Cadena Shimano", "categoria": "Repuestos", "precio": 6500},
    9: {"producto": "Asiento Deportivo", "categoria": "Confort", "precio": 7200},
    10: {"producto": "Guantes Ciclismo", "categoria": "Protección", "precio": 2800},
    11: {"producto": "Botella de Agua", "categoria": "Accesorios", "precio": 1200},
    12: {"producto": "Soporte para Celular", "categoria": "Accesorios", "precio": 3500}
}

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_logo():
    """Muestra el logo de la tienda"""
    print("="*60)
    print("" + " "*15 + "PedaleAndo-Ando" + " "*15 + "")
    print("="*60)

def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    limpiar_pantalla()
    mostrar_logo()
    print("\n MENÚ PRINCIPAL:")
    print("1  Comprar Bicicletas")
    print("2  Comprar Accesorios y Repuestos")
    print("3  Solicitar Servicio y Mantenimiento")
    print("4  Salir")
    print("-" * 60)

def mostrar_catalogo_bicicletas():
    """Muestra el catálogo completo de bicicletas"""
    limpiar_pantalla()
    mostrar_logo()
    print("\n CATÁLOGO DE BICICLETAS:")
    print("-" * 60)
    print(f"{'ID':<3} {'MODELO':<20} {'TIPO':<12} {'RODADO':<8} {'PRECIO':<10}")
    print("-" * 60)
    
    for id_bici, datos in catalogo_bicicletas.items():
        precio_formato = f"${datos['precio']:,}"
        print(f"{id_bici:<3} {datos['modelo']:<20} {datos['tipo']:<12} {datos['rodado']:<8} {precio_formato:<10}")
    
    print("-" * 60)

def comprar_bicicleta():
    """Maneja la compra de bicicletas"""
    while True:
        mostrar_catalogo_bicicletas()
        print("\n COMPRAR BICICLETA:")
        
        try:
            seleccion = int(input("Ingresa el ID de la bicicleta que deseas comprar (0 para volver): "))
            
            if seleccion == 0:
                break
            elif seleccion in catalogo_bicicletas:
                bici = catalogo_bicicletas[seleccion]
                print(f"\n Has seleccionado:")
                print(f"   Modelo: {bici['modelo']}")
                print(f"   Tipo: {bici['tipo']}")
                print(f"   Rodado: {bici['rodado']}")
                print(f"   Precio: ${bici['precio']:,}")
                
                confirmar = input("\n¿Confirmas la compra? (s/n): ").lower()
                if confirmar == 's':
                    print(f"\n ¡Compra realizada exitosamente!")
                    print(f" Total a pagar: ${bici['precio']:,}")
                    print(" Tu bicicleta será preparada para entrega.")
                    input("\nPresiona Enter para continuar...")
                    break
                else:
                    print(" Compra cancelada.")
                    time.sleep(1)
            else:
                print(" ID no válido. Por favor selecciona un ID de la lista.")
                time.sleep(1)
                
        except ValueError:
            print(" Por favor ingresa un número válido.")
            time.sleep(1)

def mostrar_catalogo_accesorios():
    """Muestra el catálogo de accesorios y repuestos"""
    limpiar_pantalla()
    mostrar_logo()
    print("\n  CATÁLOGO DE ACCESORIOS Y REPUESTOS:")
    print("-" * 70)
    print(f"{'ID':<3} {'PRODUCTO':<25} {'CATEGORÍA':<15} {'PRECIO':<10}")
    print("-" * 70)
    
    for id_acc, datos in catalogo_accesorios.items():
        precio_formato = f"${datos['precio']:,}"
        print(f"{id_acc:<3} {datos['producto']:<25} {datos['categoria']:<15} {precio_formato:<10}")
    
    print("-" * 70)

def comprar_accesorio():
    """Maneja la compra de accesorios y repuestos"""
    carrito = []
    total = 0
    
    while True:
        mostrar_catalogo_accesorios()
        if carrito:
            print(f"\n Carrito actual: {len(carrito)} productos - Total: ${total:,}")
        
        print("\n COMPRAR ACCESORIOS:")
        print("Opciones: [ID del producto] | [0] Finalizar compra | [99] Volver al menú")
        
        try:
            seleccion = int(input("Tu selección: "))
            
            if seleccion == 99:
                break
            elif seleccion == 0:
                if carrito:
                    print(f"\n RESUMEN DE COMPRA:")
                    print("-" * 50)
                    for item in carrito:
                        print(f"• {item['producto']} - ${item['precio']:,}")
                    print("-" * 50)
                    print(f" TOTAL: ${total:,}")
                    
                    confirmar = input("\n¿Confirmas la compra? (s/n): ").lower()
                    if confirmar == 's':
                        print("\n🎉 ¡Compra realizada exitosamente!")
                        print(" Tus productos serán preparados para entrega.")
                        input("\nPresiona Enter para continuar...")
                        break
                    else:
                        print(" Compra cancelada.")
                        carrito.clear()
                        total = 0
                        time.sleep(1)
                else:
                    print(" Tu carrito está vacío.")
                    time.sleep(1)
                    
            elif seleccion in catalogo_accesorios:
                producto = catalogo_accesorios[seleccion]
                carrito.append(producto)
                total += producto['precio']
                print(f" {producto['producto']} agregado al carrito!")
                time.sleep(1)
            else:
                print(" ID no válido. Por favor selecciona un ID de la lista.")
                time.sleep(1)
                
        except ValueError:
            print(" Por favor ingresa un número válido.")
            time.sleep(1)

def solicitar_servicio():
    """Muestra información de contacto para servicio técnico"""
    limpiar_pantalla()
    mostrar_logo()
    print("\n SERVICIO Y MANTENIMIENTO")
    print("="*60)
    print("\n Contáctese con los siguientes números para")
    print("   solicitar servicio y mantenimiento:\n")
    
    print(" SERVICIO MÓVIL:")
    print("   Tel: (376) 4-345-678")
    print("   Tel: (376) 4-789-012")
    print("   Tel: (376) 4-123-456")
    print("   Lunes a Sábado: 9:00 - 17:00")
    print("   ¡Vamos hasta tu domicilio!\n")
    
    print("="*60)
    print(" Servicios disponibles:")
    print("   • Mantenimiento preventivo")
    print("   • Reparación de frenos")
    print("   • Cambio de cubiertas y cámaras")
    print("   • Ajuste de cambios")
    print("   • Lubricación completa")
    print("   • Revisión general")
    
    input("\n Presiona Enter para volver al menú principal...")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = int(input("\n Selecciona una opción (1-4): "))
            
            if opcion == 1:
                comprar_bicicleta()
            elif opcion == 2:
                comprar_accesorio()
            elif opcion == 3:
                solicitar_servicio()
            elif opcion == 4:
                limpiar_pantalla()
                mostrar_logo()
                print("\n ¡Gracias por visitarnos!")
                print(" ¡Vuelve pronto a Pedaleando-Ando! ")
                print("="*60)
                break
            else:
                print(" Opción no válida. Por favor selecciona del 1 al 4.")
                time.sleep(2)
                
        except ValueError:
            print(" Por favor ingresa un número válido.")
            time.sleep(2)
        except KeyboardInterrupt:
            print("\n\n ¡Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()