productos = {
    "manzana": 2.99,
    "pera": 3, 
    "uvas": 1
}

producto_pedido = input("Escribe el nombre de un producto: ").lower()

if producto_pedido in productos:
    print("Su precio es: ", productos[producto_pedido])
else:
    print("El producto no esta en la lista")
