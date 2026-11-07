# funciones/funciones_proveedores.py
import os

def guardar_proveedor_txt(nombre, telefono, direccion):
    if not os.path.exists("Datos"):
        os.makedirs("Datos")
    
    with open("Datos/proveedores.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Proveedor: {nombre} | Teléfono: {telefono} | Dirección: {direccion}\n")

def leer_proveedores_txt():
    if os.path.exists("Datos/proveedores.txt"):
        with open("Datos/proveedores.txt", "r", encoding="utf-8") as archivo:
            return archivo.read()
    return ""

def buscar_proveedor_txt(termino):
    encontrados = []
    if os.path.exists("Datos/proveedores.txt"):
        with open("Datos/proveedores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if termino in linea.lower():
                    encontrados.append(linea)
    return encontrados

def contar_proveedores_txt():
    if os.path.exists("Datos/proveedores.txt"):
        with open("Datos/proveedores.txt", "r", encoding="utf-8") as archivo:
            lineas = [linea for linea in archivo if linea.strip()]
            return len(lineas)
    return 0