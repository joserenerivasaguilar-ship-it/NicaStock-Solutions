# Formularios/login.py
import tkinter as tk
from tkinter import messagebox
from Formularios.menu_principal import abrir_menu_principal

def abrir_login():
    # Creación de la ventana de inicio de sesión
    ventana_login = tk.Tk()
    ventana_login.title("NicaStock Solutions - Iniciar Sesión")
    ventana_login.geometry("300x250")
    ventana_login.config(bg="#f0f0f0")

    # Título
    titulo = tk.Label(ventana_login, text="Iniciar Sesión", font=("Arial", 14, "bold"), bg="#f0f0f0")
    titulo.pack(pady=15)

    # Campo Usuario
    label_usuario = tk.Label(ventana_login, text="Usuario:", bg="#f0f0f0", font=("Arial", 10))
    label_usuario.pack()
    entry_usuario = tk.Entry(ventana_login, font=("Arial", 11))
    entry_usuario.pack(pady=5)

    # Campo Contraseña
    label_password = tk.Label(ventana_login, text="Contraseña:", bg="#f0f0f0", font=("Arial", 10))
    label_password.pack()
    entry_password = tk.Entry(ventana_login, show="*", font=("Arial", 11))
    entry_password.pack(pady=5)

    # Función interna para verificar los datos al hacer clic en el botón
    def verificar_credenciales():
        usuario = entry_usuario.get()
        password = entry_password.get()
        
        # Datos de prueba para la defensa
        if usuario == "admin" and password == "1234":
            # 1. Cerramos primero la ventana de login para evitar errores de Tkinter
            ventana_login.destroy()
            # 2. Mostramos el mensaje y abrimos el menú principal
            messagebox.showinfo("Éxito", "¡Acceso concedido a NicaStock Solutions!")
            abrir_menu_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # Botón Acceder
    btn_acceder = tk.Button(
        ventana_login, 
        text="Acceder", 
        bg="#4CAF50", 
        fg="white", 
        font=("Arial", 10, "bold"), 
        width=15, 
        command=verificar_credenciales
    )
    btn_acceder.pack(pady=15)

    ventana_login.mainloop()

