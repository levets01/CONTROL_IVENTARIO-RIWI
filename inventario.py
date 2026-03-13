print ("SISTEMA DE CONTROL DE INVENTARIO ")
nombre = input("Ingrese el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")


while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero para la cantidad.")


costo_total = precio * cantidad

print("\n--- Resultado ---")
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", costo_total)

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
