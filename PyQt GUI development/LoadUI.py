from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt6.QtGui import QIcon
import sys
from PyQt6 import uic

class UI(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("PyQt GUI development\windowsui.ui", self)


app = QApplication(sys.argv)
window = UI()
window.show()

app.exec()
