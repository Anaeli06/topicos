import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from practica5 import FileHandler

class TextEditor:
    def __init__(self, master):
        self.root = None
        self.master = master
        self.master.title("Editor de Texto")
        self.master.geometry("800x400")
        self.text_widget = tk.Text(self.master, font=("Arial", 14))
        self.text_widget.pack(expand=True, fill="both")
        self.create_menu()
        self.setup_shortcuts()
        self.file_handler = None

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Eliminar contenido", command=self.delete_content)
        file_menu.add_command(label="Salir", command=self.master.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Cambiar color del texto", command=self.change_text_color)
        edit_menu.add_command(label="Buscar y reemplazar", command=self.find_and_replace)

    def setup_shortcuts(self):
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        self.master.bind("<Control-d>", lambda event: self.delete_content())
        self.master.bind("<Control-t>", lambda event: self.change_text_color())
        self.master.bind("<Control-f>", lambda event: self.find_and_replace())
        self.master.bind("<Control-q>", lambda event: self.master.quit())

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if file_path:
            try:
                self.file_handler = FileHandler(file_path)
                file_content = self.file_handler.load()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, file_content)
            except FileNotFoundError as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        if self.file_handler:
            content = self.text_widget.get(1.0, tk.END)
            try:
                self.file_handler.save(content)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
            if file_path:
                self.file_handler = FileHandler(file_path)
                content = self.text_widget.get(1.0, tk.END)
                try:
                    self.file_handler.save(content)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))

    def delete_content(self):
        response = messagebox.askyesno("Confirmar", "¿Estas seguro de borrar esta obra maestra ):?")
        if response:
            self.text_widget.delete(1.0, tk.END)

    def change_text_color(self):
        color = colorchooser.askcolor(title="Selecciona un color")[1]
        if color:
            self.text_widget.config(fg=color)

    def find_and_replace(self):
        def replace_text():
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            content = self.text_widget.get(1.0, tk.END)
            new_content = content.replace(find_text, replace_text)
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(1.0, new_content)

        find_window = tk.Toplevel(self.root)
        find_window.title("Buscar y remplazar")
        find_window.geometry("300x150")

        tk.Label(find_window, text="Introduce la palabra:").pack()
        find_entry = tk.Entry(find_window)
        find_entry.pack()

        tk.Label(find_window, text="Remplazar la palabra con:").pack()
        replace_entry = tk.Entry(find_window)
        replace_entry.pack()

        tk.Button(find_window, text="Remplazar", command=replace_text).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()