# 📦 Sistema de Control de Inventario en Python

Este es un programa básico desarrollado en **Python** que permite registrar un producto, su precio y la cantidad disponible para calcular el **costo total del inventario ingresado**.

El sistema incluye **validación de datos**, evitando que el programa se rompa si el usuario ingresa valores incorrectos.

---

## 🚀 Características

- Registro del **nombre del producto**
- Registro del **precio del producto**
- Registro de la **cantidad disponible**
- Validación para evitar errores de entrada
- Cálculo automático del **costo total**
- Presentación clara de los resultados
- El sistama no permite valores negativos
- No permite textos en el input de valor numerico e viseversa

---

## 🛠️ Tecnologías utilizadas

- **Python 3**

---

## 📋 Funcionamiento del programa

1. El sistema solicita el **nombre del producto**.
2. Luego pide el **precio del producto**.
3. Si el usuario ingresa letras u otro valor inválido, el sistema muestra un **mensaje de error** y vuelve a pedir el dato.
4. Después solicita la **cantidad del producto**.
5. Se calcula el **costo total** multiplicando el precio por la cantidad.
6. Finalmente se muestran los resultados en pantalla.

---

## 💻 Código del programa

```python
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

