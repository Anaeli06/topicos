import tkinter as tk
import random #genera los colores aleatorios

def mouse_click(event):
    label.config(text=f"Clic en ({event.x}, {event.y})")
    random_color = f'#{random.randint(0, 0xFFFFFF):06x}'
    root.config(bg=random_color)

def mouse_move(event):
    label.config(text=f"Movimiento en ({event.x}, {event.y})")

def key_press(event):
    key_label.config(text=f"Tecla presionada: {event.char}")

def clear_text(event):
    label.config(text="")
    key_label.config(text="")

root = tk.Tk()
root.title("Práctica 2")
root.geometry("400x300")

label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

key_label = tk.Label(root, text="", font=("Arial", 14))
key_label.pack(pady=20)

root.bind("<Button-1>", mouse_click)
root.bind("<Motion>", mouse_move)
root.bind("<KeyPress>", key_press)
root.bind("<space>", clear_text)

root.mainloop()
