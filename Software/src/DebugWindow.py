from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PySide2.QtCore import QTimer
from ui_DebugWindow import Ui_Dialog
from ApplicationManager import ApplicationManager


class DebugWindow(QMainWindow):
    """
    Klasa odpowiedzialna za działanie okienka do debugowania
    """
    def __init__(self, app_manag, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        def connect_to_device():
            ip = self.ui.ip_input.toPlainText()
            port = self.ui.port_input.toPlainText()
            app_manag.connect_to_device(ip, port)

        self.ui.btn_connect.clicked.connect(connect_to_device)