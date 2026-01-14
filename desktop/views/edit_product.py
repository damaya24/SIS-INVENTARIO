from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from services.api import update_product
'''UI EDITAR PRODUCTO'''
class EditProductWindow(QWidget):
    def __init__(self, product, on_updated):
        super().__init__()
        self.product = product
        self.on_updated = on_updated

        self.setWindowTitle("Editar Producto")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.codigo = QLineEdit(product["codigo"])
        self.nombre = QLineEdit(product["nombre"])
        self.categoria = QLineEdit(product["categoria"])
        self.cantidad = QLineEdit(str(product["cantidad"]))
        self.precio = QLineEdit(str(product["precio"]))

        btn = QPushButton("Guardar Cambios")
        btn.clicked.connect(self.save)

        layout.addWidget(QLabel("Editar Producto"))
        layout.addWidget(self.codigo)
        layout.addWidget(self.nombre)
        layout.addWidget(self.categoria)
        layout.addWidget(self.cantidad)
        layout.addWidget(self.precio)
        layout.addWidget(btn)

        self.setLayout(layout)

    def save(self):
        data = {
            "codigo": self.codigo.text(),
            "nombre": self.nombre.text(),
            "categoria": self.categoria.text(),
            "cantidad": int(self.cantidad.text()),
            "precio": float(self.precio.text())
        }

        if update_product(self.product["id"], data):
            QMessageBox.information(self, "OK", "Producto actualizado")
            self.on_updated()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar")
