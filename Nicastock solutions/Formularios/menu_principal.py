# Formularios/menu_principal.py
import tkinter as tk
from tkinter import messagebox
from Formularios.gestion_productos import abrir_gestion_productos
from Formularios.gestion_proveedores import abrir_gestion_proveedores

def abrir_menu_principal():
    ventana_menu = tk.Tk()
    ventana_menu.title("NicaStock Solutions - Menú Principal")
    ventana_menu.geometry("400x350")
    ventana_menu.config(bg="#f0f0f0")

    # Título principal
    titulo = tk.Label(ventana_menu, text="Menú Principal", font=("Arial", 16, "bold"), bg="#f0f0f0")
    titulo.pack(pady=20)

    # Subtítulo / Indicación
    lbl_instruccion = tk.Label(ventana_menu, text="Seleccione el módulo que desea gestionar:", font=("Arial", 11), bg="#f0f0f0")
    lbl_instruccion.pack(pady=10)

    def ir_a_productos():
        abrir_gestion_productos()
        

    def ir_a_proveedores():
        abrir_gestion_proveedores()

    # Botón Gestión de Productos
    btn_productos = tk.Button(
        ventana_menu, 
        text="📦 Gestionar Productos", 
        bg="#2196F3", 
        fg="white", 
        font=("Arial", 11, "bold"), 
        width=25, 
        command=ir_a_productos
    )
    btn_productos.pack(pady=10)

    # Botón Gestión de Proveedores
    btn_proveedores = tk.Button(
        ventana_menu, 
        text="🤝 Gestionar Proveedores", 
        bg="#FF9800", 
        fg="white", 
        font=("Arial", 11, "bold"), 
        width=25, 
        command=ir_a_proveedores
    )
    btn_proveedores.pack(pady=10)

    # Botón Cerrar Sesión / Salir
    btn_salir = tk.Button(
        ventana_menu, 
        text="Cerrar Sesión", 
        bg="#f44336", 
        fg="white", 
        font=("Arial", 10), 
        width=15, 
        command=ventana_menu.destroy
    )
    btn_salir.pack(pady=20)

    ventana_menu.mainloop()