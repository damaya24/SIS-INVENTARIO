from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QListWidget, QPushButton
)
from services.api import get_products
from views.new_product import NewProductWindow

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StockFlow - Dashboard")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Productos"))

        self.list = QListWidget()
        layout.addWidget(self.list)

        btn = QPushButton("Nuevo Producto")
        btn.clicked.connect(self.open_new_product)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.load_products()

    def load_products(self):
        self.list.clear()
        products = get_products()
        for p in products:
            self.list.addItem(
                f"{p['codigo']} - {p['nombre']} ({p['cantidad']})"
            )

    def open_new_product(self):
        self.new_window = NewProductWindow(self.load_products)
        self.new_window.show()
