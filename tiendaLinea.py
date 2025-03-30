nombreProductos =[]
precios= []
stocks= []
ventasRealizadas=0

def resgitrarProducto():
    """Funcion para registrar un producto en la tienda The'Joel Online"""
    nombreProducto= input("Ingrese el nombre del producto: ")
    precio =  float(input("Ingrese el precio del prodcuto: "))
    stock =int(input("Ingrese la cantidad en stock:: "))

    nombreProductos.append(nombreProducto)
    precios.append(precio)
    stocks.append(stock)

    print(f"✅​ Producto '{nombreProducto}' Agregado con exito!!!")

def mostrarProducto():
    """Funcion para mostrar los productos en la tienda The'Joel Online"""
    print("\n 📦 Productos Disponibles​")
    if len(nombreProductos)==0:
        print(" ⚠️​ No hay productos registrados.")
    else:
        for i in range(len(nombreProductos)):
            print(f"{i+1}. {nombreProductos[i]}- Precio: ${precios[i]}- Stock: {stocks[i]} unidades")

def venderProducto():
    """Funcion para vender los productos en la tienda The'Joel Online"""
    global ventasRealizadas
    mostrarProducto()
    if len(nombreProductos)==0:
        print("⚠️​ No hay productos para vender.")
        return
    nombreVender = input("Ingrese el nombre del producto que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad que desea comparar: "))

    for i in range(len(nombreProductos)):
        if nombreVender.lower() == nombreProductos[i].lower():
            if stocks[i] >= cantidad:
                stocks[i] -= cantidad
                totalVentas = cantidad*precios[i]
                ventasRealizadas+=totalVentas
                print(f"✅​ Venta realizada con Exito. Total a pagar: ${totalVentas}")
            else:
                print("​❌​ No hay suficiente Stock Disponible ")
                return
    print("​❌​ Producto no encontrado.")      

def mostrarVentas():
        """Funcion para mostrar el total de ventas realizadas en la tienda The'Joel Online"""    
        print(f"\n ​💰​ Total de ventas realizadas ​💵​$ {ventasRealizadas}")

while True:
    print ("\n ​📌​ Menu de The JOEl de Online: ")
    print ("1. Regisrar productos")
    print ("2. Mostrar productos")
    print ("3. Vender productos")
    print ("4. Mostrar total de ventas")
    print ("5. Salir")
    opcion = int(input("Selecione la opcion a realizar: "))

    if opcion ==1:
        resgitrarProducto()
    elif opcion ==2:
        mostrarProducto()
    elif opcion ==3:
        venderProducto()
    elif opcion ==4:
        mostrarVentas()
    elif opcion ==5:
        print("​🥰​ Gracias por visitar nuestra tienda!!")
        break
    else:
        print("​❌​ Opcion no valida, intente nuevamente.")

