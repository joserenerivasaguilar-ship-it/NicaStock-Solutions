# Formularios/eliminar_proveedor.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_eliminar_proveedor():
    ventana_eliminar_prov = tk.Toplevel()
    ventana_eliminar_prov.title("NicaStock Solutions - Eliminar Proveedor")
    ventana_eliminar_prov.geometry("380x350")
    ventana_eliminar_prov.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_eliminar_prov, text="Eliminar Proveedor", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Campo para escribir el proveedor a eliminar
    lbl_eliminar = tk.Label(ventana_eliminar_prov, text="Nombre exacto del proveedor a eliminar:", bg="#f0f0f0", font=("Arial", 10))
    lbl_eliminar.pack()
    
    entry_eliminar = tk.Entry(ventana_eliminar_prov, font=("Arial", 11), width=25)
    entry_eliminar.pack(pady=10)

    # Función para procesar la eliminación
    def ejecutar_eliminacion():
        nombre_a_borrar = entry_eliminar.get().strip().lower()

        if not nombre_a_borrar:
            messagebox.showerror("Error", "Por favor ingrese el nombre del proveedor")
            return

        if not os.path.exists("Datos/proveedores.txt"):
            messagebox.showerror("Error", "No hay registros de proveedores.")
            return

        # Confirmación de seguridad
        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el proveedor '{entry_eliminar.get().strip()}'?")
        if not confirmar:
            return

        lineas_conservadas = []
        encontrado = False

        with open("Datos/proveedores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if f"Proveedor: {nombre_a_borrar}" in linea.lower():
                    encontrado = True
                else:
                    lineas_conservadas.append(linea)

        if encontrado:
            with open("Datos/proveedores.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(lineas_conservadas)
            messagebox.showinfo("Éxito", "¡Proveedor eliminado correctamente!")
            ventana_eliminar_prov.destroy()
        else:
            messagebox.showerror("Error", "No se encontró un proveedor con ese nombre exacto.")

    # Botón Eliminar
    btn_eliminar = tk.Button(
        ventana_eliminar_prov,
        text="Eliminar Proveedor",
        bg="#f44336",
        fg="white",
        font=("Arial", 10, "bold"),
        width=18,
        command=ejecutar_eliminacion
    )
    btn_eliminar.pack(pady=15)

    # Botón Regresar
    btn_regresar = tk.Button(
        ventana_eliminar_prov,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_eliminar_prov.destroy
    )
    btn_regresar.pack()