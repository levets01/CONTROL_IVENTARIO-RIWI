print(" ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗         ██████╗ ███████╗    ██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ █████╗ ██████╗ ██╗ ██████╗  ")  
print("██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║         ██╔══██╗██╔════╝    ██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔═══██╗  ")  
print("██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║         ██║  ██║█████╗      ██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ███████║██████╔╝██║██║   ██║  ")  
print("██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║         ██║  ██║██╔══╝      ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██╔══██╗██║██║   ██║  ")  
print(" ██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗    ██████╔╝███████╗    ██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║██║╚██████╔╝  ")  
print("╚ ═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝   ")  

# aca esta la condicion para que no se permita numeros negrativos ni letras en los input de valor numericos e valores de textos input de textos 
while True:
    
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    if not nombre:
        
        print("Error : El nombre no puede estar vacio")
    
    elif not nombre.isalpha():
        
        print("Error: El nombre solo debe tener letras")
           
    else :
        
        break
#aca esta la condicion para ingresar los productos y hacer las demas operaciones 
while True:
    
    try:
        precio = float(input("Ingrese el precio del producto: "))
        
        if precio < 0:
            
            print("Error: El precio no puede ser negativo.")
            
            continue
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        if cantidad < 0:
            
            print("Error: La cantidad no puede ser negativa.")
            
            continue
        
        break
    except ValueError:
        print("Error: Debe ingresar un número entero para la cantidad.")

costo_total = precio * cantidad
# aca de muestra estilo factura
print("\n--- Resultado ---")
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", costo_total)

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

