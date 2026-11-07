# Formularios/registrar_proveedor.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_registrar_proveedor():
    ventana_registrar_prov = tk.Toplevel()
    ventana_registrar_prov.title("NicaStock Solutions - Registrar Proveedor")
    ventana_registrar_prov.geometry("350x420")
    ventana_registrar_prov.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_registrar_prov, text="Registrar Nuevo Proveedor", font=("Arial", 13, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Campo Nombre del Proveedor
    lbl_nombre = tk.Label(ventana_registrar_prov, text="Nombre del Proveedor:", bg="#f0f0f0", font=("Arial", 10))
    lbl_nombre.pack()
    entry_nombre = tk.Entry(ventana_registrar_prov, font=("Arial", 11), width=25)
    entry_nombre.pack(pady=5)

    # Campo Teléfono
    lbl_telefono = tk.Label(ventana_registrar_prov, text="Teléfono:", bg="#f0f0f0", font=("Arial", 10))
    lbl_telefono.pack()
    entry_telefono = tk.Entry(ventana_registrar_prov, font=("Arial", 11), width=25)
    entry_telefono.pack(pady=5)

    # Campo Dirección
    lbl_direccion = tk.Label(ventana_registrar_prov, text="Dirección:", bg="#f0f0f0", font=("Arial", 10))
    lbl_direccion.pack()
    entry_direccion = tk.Entry(ventana_registrar_prov, font=("Arial", 11), width=25)
    entry_direccion.pack(pady=5)

    # Función para guardar en un archivo de proveedores
    def guardar_proveedor():
        nombre = entry_nombre.get().strip()
        telefono = entry_telefono.get().strip()
        direccion = entry_direccion.get().strip()

        if not nombre or not telefono or not direccion:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not os.path.exists("Datos"):
            os.makedirs("Datos")

        # Guardar en un archivo de texto separado para proveedores
        with open("Datos/proveedores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Proveedor: {nombre} | Teléfono: {telefono} | Dirección: {direccion}\n")

        messagebox.showinfo("Éxito", f"¡Proveedor '{nombre}' registrado correctamente!")
        
        # Limpiar campos
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)

    # Botón Guardar
    btn_guardar = tk.Button(
        ventana_registrar_prov,
        text="Guardar Proveedor",
        bg="#FF9800",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        command=guardar_proveedor
    )
    btn_guardar.pack(pady=20)

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_registrar_prov,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_registrar_prov.destroy
    )
    btn_regresar.pack()