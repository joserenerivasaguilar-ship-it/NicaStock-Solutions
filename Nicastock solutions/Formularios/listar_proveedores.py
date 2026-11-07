# Formularios/listar_proveedores.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_listar_proveedores():
    ventana_listar_prov = tk.Toplevel()
    ventana_listar_prov.title("NicaStock Solutions - Listar Proveedores")
    ventana_listar_prov.geometry("450x400")
    ventana_listar_prov.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_listar_prov, text="Lista de Proveedores", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Área de texto con Scroll para mostrar los proveedores
    frame_texto = tk.Frame(ventana_listar_prov)
    frame_texto.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    caja_texto = tk.Text(frame_texto, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Arial", 10))
    caja_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=caja_texto.yview)

    # Función para cargar los datos del archivo de texto
    def cargar_datos():
        caja_texto.delete("1.0", tk.END)
        
        if os.path.exists("Datos/proveedores.txt"):
            with open("Datos/proveedores.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido.strip() == "":
                    caja_texto.insert(tk.END, "No hay proveedores registrados todavía.")
                else:
                    caja_texto.insert(tk.END, contenido)
        else:
            caja_texto.insert(tk.END, "Aún no se ha creado el archivo de proveedores (registre uno primero).")
        
        caja_texto.config(state=tk.DISABLED)

    cargar_datos()

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_listar_prov,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 10),
        width=15,
        command=ventana_listar_prov.destroy
    )
    btn_regresar.pack(pady=15)