import os

class FileHandler:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def load(self):
        if self.file_path and os.path.isfile(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return f.read()
        raise FileNotFoundError(f"No se puede encontrar el archivo: {self.file_path}")

    def save(self, content):
        if not self.file_path:
            raise ValueError("La ruta del archivo no está definida.")
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def remove(self):
        if self.file_path and os.path.isfile(self.file_path):
            os.remove(self.file_path)
        else:
            raise FileNotFoundError(f"El archivo no se pudo encontrar para eliminar: {self.file_path}")