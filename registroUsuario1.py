import tkinter as tk
from tkinter import messagebox  # Importar el módulo messagebox para ventanas emergentes

def registrar():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contrasenia = entry_contrasenia.get()
    aceptar_terminos = var_terminos.get()

    if aceptar_terminos:
        # Mostrar mensaje de registro exitoso en una nueva ventana
        ventana_registro_exitoso = tk.Toplevel()
        ventana_registro_exitoso.title("Registro exitoso")
        
        mensaje_registro_exitoso = tk.Label(ventana_registro_exitoso, text=f"¡Registro Exitoso!\n Nombre: {nombre}\n Correo Electrónico: {correo}")
        mensaje_registro_exitoso.pack(padx=20, pady=20)
        #mensaje_registro_exitoso.grid(row=0, column=0)
        
        boton_cerrar = tk.Button(ventana_registro_exitoso, text="Aceptar", command=ventana_registro_exitoso.destroy)
        boton_cerrar.pack(padx=10, pady=10)
        #boton_cerrar.grid(row=0, column=0)
    else:
        messagebox.showerror("Error", "Debes aceptar los términos y condiciones")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.configure(bg="#C3C3C3")  # Color de fondo personalizado
ventana.geometry("300x240")
ventana.resizable(False, False)

# Etiquetas y campos de entrada
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10)
etiqueta_nombre.configure(bg="#C3C3C3")  # Color de fondo personalizado

entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

etiqueta_correo = tk.Label(ventana, text="Correo Electrónico:")
etiqueta_correo.grid(row=1, column=0, padx=10, pady=10)
etiqueta_correo.configure(bg="#C3C3C3")  # Color de fondo personalizado

entry_correo = tk.Entry(ventana)
entry_correo.grid(row=1, column=1, padx=10, pady=10)

etiqueta_contrasenia = tk.Label(ventana, text="Contraseña:")
etiqueta_contrasenia.grid(row=2, column=0, padx=10, pady=10)
etiqueta_contrasenia.configure(bg="#C3C3C3")  # Color de fondo personalizado

entry_contrasenia = tk.Entry(ventana, show="*")
entry_contrasenia.grid(row=2, column=1, padx=10, pady=10)

# Casilla de verificación para términos y condiciones
var_terminos = tk.BooleanVar()
check_terminos = tk.Checkbutton(ventana, text="Acepto los términos y condiciones", variable=var_terminos)
check_terminos.grid(row=3, columnspan=2, padx=10, pady=10)
check_terminos.configure(bg="#C3C3C3")  # Color de fondo personalizado

# Botón de registro
boton_registrar = tk.Button(ventana, text="Registrar", font="Helvetica 10 bold", command=registrar)
boton_registrar.grid(row=4, columnspan=2, padx=10, pady=10)
boton_registrar.configure(width= 20, bg="#5386E4", fg="#FFFFFF")  # Ancho del botón personalizado width=20

# Ejecutar la aplicación
ventana.mainloop()
