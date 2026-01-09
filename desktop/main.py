import sys
from PyQt6.QtWidgets import QApplication
from views.login import LoginWindow
from views.dashboard import Dashboard

app = QApplication(sys.argv)

def open_dashboard():
    dashboard = Dashboard()
    dashboard.show()
    app.dashboard = dashboard  # evita GC

login = LoginWindow(on_success=open_dashboard)
login.show()

sys.exit(app.exec())
