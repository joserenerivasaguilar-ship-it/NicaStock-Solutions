# Formularios/gestion_proveedores.py
import tkinter as tk
from tkinter import messagebox
from Formularios.registrar_proveedor import abrir_registrar_proveedor
from Formularios.listar_proveedores import abrir_listar_proveedores
from Formularios.buscar_proveedor import abrir_buscar_proveedor
from Formularios.actualizar_proveedor import abrir_actualizar_proveedor
from Formularios.eliminar_proveedor import abrir_eliminar_proveedor
from Formularios.contar_proveedores import abrir_contar_proveedores

def abrir_gestion_proveedores():
    ventana_proveedores = tk.Toplevel()
    ventana_proveedores.title("NicaStock Solutions - Gestión de Proveedores")
    ventana_proveedores.geometry("450x500")
    ventana_proveedores.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_proveedores, text="Gestión de Proveedores", font=("Arial", 15, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    lbl_sub = tk.Label(ventana_proveedores, text="Seleccione la operación que desea realizar:", font=("Arial", 10), bg="#f0f0f0")
    lbl_sub.pack(pady=5)

    def ejecutar_accion(accion):
        if accion == "Registrar Proveedor":
            abrir_registrar_proveedor()
        elif accion == "Listar Proveedores":
            abrir_listar_proveedores()
        elif accion == "Buscar Proveedor":
            abrir_buscar_proveedor()
        elif accion == "Actualizar Proveedor":
            abrir_actualizar_proveedor()
        elif accion == "Eliminar Proveedor":
            abrir_eliminar_proveedor()
        elif accion == "Contar Proveedores":
            abrir_contar_proveedores()
        else:
            messagebox.showinfo("Módulo de Proveedores", f"Aquí se programará la pantalla para: {accion}")

    # Botones según la guía BPMN para proveedores
    operaciones = [
        "Registrar Proveedor",
        "Listar Proveedores",
        "Buscar Proveedor",
        "Actualizar Proveedor",
        "Eliminar Proveedor",
        "Contar Proveedores"
    ]

    for op in operaciones:
        btn = tk.Button(
            ventana_proveedores,
            text=op,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            width=28,
            command=lambda o=op: ejecutar_accion(o)
        )
        btn.pack(pady=6)

    # Botón para regresar
    btn_regresar = tk.Button(
        ventana_proveedores,
        text="Regresar al Menú Principal",
        bg="#757575",
        fg="white",
        font=("Arial", 10),
        width=28,
        command=ventana_proveedores.destroy
    )
    btn_regresar.pack(pady=15)