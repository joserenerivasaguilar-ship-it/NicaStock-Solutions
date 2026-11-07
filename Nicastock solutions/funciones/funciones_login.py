# funciones/funciones_login.py
import os

def validar_credenciales(usuario, contraseña):
    # Credenciales por defecto para el sistema
    usuario_valido = "admin"
    contrasena_valida = "1234"
    
    if usuario == usuario_valido and contraseña == contrasena_valida:
        return True
    return False