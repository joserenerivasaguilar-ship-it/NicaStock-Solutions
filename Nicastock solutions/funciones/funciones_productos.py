# funciones/funciones_productos.py
import os

def guardar_producto_txt(nombre, cantidad, precio):
    if not os.path.exists("Datos"):
        os.makedirs("Datos")
    
    with open("Datos/productos.txt", "r", encoding="utf-8") if os.path.exists("Datos/productos.txt") else open("Datos/productos.txt", "w", encoding="utf-8") as archivo:
        pass # Solo asegura que exista

    with open("Datos/productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Producto: {nombre} | Cantidad: {cantidad} | Precio: ${precio}\n")

def leer_productos_txt():
    if os.path.exists("Datos/productos.txt"):
        with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
            return archivo.read()
    return ""

def buscar_producto_txt(termino):
    encontrados = []
    if os.path.exists("Datos/productos.txt"):
        with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if termino in linea.lower():
                    encontrados.append(linea)
    return encontrados

def contar_productos_txt():
    if os.path.exists("Datos/productos.txt"):
        with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
            lineas = [linea for linea in archivo if linea.strip()]
            return len(lineas)
    return 0