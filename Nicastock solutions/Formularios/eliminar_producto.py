# Formularios/eliminar_producto.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_eliminar_producto():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("NicaStock Solutions - Eliminar Producto")
    ventana_eliminar.geometry("380x350")
    ventana_eliminar.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_eliminar, text="Eliminar Producto", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Campo para escribir el producto a eliminar
    lbl_eliminar = tk.Label(ventana_eliminar, text="Nombre exacto del producto a eliminar:", bg="#f0f0f0", font=("Arial", 10))
    lbl_eliminar.pack()
    
    entry_eliminar = tk.Entry(ventana_eliminar, font=("Arial", 11), width=25)
    entry_eliminar.pack(pady=10)

    # Función para procesar la eliminación
    def ejecutar_eliminacion():
        nombre_a_borrar = entry_eliminar.get().strip().lower()

        if not nombre_a_borrar:
            messagebox.showerror("Error", "Por favor ingrese el nombre del producto")
            return

        if not os.path.exists("Datos/productos.txt"):
            messagebox.showerror("Error", "No hay registros de productos.")
            return

        # Confirmación de seguridad
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto '{entry_eliminar.get().strip()}'?")
        if not confirmar:
            return

        lineas_conservadas = []
        encontrado = False

        with open("Datos/productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Si la línea contiene el nombre, no la guardamos (la eliminamos)
                if f"Producto: {nombre_a_borrar}" in linea.lower():
                    encontrado = True
                else:
                    lineas_conservadas.append(linea)

        if encontrado:
            with open("Datos/productos.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(lineas_conservadas)
            messagebox.showinfo("Éxito", "¡Producto eliminado correctamente!")
            ventana_eliminar.destroy()
        else:
            messagebox.showerror("Error", "No se encontró un producto con ese nombre exacto.")

    # Botón Eliminar
    btn_eliminar = tk.Button(
        ventana_eliminar,
        text="Eliminar Producto",
        bg="#f44336",
        fg="white",
        font=("Arial", 10, "bold"),
        width=18,
        command=ejecutar_eliminacion
    )
    btn_eliminar.pack(pady=15)

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_eliminar,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_eliminar.destroy
    )
    btn_regresar.pack()