# Formularios/actualizar_producto.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_actualizar_producto():
    ventana_actualizar = tk.Toplevel()
    ventana_actualizar.title("NicaStock Solutions - Actualizar Producto")
    ventana_actualizar.geometry("400x450")
    ventana_actualizar.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_actualizar, text="Actualizar Producto", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Buscar producto a modificar
    lbl_buscar = tk.Label(ventana_actualizar, text="Nombre exacto a modificar:", bg="#f0f0f0", font=("Arial", 10))
    lbl_buscar.pack()
    entry_buscar = tk.Entry(ventana_actualizar, font=("Arial", 11), width=25)
    entry_buscar.pack(pady=5)

    # Nuevos datos
    lbl_nuevo_precio = tk.Label(ventana_actualizar, text="Nuevo Precio (C$):", bg="#f0f0f0", font=("Arial", 10))
    lbl_nuevo_precio.pack()
    entry_nuevo_precio = tk.Entry(ventana_actualizar, font=("Arial", 11), width=25)
    entry_nuevo_precio.pack(pady=5)

    lbl_nueva_cantidad = tk.Label(ventana_actualizar, text="Nueva Cantidad:", bg="#f0f0f0", font=("Arial", 10))
    lbl_nueva_cantidad.pack()
    entry_nueva_cantidad = tk.Entry(ventana_actualizar, font=("Arial", 11), width=25)
    entry_nueva_cantidad.pack(pady=5)

    # Función para ejecutar la actualización en el archivo
    def guardar_actualizacion():
        nombre_buscar = entry_buscar.get().strip().lower()
        nuevo_precio = entry_nuevo_precio.get().strip()
        nueva_cantidad = entry_nueva_cantidad.get().strip()

        if not nombre_buscar or not nuevo_precio or not nueva_cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            float(nuevo_precio)
            int(nueva_cantidad)
        except ValueError:
            messagebox.showerror("Error", "El precio y la cantidad deben ser valores numéricos")
            return

        if not os.path.exists("Datos/productos.txt"):
            messagebox.showerror("Error", "No hay registros de productos.")
            return

        # Leer todas las líneas y buscar la coincidencia
        lineas_actualizadas = []
        encontrado = False

        with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Verificamos si la línea contiene el nombre del producto
                if f"Producto: {nombre_buscar}" in linea.lower():
                    lineas_actualizadas.append(f"Producto: {entry_buscar.get().strip()} | Precio: {nuevo_precio} | Cantidad: {nueva_cantidad}\n")
                    encontrado = True
                else:
                    lineas_actualizadas.append(linea)

        if encontrado:
            with open("Datos/productos.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(lineas_actualizadas)
            messagebox.showinfo("Éxito", "¡Producto actualizado correctamente!")
            ventana_actualizar.destroy()
        else:
            messagebox.showerror("Error", "No se encontró un producto con ese nombre exacto.")

    # Botón Actualizar
    btn_actualizar = tk.Button(
        ventana_actualizar,
        text="Guardar Cambios",
        bg="#FF9800",
        fg="white",
        font=("Arial", 10, "bold"),
        width=18,
        command=guardar_actualizacion
    )
    btn_actualizar.pack(pady=15)

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_actualizar,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_actualizar.destroy
    )
    btn_regresar.pack()