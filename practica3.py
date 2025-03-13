import tkinter as tk
from tkinter import messagebox

def validar():
    nombre = entrada_nombre.get()
    correo = entrada_correo.get()
    edad = entrada_edad.get()

    if not nombre:
        messagebox.showerror("Error", "El nombre no debe estar vacio")
        return
    if "@" not in correo or "." not in correo:
        messagebox.showerror("Error", "Correo no valido")
        return
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un numero")
        return

    messagebox.showinfo("Datos de la persona",
                        f"Nombre: {nombre}\nCorreo: {correo}\nEdad: {edad}\nEscolaridad: {escolaridad_var.get()}")

def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    escolaridad_var.set("Seleccione")

ventana = tk.Tk()
ventana.title("Practica 3")
ventana.geometry("300x250")

tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Correo:").pack()
entrada_correo = tk.Entry(ventana)
entrada_correo.pack()

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

escolaridad_var = tk.StringVar(ventana)
escolaridad_var.set("Seleccione")
tk.Label(ventana, text="Escolaridad:").pack()
escolaridad_menu = tk.OptionMenu(ventana, escolaridad_var, "Primaria", "Secundaria", "Preparatoria", "Universidad")
escolaridad_menu.pack()

tk.Button(ventana, text="Enviar", command=validar).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

ventana.mainloop()