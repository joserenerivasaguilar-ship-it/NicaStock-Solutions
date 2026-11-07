# Formularios/actualizar_proveedor.py
import tkinter as tk
from tkinter import messagebox
import os

def abrir_actualizar_proveedor():
    ventana_actualizar_prov = tk.Toplevel()
    ventana_actualizar_prov.title("NicaStock Solutions - Actualizar Proveedor")
    ventana_actualizar_prov.geometry("400x450")
    ventana_actualizar_prov.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_actualizar_prov, text="Actualizar Proveedor", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Buscar proveedor a modificar
    lbl_buscar = tk.Label(ventana_actualizar_prov, text="Nombre exacto del proveedor a modificar:", bg="#f0f0f0", font=("Arial", 10))
    lbl_buscar.pack()
    entry_buscar = tk.Entry(ventana_actualizar_prov, font=("Arial", 11), width=25)
    entry_buscar.pack(pady=5)

    # Nuevos datos
    lbl_nuevo_tel = tk.Label(ventana_actualizar_prov, text="Nuevo Teléfono:", bg="#f0f0f0", font=("Arial", 10))
    lbl_nuevo_tel.pack()
    entry_nuevo_tel = tk.Entry(ventana_actualizar_prov, font=("Arial", 11), width=25)
    entry_nuevo_tel.pack(pady=5)

    lbl_nueva_dir = tk.Label(ventana_actualizar_prov, text="Nueva Dirección:", bg="#f0f0f0", font=("Arial", 10))
    lbl_nueva_dir.pack()
    entry_nueva_dir = tk.Entry(ventana_actualizar_prov, font=("Arial", 11), width=25)
    entry_nueva_dir.pack(pady=5)

    # Función para ejecutar la actualización en el archivo
    def guardar_actualizacion():
        nombre_buscar = entry_buscar.get().strip().lower()
        nuevo_tel = entry_nuevo_tel.get().strip()
        nueva_dir = entry_nueva_dir.get().strip()

        if not nombre_buscar or not nuevo_tel or not nueva_dir:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not os.path.exists("Datos/proveedores.txt"):
            messagebox.showerror("Error", "No hay registros de proveedores.")
            return

        lineas_actualizadas = []
        encontrado = False

        with open("Datos/proveedores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if f"Proveedor: {nombre_buscar}" in linea.lower():
                    lineas_actualizadas.append(f"Proveedor: {entry_buscar.get().strip()} | Teléfono: {nuevo_tel} | Dirección: {nueva_dir}\n")
                    encontrado = True
                else:
                    lineas_actualizadas.append(linea)

        if encontrado:
            with open("Datos/proveedores.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(lineas_actualizadas)
            messagebox.showinfo("Éxito", "¡Proveedor actualizado correctamente!")
            ventana_actualizar_prov.destroy()
        else:
            messagebox.showerror("Error", "No se encontró un proveedor con ese nombre exacto.")

    # Botón Actualizar
    btn_actualizar = tk.Button(
        ventana_actualizar_prov,
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
        ventana_actualizar_prov,
        text="Regresar",
        bg="#757575",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=ventana_actualizar_prov.destroy
    )
    btn_regresar.pack()