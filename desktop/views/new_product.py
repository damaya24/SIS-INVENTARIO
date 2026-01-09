from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from services.api import create_product

class NewProductWindow(QWidget):
    def __init__(self, on_created):
        super().__init__()
        self.on_created = on_created
        self.setWindowTitle("Nuevo Producto")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código")

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Nombre")

        self.categoria = QLineEdit()
        self.categoria.setPlaceholderText("Categoría")

        self.cantidad = QLineEdit()
        self.cantidad.setPlaceholderText("Cantidad")

        self.precio = QLineEdit()
        self.precio.setPlaceholderText("Precio")

        btn = QPushButton("Guardar")
        btn.clicked.connect(self.save)

        layout.addWidget(QLabel("Crear Producto"))
        layout.addWidget(self.codigo)
        layout.addWidget(self.nombre)
        layout.addWidget(self.categoria)
        layout.addWidget(self.cantidad)
        layout.addWidget(self.precio)
        layout.addWidget(btn)

        self.setLayout(layout)

    def save(self):
        product = {
            "codigo": self.codigo.text(),
            "nombre": self.nombre.text(),
            "categoria": self.categoria.text(),
            "cantidad": int(self.cantidad.text()),
            "precio": float(self.precio.text())
        }

        if create_product(product):
            QMessageBox.information(self, "OK", "Producto creado")
            self.on_created()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "No se pudo crear el producto")
