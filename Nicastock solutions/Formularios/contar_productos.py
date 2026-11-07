# Formularios/contar_productos.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_contar_productos():
    ventana_contar = tk.Toplevel()
    ventana_contar.title("NicaStock Solutions - Contar Productos")
    ventana_contar.geometry("350x300")
    ventana_contar.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_contar, text="Total de Productos", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=20)

    # Etiqueta para mostrar el número total
    lbl_contador_titulo = tk.Label(ventana_contar, text="Cantidad total en inventario:", bg="#f0f0f0", font=("Arial", 11))
    lbl_contador_titulo.pack(pady=5)

    lbl_resultado = tk.Label(ventana_contar, text="0", bg="#f0f0f0", font=("Arial", 30, "bold"), fg="#2196F3")
    lbl_resultado.pack(pady=10)

    # Función para contar las líneas del archivo
    def calcular_total():
        if os.path.exists("Datos/productos.txt"):
            with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
                # Contamos cuántas líneas tienen texto válido
                lineas = [linea for linea in archivo if linea.strip()]
                total = len(lineas)
                lbl_resultado.config(text=str(total))
        else:
            lbl_resultado.config(text="0")

    calcular_total()

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_contar,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_contar.destroy
    )
    btn_regresar.pack(pady=20)