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
        
         print("\033[31mError : El nombre no puede estar vacio\033[0m")
    
    elif not nombre.isalpha():
        
        print("\033[31mError: El nombre solo debe tener letras\033[0m")
           
    else :
        
        break
#aca esta la condicion para ingresar los productos y hacer las demas operaciones 
while True:
    
    try:
        precio = float(input("Ingrese el precio del producto: "))
        
        if precio < 0:
            
            print("\033[31mError: El precio no puede ser negativo.\033[0m")
            
            continue
        break
    except ValueError:
        print("\033[31mError: Debe ingresar un número válido para el precio.\033[0m")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        if cantidad < 0:
            
            print("\033[31mError: La cantidad no puede ser negativa.\033[0m")
            
            continue
        
        break
    except ValueError:
        print("\033[31mError: Debe ingresar un número entero para la cantidad.\033[0m")

costo_total = precio * cantidad
# aca de muestra estilo factura
print("\n--- Resultado ---")
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", costo_total)

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

