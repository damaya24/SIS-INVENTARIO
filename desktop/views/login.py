from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from services.api import login

class LoginWindow(QWidget):
    def __init__(self, on_success):
        super().__init__()
        self.on_success = on_success
        self.setWindowTitle("StockFlow - Login")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        btn = QPushButton("Ingresar")
        btn.clicked.connect(self.handle_login)

        layout.addWidget(QLabel("Iniciar Sesión"))
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(btn)

        self.setLayout(layout)

    def handle_login(self):
        if login(self.email.text(), self.password.text()):
            self.on_success()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")
