from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys

app = QApplication(sys.argv)

# window = QWidget()
window = QMainWindow()
window.statusBar().showMessage("Welcome to PyQt6 Course")
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())
