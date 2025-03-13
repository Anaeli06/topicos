import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Practica 1")
root.geometry("400x400")
root.configure(bg="purple")

label = tk.Label(root, text="Escribe algo:", bg="purple", fg="black")
label.pack()

entry = tk.Entry(root)
entry.pack()

def mostrar():
    text = entry.get()
    messagebox.showinfo("Aviso", "Escribiste: " + text)

btn = tk.Button(root, text="Aceptar", command=mostrar)
btn.pack()

btn_exit = tk.Button(root, text="Salir", command=root.destroy)
btn_exit.pack()

root.mainloop()
