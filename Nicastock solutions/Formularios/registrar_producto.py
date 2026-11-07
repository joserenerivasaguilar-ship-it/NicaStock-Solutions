# Formularios/registrar_producto.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_registrar_producto():
    ventana_registrar = tk.Toplevel()
    ventana_registrar.title("NicaStock Solutions - Registrar Producto")
    ventana_registrar.geometry("350x400")
    ventana_registrar.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_registrar, text="Registrar Nuevo Producto", font=("Arial", 13, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Campo Nombre del Producto
    lbl_nombre = tk.Label(ventana_registrar, text="Nombre del Producto:", bg="#f0f0f0", font=("Arial", 10))
    lbl_nombre.pack()
    entry_nombre = tk.Entry(ventana_registrar, font=("Arial", 11), width=25)
    entry_nombre.pack(pady=5)

    # Campo Precio
    lbl_precio = tk.Label(ventana_registrar, text="Precio (C$):", bg="#f0f0f0", font=("Arial", 10))
    lbl_precio.pack()
    entry_precio = tk.Entry(ventana_registrar, font=("Arial", 11), width=25)
    entry_precio.pack(pady=5)

    # Campo Cantidad / Stock
    lbl_cantidad = tk.Label(ventana_registrar, text="Cantidad en Stock:", bg="#f0f0f0", font=("Arial", 10))
    lbl_cantidad.pack()
    entry_cantidad = tk.Entry(ventana_registrar, font=("Arial", 11), width=25)
    entry_cantidad.pack(pady=5)

    # Función para guardar los datos en la carpeta Datos
    def guardar_producto():
        nombre = entry_nombre.get().strip()
        precio = entry_precio.get().strip()
        cantidad = entry_cantidad.get().strip()

        # Validar que no estén vacíos
        if not nombre or not precio or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            # Validar que precio y cantidad sean números
            float(precio)
            int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "El precio y la cantidad deben ser valores numéricos")
            return

        # Asegurarnos de que la carpeta Datos exista
        if not os.path.exists("Datos"):
            os.makedirs("Datos")

        # Guardar en un archivo de texto dentro de la carpeta Datos
        with open("Datos/productos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}\n")

        messagebox.showinfo("Éxito", f"¡Producto '{nombre}' registrado correctamente!")
        
        # Limpiar los campos
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)

    # Botón Guardar
    btn_guardar = tk.Button(
        ventana_registrar,
        text="Guardar Producto",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        command=guardar_producto
    )
    btn_guardar.pack(pady=20)

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_registrar,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_registrar.destroy
    )
    btn_regresar.pack()