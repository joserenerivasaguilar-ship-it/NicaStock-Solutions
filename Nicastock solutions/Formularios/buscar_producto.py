# Formularios/buscar_producto.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_buscar_producto():
    ventana_buscar = tk.Toplevel()
    ventana_buscar.title("NicaStock Solutions - Buscar Producto")
    ventana_buscar.geometry("400x400")
    ventana_buscar.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_buscar, text="Buscar Producto", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Campo para escribir el nombre a buscar
    lbl_buscar = tk.Label(ventana_buscar, text="Ingrese el nombre del producto:", bg="#f0f0f0", font=("Arial", 10))
    lbl_buscar.pack()
    
    entry_buscar = tk.Entry(ventana_buscar, font=("Arial", 11), width=25)
    entry_buscar.pack(pady=5)

    # Área de resultados
    lbl_resultado = tk.Label(ventana_buscar, text="Resultado de la búsqueda:", bg="#f0f0f0", font=("Arial", 10, "bold"))
    lbl_resultado.pack(pady=10)

    caja_resultado = tk.Text(ventana_buscar, height=6, width=40, font=("Arial", 10))
    caja_resultado.pack(pady=5)
    caja_resultado.config(state=tk.DISABLED)

    # Función para realizar la búsqueda en el archivo de texto
    def realizar_busqueda():
        termino = entry_buscar.get().strip().lower()
        caja_resultado.config(state=tk.NORMAL)
        caja_resultado.delete("1.0", tk.END)

        if not termino:
            messagebox.showerror("Error", "Por favor ingrese un nombre para buscar")
            caja_resultado.config(state=tk.DISABLED)
            return

        if os.path.exists("Datos/productos.txt"):
            encontrados = []
            with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if termino in linea.lower():
                        encontrados.append(linea)

            if encontrados:
                caja_resultado.insert(tk.END, "".join(encontrados))
            else:
                caja_resultado.insert(tk.END, "No se encontró ningún producto con ese nombre.")
        else:
            caja_resultado.insert(tk.END, "No hay registros de productos todavía.")

        caja_resultado.config(state=tk.DISABLED)

    # Botón Buscar
    btn_buscar = tk.Button(
        ventana_buscar,
        text="Buscar",
        bg="#2196F3",
        fg="white",
        font=("Arial", 10, "bold"),
        width=15,
        command=realizar_busqueda
    )
    btn_buscar.pack(pady=10)

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_buscar,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_buscar.destroy
    )
    btn_regresar.pack()