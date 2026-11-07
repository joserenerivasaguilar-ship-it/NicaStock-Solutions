# Formularios/gestion_productos.py
import tkinter as tk
from tkinter import messagebox
from Formularios.registrar_producto import abrir_registrar_producto
from Formularios.listar_productos import abrir_listar_productos
from Formularios.buscar_producto import abrir_buscar_producto
from Formularios.actualizar_producto import abrir_actualizar_producto
from Formularios.eliminar_producto import abrir_eliminar_producto
from Formularios.contar_productos import abrir_contar_productos

def abrir_gestion_productos():
    ventana_productos = tk.Toplevel()
    ventana_productos.title("NicaStock Solutions - Gestión de Productos")
    ventana_productos.geometry("450x500")
    ventana_productos.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_productos, text="Gestión de Productos", font=("Arial", 15, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    lbl_sub = tk.Label(ventana_productos, text="Seleccione la operación que desea realizar:", font=("Arial", 10), bg="#f0f0f0")
    lbl_sub.pack(pady=5)

    def ejecutar_accion(accion):
        if accion == "Registrar Producto":
            abrir_registrar_producto()
        elif accion == "Listar Productos":
            abrir_listar_productos()
        elif accion == "Buscar Producto":
            abrir_buscar_producto()
        elif accion == "Actualizar Producto":
            abrir_actualizar_producto()
        elif accion == "Eliminar Producto":
            abrir_eliminar_producto()
        elif accion == "Contar Productos":
            abrir_contar_productos()
        else:
            messagebox.showinfo("Módulo de Productos", f"Aquí se programará la pantalla para: {accion}")

    # Botones según la guía BPMN (Registrar, Listar, Buscar, Actualizar, Eliminar, Contar)
    operaciones = [
        "Registrar Producto",
        "Listar Productos",
        "Buscar Producto",
        "Actualizar Producto",
        "Eliminar Producto",
        "Contar Productos"
    ]

    for op in operaciones:
        btn = tk.Button(
            ventana_productos,
            text=op,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            width=28,
            command=lambda o=op: ejecutar_accion(o)
        )
        btn.pack(pady=6)

    # Botón para regresar
    btn_regresar = tk.Button(
        ventana_productos,
        text="Regresar al Menú Principal",
        bg="#757575",
        fg="white",
        font=("Arial", 10),
        width=28,
        command=ventana_productos.destroy
    )
    btn_regresar.pack(pady=15)