# Formularios/listar_productos.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_listar_productos():
    ventana_listar = tk.Toplevel()
    ventana_listar.title("NicaStock Solutions - Listar Productos")
    ventana_listar.geometry("450x400")
    ventana_listar.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_listar, text="Inventario de Productos", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Área de texto con Scroll para mostrar los productos
    frame_texto = tk.Frame(ventana_listar)
    frame_texto.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    caja_texto = tk.Text(frame_texto, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Arial", 10))
    caja_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=caja_texto.yview)

    # Función para cargar los datos del archivo de texto
    def cargar_datos():
        caja_texto.delete("1.0", tk.END) # Limpiar por si acaso
        
        if os.path.exists("Datos/productos.txt"):
            with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido.strip() == "":
                    caja_texto.insert(tk.END, "No hay productos registrados todavía.")
                else:
                    caja_texto.insert(tk.END, contenido)
        else:
            caja_texto.insert(tk.END, "Aún no se ha creado el archivo de productos (registre uno primero).")
        
        # Bloquear edición manual en la caja de texto
        caja_texto.config(state=tk.DISABLED)

    cargar_datos()

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_listar,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 10),
        width=15,
        command=ventana_listar.destroy
    )
    btn_regresar.pack(pady=15)