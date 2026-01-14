from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QListWidget, QPushButton, QMessageBox
)
from services.api import get_products, delete_product
from views.new_product import NewProductWindow
from views.edit_product import EditProductWindow

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StockFlow - Dashboard")
        self.setFixedSize(450, 450)

        self.products = []

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Productos"))

        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.edit_selected)
        layout.addWidget(self.list)

        btn_new = QPushButton("Nuevo Producto")
        btn_new.clicked.connect(self.open_new_product)

        btn_delete = QPushButton("Eliminar Producto")
        btn_delete.clicked.connect(self.delete_selected)

        layout.addWidget(btn_new)
        layout.addWidget(btn_delete)

        self.setLayout(layout)
        self.load_products()

    def load_products(self):
        self.list.clear()
        self.products = get_products()
        for p in self.products:
            self.list.addItem(
                f"{p['codigo']} - {p['nombre']} ({p['cantidad']})"
            )

    def get_selected(self):
        index = self.list.currentRow()
        if index == -1:
            return None
        return self.products[index]

    def open_new_product(self):
        self.new_window = NewProductWindow(self.load_products)
        self.new_window.show()

    def edit_selected(self):
        product = self.get_selected()
        if product:
            self.edit_window = EditProductWindow(product, self.load_products)
            self.edit_window.show()

    def delete_selected(self):
        product = self.get_selected()
        if not product:
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Eliminar {product['nombre']}?"
        )

        if confirm == QMessageBox.StandardButton.Yes:
            if delete_product(product["id"]):
                self.load_products()