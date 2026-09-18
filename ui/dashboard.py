from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton
)

from PyQt6.QtCore import Qt

from ui.data_entry import DataEntryWindow

import sys



class Dashboard(QWidget):

    def __init__(
        self,
        username,
        role,
        zone_id
    ):

        super().__init__()


        self.username = username

        self.role = role

        self.zone_id = zone_id


        self.data_entry = None


        self.setWindowTitle(
            "BMDA Irrigation Report System"
        )


        # =========================
        # Window Size
        # =========================

        self.resize(
            700,
            600
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


        self.setStyleSheet(
            """
            QWidget {

                background-color:white;

            }
            """
        )


        # =========================
        # Title
        # =========================

        title = QLabel(
            "BMDA Irrigation Report System",
            self
        )


        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        title.setGeometry(
            50,
            60,
            600,
            50
        )


        title.setStyleSheet(
            """
            font-size:28px;
            font-weight:bold;
            color:green;
            border:none;
            """
        )


        # =========================
        # User Information
        # =========================


        user_label = QLabel(
            f"Welcome: {self.username}",
            self
        )


        user_label.setGeometry(
            200,
            180,
            300,
            40
        )


        user_label.setStyleSheet(
            """
            font-size:20px;
            color:green;
            border:none;
            """
        )



        role_label = QLabel(
            f"Role: {self.role}",
            self
        )


        role_label.setGeometry(
            200,
            230,
            300,
            40
        )


        role_label.setStyleSheet(
            """
            font-size:18px;
            color:green;
            border:none;
            """
        )



        zone_text = (
            "All Zones"
            if self.zone_id is None
            else
            f"Zone ID: {self.zone_id}"
        )


        zone_label = QLabel(
            zone_text,
            self
        )


        zone_label.setGeometry(
            200,
            280,
            300,
            40
        )


        zone_label.setStyleSheet(
            """
            font-size:18px;
            color:green;
            border:none;
            """
        )



        # =========================
        # Regional Admin
        # =========================


        if self.role == "Regional Admin":


            self.view_button = QPushButton(
                "View Zone Report",
                self
            )


            self.view_button.setGeometry(
                200,
                360,
                300,
                45
            )



            self.generate_button = QPushButton(
                "Generate Report",
                self
            )


            self.generate_button.setGeometry(
                200,
                420,
                300,
                45
            )



            self.print_button = QPushButton(
                "Print Report",
                self
            )


            self.print_button.setGeometry(
                200,
                480,
                300,
                45
            )



            self.users_button = QPushButton(
                "Manage Users",
                self
            )


            self.users_button.setGeometry(
                200,
                540,
                300,
                45
            )


            self.style_buttons()



        # =========================
        # Zone User
        # =========================


        elif self.role == "Zone User":


            self.entry_button = QPushButton(
                "Daily Data Entry",
                self
            )


            self.entry_button.setGeometry(
                200,
                360,
                300,
                45
            )


            self.previous_button = QPushButton(
                "Previous Entry",
                self
            )


            self.previous_button.setGeometry(
                200,
                430,
                300,
                45
            )


            self.style_buttons()


            self.entry_button.clicked.connect(
                self.open_data_entry
            )



    # =========================
    # Button Style
    # =========================

    def style_buttons(self):

        buttons = []

        if self.role == "Zone User":

            buttons = [
                self.entry_button,
                self.previous_button
            ]


        elif self.role == "Regional Admin":

            buttons = [
                self.view_button,
                self.generate_button,
                self.print_button,
                self.users_button
            ]

        for button in buttons:
            button.setStyleSheet(
                """
                QPushButton {

                    background-color: green;

                    color: white;

                    font-size: 18px;

                    font-weight: bold;

                    border-radius: 10px;

                    padding: 5px;

                }


                QPushButton:hover {

                    background-color: darkgreen;

                }


                QPushButton:pressed {

                    background-color: #006400;

                }

                """
            )



    # =========================
    # Open Data Entry
    # =========================

    def open_data_entry(self):


        self.data_entry = DataEntryWindow(

            self.username,

            self.zone_id

        )


        self.data_entry.show()



if __name__ == "__main__":


    app = QApplication(sys.argv)


    window = Dashboard(

        "admin",

        "Regional Admin",

        None

    )


    window.show()


    sys.exit(
        app.exec()
    )