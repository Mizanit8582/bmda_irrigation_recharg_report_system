from PyQt6.QtWidgets import QApplication

from ui.login import LoginWindow

import sys


def main():

    print(
        "Irrigation Report System Started"
    )


    app = QApplication(sys.argv)


    window = LoginWindow()

    window.show()


    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    main()