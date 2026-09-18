from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from sqlalchemy.orm import Session
from database.connection import engine
from models.user import User

from ui.dashboard import Dashboard

import sys
import os


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "BMDA IRRIGATION REPORT SYSTEM"
        )

        # =========================
        # Window Size
        # =========================

        self.resize(
            450,
            650
        )

        # =========================
        # Center Window
        # =========================

        screen = QApplication.primaryScreen()

        screen_geometry = screen.availableGeometry()

        x = (
                    screen_geometry.width()
                    -
                    self.width()
            ) // 2

        y = (
                    screen_geometry.height()
                    -
                    self.height()
            ) // 2

        self.move(
            x,
            y
        )

        # =========================
        # Logo
        # =========================

        logo = QLabel(self)

        logo_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "assets",
            "logo.png"
        )

        pixmap = QPixmap(
            logo_path
        )

        logo.setPixmap(
            pixmap
        )

        logo.setScaledContents(
            True
        )

        logo.setGeometry(
            135,
            40,
            180,
            150
        )

        logo.setStyleSheet(
            """
            border:none;
            """
        )
        # Green Border + White Background
        self.setStyleSheet("""
            LoginWindow {
                background-color: white;
                border: 4px solid green;
            }
        """)

        title = QLabel("BMDA IRRIGATION REPORT\n SYSTEM", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(50, 250, 350, 50)

        title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: green;
            border: none;
        """)

        username_label = QLabel("Username", self)
        username_label.setGeometry(70, 340, 120, 30)

        username_label.setStyleSheet("""
            font-size: 16px;
            color: green;
            border: none;
        """)


        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(70, 370, 310, 40)

        self.username_input.setPlaceholderText("Enter Username")

        self.username_input.setStyleSheet("""
            font-size: 15px;
            border: 2px solid green;
            border-radius: 8px;
            padding: 5px;
        """)


        password_label = QLabel("Password", self)
        password_label.setGeometry(70, 430, 120, 30)

        password_label.setStyleSheet("""
            font-size: 16px;
            color: green;
            border: none;
        """)


        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(70, 460, 310, 40)

        self.password_input.setPlaceholderText("Enter Password")

        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.password_input.setStyleSheet("""
            font-size: 15px;
            border: 2px solid green;
            border-radius: 8px;
            padding: 5px;
        """)
        login_button = QPushButton("LOGIN", self)
        login_button.clicked.connect(self.login_test)

        login_button.setGeometry(120, 530, 210, 45)

        login_button.setStyleSheet("""
            QPushButton {
                background-color: green;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: darkgreen;
            }
        """)

    def login_test(self):

        username = self.username_input.text()
        password = self.password_input.text()

        with Session(engine) as session:

            user = session.query(User).filter(
                User.username == username,
                User.password == password
            ).first()

            if user:

                print("Username:", user.username)
                print("Role:", user.role)
                print("Zone ID:", user.zone_id)

                self.dashboard = Dashboard(
                    user.username,
                    user.role,
                    user.zone_id
                )

                self.dashboard.show()

                self.close()

            else:
                QMessageBox.warning(
                    self,
                    "Login Failed",
                    "Invalid Username or Password"
                )
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = LoginWindow()

    window.show()

    sys.exit(
        app.exec()
    )