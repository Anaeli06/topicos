import tkinter as tk
from tkinter import messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto")
        self.master.geometry("800x400")
        self.text_widget = tk.Text(self.master, font=("Arial", 14))
        self.text_widget.pack(expand=True, fill="both")
        self.create_menu()
        self.setup_shortcuts()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.show_unavailable)
        file_menu.add_command(label="Guardar", command=self.show_unavailable)
        file_menu.add_command(label="Eliminar contenido", command=self.show_unavailable)
        file_menu.add_command(label="Salir", command=self.master.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Cambiar color del texto", command=self.show_unavailable)
        edit_menu.add_command(label="Buscar y reemplazar", command=self.show_unavailable)

    def setup_shortcuts(self):
        self.master.bind("<Control-o>", lambda event: self.show_unavailable())
        self.master.bind("<Control-s>", lambda event: self.show_unavailable())
        self.master.bind("<Control-d>", lambda event: self.show_unavailable())
        self.master.bind("<Control-t>", lambda event: self.show_unavailable())
        self.master.bind("<Control-f>", lambda event: self.show_unavailable())
        self.master.bind("<Control-q>", lambda event: self.master.quit())

    @staticmethod
    def show_unavailable():
        messagebox.showinfo("Peligro!", "Este botón no sirve! ):")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
