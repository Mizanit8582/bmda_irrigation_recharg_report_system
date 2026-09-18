from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Irrigation Report System")
        self.setGeometry(300, 200, 800, 500)

        label = QLabel("Irrigation Report System Running", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label.setGeometry(150, 200, 500, 50)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())