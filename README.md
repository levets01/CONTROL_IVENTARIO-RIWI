#  Sistema de Control de Inventario en Python

Este es un programa sencillo desarrollado en **Python** que permite registrar un producto, su precio y la cantidad disponible para calcular el **costo total del inventario ingresado**.

El sistema incluye **validación de datos**, lo que evita errores si el usuario ingresa información incorrecta.

---

## ¿Qué hace este programa?

El programa permite:

* Registrar el **nombre de un producto**
* Registrar el **precio del producto**
* Registrar la **cantidad disponible**
* Calcular automáticamente el **costo total**
* Mostrar los resultados de forma clara en pantalla
* Evitar errores cuando se ingresan datos incorrectos

---

##  ¿Cómo usar el programa?

Sigue estos pasos:

1. Ejecuta el programa en **Python**.
2. El sistema te pedirá el **nombre del producto**.
3. Luego te pedirá el **precio del producto**.
4. Después deberás ingresar la **cantidad disponible**.
5. Finalmente el sistema calculará el **costo total** y mostrará el resultado en pantalla.

---

##  Validaciones del sistema

El programa incluye varias validaciones para evitar errores:

* El **nombre del producto** no puede estar vacío.
* El nombre solo puede contener **letras**.
* El **precio** debe ser un número válido.
* El precio **no puede ser negativo**.
* La **cantidad** debe ser un número entero.
* La cantidad **no puede ser negativa**.

Si se ingresa un dato incorrecto, el sistema mostrará un **mensaje de error** y volverá a pedir el dato.

---

## 💻 Requisitos

Para ejecutar este programa necesitas tener instalado:

* **Python 3**

---

## ▶️ Cómo ejecutar el programa

1. Descarga el archivo `.py`
2. Abre una **terminal o consola**.
3. Ejecuta el siguiente comando:

```bash
python3 inventario.py

```
## si no tienes python3 instalado usa

```bash
apt install python3
```
## Si te pide persmisos elevados usa 

```bash
sudo apt install python3
```


---

## 🧾 Ejemplo de uso

```
Ingrese el nombre del producto: Arroz
Ingrese el precio del producto: 2.5
Ingrese la cantidad del producto: 10

--- Resultado ---
Producto: Arroz | Precio: 2.5 | Cantidad: 10 | Total: 25.0
```

---

## 🛠️ Tecnologías utilizadas

* Python 3


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



```




## Creado por Stevel iglesias 🐍

