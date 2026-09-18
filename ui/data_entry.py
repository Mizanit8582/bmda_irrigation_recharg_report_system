from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QDateEdit,
    QPushButton,
    QMessageBox,
    QDialog,
    QTableWidgetItem
)

from PyQt6.QtCore import QDate
from ui.view_data import ViewDataDialog

from sqlalchemy.orm import Session

from database.connection import engine
from models.zone import Zone
from models.upazila import Upazila
from ui.custom_table import CustomReportTable
from models.daily_report import DailyReport
from datetime import datetime
import sys


class PreviousEntryDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent_window = parent


        self.setWindowTitle(
            "Previous Entry Search"
        )


        self.setGeometry(
            500,
            300,
            400,
            280
        )


        self.create_ui()

    def create_ui(self):

        # =========================
        # Title
        # =========================

        title = QLabel(
            "Search Previous Report",
            self
        )

        title.setGeometry(
            80,
            30,
            250,
            30
        )

        # =========================
        # Report Date
        # =========================

        date_label = QLabel(
            "Report Date:",
            self
        )

        date_label.setGeometry(
            50,
            90,
            120,
            30
        )

        date_label.setStyleSheet(
            """
            font-size:16px;
            color:green;
            border:none;
            """
        )

        self.date_input = QDateEdit(
            self
        )

        self.date_input.setDate(
            QDate.currentDate()
        )

        self.date_input.setCalendarPopup(
            True
        )

        self.date_input.setDisplayFormat(
            "dd-MM-yyyy"
        )

        self.date_input.setGeometry(
            180,
            90,
            180,
            35
        )

        # =========================
        # Upazila
        # =========================

        upazila_label = QLabel(
            "Upazila:",
            self
        )

        upazila_label.setGeometry(
            50,
            140,
            120,
            30
        )

        self.search_upazila = QComboBox(
            self
        )

        self.search_upazila.setGeometry(
            180,
            140,
            180,
            35
        )

        self.search_upazila.addItems([

            "-- উপজেলা নির্বাচন করুন --",

            "পঞ্চগড় উপজেলা",

            "তেতুলিয়া উপজেলা",

            "বোদা উপজেলা",

            "দেবীগঞ্জ উপজেলা",

            "আটোয়ারী উপজেলা"

        ])

        # =========================
        # Search Button
        # =========================

        self.search_button = QPushButton(
            "Search Report",
            self
        )

        self.search_button.setGeometry(
            120,
            210,
            150,
            35
        )

        self.search_button.clicked.connect(
            self.search_report
        )



    # =========================
    # Search Function
    # =========================

    def search_report(self):

        report_date = self.date_input.date().toPyDate()

        upazila = self.search_upazila.currentText()

        print(report_date)

        print(upazila)

        # =========================
        # Find Upazila ID
        # =========================


        with Session(engine) as session:

            upazila_obj = session.query(
                Upazila
            ).filter(
                Upazila.upazila_name == upazila
            ).first()

        if not upazila_obj:
            QMessageBox.warning(
                self,
                "Search Error",
                "Upazila Not Found"
            )

            return

        upazila_id = upazila_obj.id

        print(
            "Upazila ID:",
            upazila_id
        )

        # =========================
        # Find Report
        # =========================

        print("Searching Date:", report_date)

        print("Searching Upazila ID:", upazila_id)

        with Session(engine) as session:
            all_reports = session.query(
                DailyReport
            ).all()

            print("===== All Reports =====")

            for r in all_reports:
                print(
                    r.id,
                    r.upazila_id,
                    r.report_date
                )

            print("======================")

            report = session.query(
                DailyReport
            ).filter(

                DailyReport.upazila_id ==
                upazila_id,

                DailyReport.report_date ==
                report_date

            ).first()

        if report:

            print("Report Found")

            print(
                "Report ID:",
                report.id
            )

            print(
                "Deep Well New:",
                report.deep_well_new
            )

            print(
                "Deep Well Commission:",
                report.deep_well_commission
            )

            print(
                "LLP Used:",
                report.llp_used
            )

            print(
                "LLP Commission:",
                report.llp_commission
            )

            print(
                "AUS:",
                report.aus
            )

            print(
                "Current Charge:",
                report.current_charge
            )

            # =========================
            # Crop Load
            # =========================

            self.parent_window.report_table.item(
                3, 7
            ).setText(
                str(report.aus)
            )
            self.parent_window.report_table.item(
                3, 8
            ).setText(
                str(report.aus_other)
            )

            self.parent_window.report_table.item(
                3, 9
            ).setText(
                str(report.aman)
            )

            self.parent_window.report_table.item(
                3, 10
            ).setText(
                str(report.aman_other)
            )

            self.parent_window.report_table.item(
                3, 11
            ).setText(
                str(report.boro)
            )

            self.parent_window.report_table.item(
                3, 12
            ).setText(
                str(report.maize)
            )

            self.parent_window.report_table.item(
                3, 13
            ).setText(
                str(report.wheat)
            )

            self.parent_window.report_table.item(
                3, 14
            ).setText(
                str(report.potato)
            )

            self.parent_window.report_table.item(
                3, 15
            ).setText(
                str(report.mustard)
            )

            self.parent_window.report_table.item(
                3, 16
            ).setText(
                str(report.lentil)
            )

            self.parent_window.report_table.item(
                3, 17
            ).setText(
                str(report.other_crop)
            )

            # =========================
            # Deep Well Load
            # =========================

            self.parent_window.report_table.item(
                3, 2
            ).setText(
                str(report.deep_well_new)
            )

            self.parent_window.report_table.item(
                3, 3
            ).setText(
                str(report.deep_well_commission)
            )
            self.parent_window.report_table.item(
                3, 4
            ).setText(
                str(report.deep_well_used)
            )

            # =========================
            # LLP Load
            # =========================

            self.parent_window.report_table.item(
                3, 5
            ).setText(
                str(report.llp_used)
            )

            self.parent_window.report_table.item(
                3, 6
            ).setText(
                str(report.llp_commission)
            )

            # =========================
            # Charge Load
            # =========================

            self.parent_window.report_table.item(
                3, 20
            ).setText(
                str(report.previous_charge)
            )

            self.parent_window.report_table.item(
                3, 21
            ).setText(
                str(report.current_charge)
            )

            self.parent_window.report_table.item(
                3, 22
            ).setText(
                str(report.recharge)
            )

            # =========================
            # Farmer Family Load
            # =========================

            self.parent_window.report_table.item(
                3, 27
            ).setText(
                str(report.farmer_family)
            )

            QMessageBox.information(
                self,
                "Search Result",
                "Report Found Successfully"
            )



        else:

            QMessageBox.warning(

                self,

                "Search Result",

                "No Report Found"

            )


class DataEntryWindow(QWidget):


    def __init__(self, username, zone_id):

        super().__init__()


        self.username = username
        self.zone_id = zone_id
        print(zone_id)

        self.setWindowTitle(
            "BMDA Irrigation Report System - Data Entry"
        )

        # =========================
        # Window Size
        # =========================

        self.resize(
            1250,
            700
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


        self.setFont(
            QFont(
                "Nirmala UI",
                12
            )
        )

        # =========================
        # Title
        # =========================

        title = QLabel(
            "BMDA Irrigation Report System",
            self
        )

        title.setGeometry(
            120,
            30,
            700,
            40
        )

        title.setStyleSheet("""

            font-size:26px;
            font-weight:bold;
            color:green;

        """)

        # =========================
        # Zone Name
        # =========================

        with Session(engine) as session:

            zone = session.query(Zone).filter(
                Zone.id == self.zone_id
            ).first()

        if zone:

            zone_name = zone.zone_name

        else:

            zone_name = "Unknown Zone"

        zone_label = QLabel(
            f"Zone Name: {zone_name}",
            self
        )

        zone_label.setGeometry(
            80,
            90,
            400,
            30
        )

        zone_label.setStyleSheet("""

            font-size:18px;
            color:green;

        """)

        # =========================
        # Date
        # =========================

        date_label = QLabel(
            "Report Date:",
            self
        )

        date_label.setGeometry(
            80,
            135,
            150,
            30
        )

        date_label.setStyleSheet("""

            font-size:16px;
            color:green;

        """)

        self.date_input = QDateEdit(
            self
        )

        self.date_input.setDate(
            QDate.currentDate()
        )

        self.date_input.setCalendarPopup(
            True
        )

        self.date_input.setDisplayFormat(
            "dd-MM-yyyy"
        )

        self.date_input.setGeometry(
            230,
            130,
            200,
            35
        )

        # =========================
        # Upazila
        # =========================

        upazila_label = QLabel(
            "Upazila:",
            self
        )

        upazila_label.setGeometry(
            80,
            180,
            150,
            30
        )

        upazila_label.setStyleSheet("""

            font-size:16px;
            color:green;

        """)

        self.upazila_box = QComboBox(
            self
        )

        self.upazila_box.setGeometry(
            230,
            190,
            250,
            35
        )

        self.upazila_box.addItem(
            "-- উপজেলা নির্বাচন করুন --"
        )

        if self.zone_id == 1:

            self.upazila_box.addItems([

                "পঞ্চগড় উপজেলা",

                "তেতুলিয়া উপজেলা"

            ])


        elif self.zone_id == 2:

            self.upazila_box.addItems([

                "বোদা উপজেলা"

            ])


        elif self.zone_id == 3:

            self.upazila_box.addItems([

                "দেবীগঞ্জ উপজেলা"

            ])


        elif self.zone_id == 4:

            self.upazila_box.addItems([

                "আটোয়ারী উপজেলা"

            ])
        # =========================
        # Report Table
        # =========================

        print("Before Table Create")

        self.report_table = CustomReportTable(
            self
        )

        # =========================
        # Initial Date Header Update
        # =========================

        self.update_date_headers()



        print("After Table Create")

        self.report_table.setGeometry(
            30,
            280,
            1150,
            280
        )
        # Initial Date Header Update
        self.update_current_date_header()

        # =========================
        # Previous Day Auto Load
        # Signal Connection
        # =========================

        # self.date_input.dateChanged.connect(
        #     lambda _: self.load_previous_day_data()
        # )
        self.date_input.dateChanged.connect(
            lambda _: self.update_current_date_header()
        )

        self.date_input.dateChanged.connect(
            lambda _: self.update_previous_year_header()
        )

        self.date_input.dateChanged.connect(
            lambda _: self.update_previous_report_date_header()
        )

        self.upazila_box.currentTextChanged.connect(
            lambda _: self.load_previous_day_data()
        )

        self.upazila_box.currentTextChanged.connect(
            self.set_upazila_to_table
        )


        print("Auto Previous Day Signal Connected")
        # =========================
        # Save Button
        # =========================

        self.save_button = QPushButton(
            "Save Report",
            self
        )

        self.save_button.clicked.connect(
            self.save_report
        )

        print("Before Button Create")

        self.view_button = QPushButton(
            "View Data",
            self
        )

        print("After Button Create")

        self.view_button.setGeometry(
            300,
            610,
            180,
            45
        )

        self.view_button.clicked.connect(
            self.open_view_data
        )


        self.save_button.setGeometry(
            505,
            610,
            200,
            45
        )
        self.save_button.clicked.connect(
            self.save_report
        )

        # Auto Calculation

        self.report_table.cellChanged.connect(
            self.calculate_values
        )

    # =========================
    # Set Upazila Information
    # =========================

    def set_upazila_to_table(self):

        upazila_name = self.upazila_box.currentText()

        if upazila_name == "-- উপজেলা নির্বাচন করুন --":
            return

        # Serial No

        self.report_table.item(
            3,
            0
        ).setText(
            "1"
        )

        # Upazila Name

        self.report_table.item(
            3,
            1
        ).setText(
            upazila_name
        )

        print(
            "Upazila Set:",
            upazila_name
        )

    # =========================
    # Auto Calculation
    # =========================

    def convert_bangla_number(self, value):

        bangla_digits = {
            "০": "0",
            "১": "1",
            "২": "2",
            "৩": "3",
            "৪": "4",
            "৫": "5",
            "৬": "6",
            "৭": "7",
            "৮": "8",
            "৯": "9"
        }


        for bangla, english in bangla_digits.items():

            value = value.replace(
                bangla,
                english
            )


        return value

    # =========================
    # Update Date Headers
    # =========================

    def update_date_headers(self):

        current_date = self.date_input.date().toPyDate()

        # Current Date Header
        self.report_table.setHorizontalHeaderItem(
            21,
            QTableWidgetItem(
                current_date.strftime("%d.%m.%Y")
            )
        )

        print(
            "Current Header Date:",
            current_date
        )




    def load_previous_entry(self):

        dialog = PreviousEntryDialog(self)

        dialog.exec()

    # =========================
    # Open View Data
    # =========================

    def open_view_data(self):

        self.view_window = ViewDataDialog(
            self
        )

        self.view_window.show()

    def clear_entry_row(self):

        self.report_table.blockSignals(True)

        for column in range(28):

            item = self.report_table.item(
                3,
                column
            )

            if item:
                item.setText("")

        self.report_table.blockSignals(False)

    # =========================
    # Update Current Date Header
    # =========================

    def update_current_date_header(self):

        current_date = self.date_input.date().toPyDate()

        print(
            "HEADER UPDATE RUN:",
            current_date
        )

        item = self.report_table.item(
            1,
            21
        )

        if item:
            item.setText(
                current_date.strftime("%d.%m.%Y")
            )

    # =========================
    # Update Previous Year Date Header
    # =========================

    def update_previous_year_header(self):

        current_date = self.date_input.date().toPyDate()

        previous_year_date = current_date.replace(
            year=current_date.year - 1
        )

        print(
            "Previous Year Header:",
            previous_year_date
        )

        item = self.report_table.item(
            1,
            20
        )

        if item:
            item.setText(
                previous_year_date.strftime("%d.%m.%Y")
            )

    # =========================
    # Update Previous Report Date Header
    # =========================

    def update_previous_report_date_header(self):

        upazila_name = self.upazila_box.currentText()

        if upazila_name == "-- উপজেলা নির্বাচন করুন --":
            print(
                "Upazila Not Selected"
            )

            return

        print(
            "Previous Header Function Called"
        )

        current_date = self.date_input.date().toPyDate()

        print(
            "Current Date:",
            current_date
        )

        print(
            "Selected Upazila:",
            upazila_name
        )

        # Get Previous Report

        previous_report = self.get_previous_day_report()

        if previous_report:

            previous_date = previous_report.report_date

            print(
                "Found Previous Report:",
                previous_date
            )

            item = self.report_table.item(
                0,
                25
            )

            if item:
                item.setText(
                    previous_date.strftime("%d.%m.%Y")
                )

                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )

                print(
                    "Previous Header Updated Successfully"
                )

            print(
                "Previous Header Updated Successfully"
            )



        else:

            print(
                "No Previous Report"
            )

    # =========================
    # Auto Calculation Trigger
    # =========================

    def calculate_values(self, row, column):

        if row != 3:
            return

        self.calculate_all_values()

    # =========================
    # Get Previous Day Report
    # =========================

    def get_previous_day_report(self):

        try:

            # =========================
            # Current Report Date
            # =========================

            current_date = self.date_input.date().toPyDate()

            # =========================
            # Current Upazila
            # =========================

            upazila_name = self.upazila_box.currentText()

            if upazila_name == "-- উপজেলা নির্বাচন করুন --":
                return None

            # =========================
            # Find Upazila ID
            # =========================

            with Session(engine) as session:

                upazila = session.query(
                    Upazila
                ).filter(
                    Upazila.upazila_name == upazila_name
                ).first()

            if not upazila:
                return None

            # =========================
            # Find Latest Previous Report
            # Friday & Saturday Skip
            # =========================

            from datetime import timedelta

            search_date = current_date - timedelta(days=1)

            previous_report = None

            while search_date >= current_date - timedelta(days=30):

                # Friday = 4
                # Saturday = 5

                if search_date.weekday() not in [4, 5]:

                    with Session(engine) as session:

                        previous_report = session.query(
                            DailyReport
                        ).filter(

                            DailyReport.upazila_id == upazila.id,

                            DailyReport.report_date == search_date

                        ).first()

                    if previous_report:
                        break

                search_date -= timedelta(days=1)

            # =========================
            # Update Previous Date Header
            # =========================

            if previous_report:

                item = self.report_table.item(
                    0,
                    25
                )

                if item:
                    item.setText(
                        previous_report.report_date.strftime(
                            "%d.%m.%Y"
                        )
                    )

                print(
                    "Previous Report Found:",
                    previous_report.report_date
                )


            else:

                print(
                    "No Previous Report Found"
                )

            return previous_report



        except Exception as e:

            print(
                "Previous Report Error:",
                e
            )

            return None
    # =========================
    # Load Previous Day Data
    # =========================

    def load_previous_day_data(self):

        print(
            "Date Changed Event Fired"
        )
        try:

            # Check Upazila

            upazila_name = self.upazila_box.currentText()

            if upazila_name == "-- উপজেলা নির্বাচন করুন --":
                return

            # Current Date

            current_date = self.date_input.date().toPyDate()

            from datetime import timedelta

            previous_date = current_date - timedelta(days=1)

            print(
                "Current Date:",
                current_date
            )

            print(
                "Previous Date:",
                previous_date
            )

            # Find Upazila ID

            with Session(engine) as session:

                upazila = session.query(
                    Upazila
                ).filter(
                    Upazila.upazila_name == upazila_name
                ).first()

            if not upazila:
                print(
                    "Upazila Not Found"
                )

                return

            print(
                "Upazila ID:",
                upazila.id
            )

            # Search Previous Report

            with Session(engine) as session:

                previous_report = session.query(
                    DailyReport
                ).filter(

                    DailyReport.upazila_id == upazila.id,

                    DailyReport.report_date == previous_date

                ).first()

            if previous_report:

                print(
                    "Previous Report Found"
                )

                print(
                    "Report ID:",
                    previous_report.id
                )

                # =========================
                # Stop Table Signals
                # =========================

                self.report_table.blockSignals(True)

                try:

                    # =========================
                    # Deep Well
                    # =========================

                    self.report_table.item(
                        3, 2
                    ).setText(
                        str(previous_report.deep_well_new)
                    )

                    self.report_table.item(
                        3, 3
                    ).setText(
                        str(previous_report.deep_well_commission)
                    )

                    self.report_table.item(
                        3, 4
                    ).setText(
                        str(previous_report.deep_well_used)
                    )

                    # =========================
                    # LLP
                    # =========================

                    self.report_table.item(
                        3, 5
                    ).setText(
                        str(previous_report.llp_used)
                    )

                    self.report_table.item(
                        3, 6
                    ).setText(
                        str(previous_report.llp_commission)
                    )

                    # =========================
                    # Kharif-1
                    # =========================

                    self.report_table.item(
                        3, 7
                    ).setText(
                        str(previous_report.aus)
                    )

                    self.report_table.item(
                        3, 8
                    ).setText(
                        str(previous_report.aus_other)
                    )

                    # =========================
                    # Kharif-2
                    # =========================

                    self.report_table.item(
                        3, 9
                    ).setText(
                        str(previous_report.aman)
                    )

                    self.report_table.item(
                        3, 10
                    ).setText(
                        str(previous_report.aman_other)
                    )

                    # =========================
                    # Rabi
                    # =========================

                    self.report_table.item(
                        3, 11
                    ).setText(
                        str(previous_report.boro)
                    )

                    self.report_table.item(
                        3, 12
                    ).setText(
                        str(previous_report.maize)
                    )

                    self.report_table.item(
                        3, 13
                    ).setText(
                        str(previous_report.wheat)
                    )

                    self.report_table.item(
                        3, 14
                    ).setText(
                        str(previous_report.potato)
                    )

                    self.report_table.item(
                        3, 15
                    ).setText(
                        str(previous_report.mustard)
                    )

                    self.report_table.item(
                        3, 16
                    ).setText(
                        str(previous_report.lentil)
                    )

                    self.report_table.item(
                        3, 17
                    ).setText(
                        str(previous_report.other_crop)
                    )

                    # =========================
                    # Irrigation Charge
                    # Previous Values Carry Forward
                    # =========================

                    self.report_table.item(
                        3, 20
                    ).setText(
                        str(previous_report.previous_charge)
                    )

                    self.report_table.item(
                        3, 21
                    ).setText(
                        str(previous_report.current_charge)
                    )

                    self.report_table.item(
                        3, 22
                    ).setText(
                        str(previous_report.recharge)
                    )

                    # =========================
                    # Farmer Family
                    # =========================

                    self.report_table.item(
                        3, 27
                    ).setText(
                        str(previous_report.farmer_family)
                    )


                finally:

                    self.report_table.blockSignals(False)

                # =========================
                # Recalculate Auto Fields
                # =========================

                self.calculate_all_values()

                print(
                    "Previous Day Data Loaded Successfully"
                )


            else:

                print(
                    "No Previous Report Found"
                )



        except Exception as e:

            print(
                "Previous Load Error:",
                e
            )

    # =========================
    # Get Previous Day Total
    # =========================

    def get_previous_day_total(self):

        try:

            from datetime import timedelta

            # =========================
            # Current Report Date
            # =========================

            current_date = self.date_input.date().toPyDate()

            # =========================
            # Previous Date
            # =========================

            previous_date = current_date - timedelta(days=1)

            # =========================
            # Current Upazila
            # =========================

            upazila_name = self.upazila_box.currentText()

            if upazila_name == "-- উপজেলা নির্বাচন করুন --":
                return 0

            # =========================
            # Find Upazila
            # =========================

            with Session(engine) as session:

                upazila = session.query(
                    Upazila
                ).filter(
                    Upazila.upazila_name == upazila_name
                ).first()

            if not upazila:
                return 0

            # =========================
            # Find Previous Day Report
            # =========================

            with Session(engine) as session:

                previous_report = session.query(
                    DailyReport
                ).filter(

                    DailyReport.upazila_id == upazila.id,

                    DailyReport.report_date == previous_date

                ).first()

                if not previous_report:
                    print(
                        "Previous Day Report Not Found:",
                        previous_date
                    )

                    return 0

                # =========================
                # Previous Day Total
                # Current Charge + Recharge
                # =========================

                previous_current_charge = float(
                    previous_report.current_charge or 0
                )

                previous_recharge = float(
                    previous_report.recharge or 0
                )

                previous_total = (
                        previous_current_charge
                        +
                        previous_recharge
                )

            print(
                "Previous Date:",
                previous_date
            )

            print(
                "Previous Day Total:",
                previous_total
            )

            return previous_total


        except Exception as e:

            print(
                "Previous Day Total Error:",
                e
            )

            return 0
    # =========================
    # Calculate All Values
    # =========================

    def calculate_all_values(self):

        self.report_table.blockSignals(True)

        try:

            # =====================
            # Previous Day Total
            # =====================

            previous_day_total = self.get_previous_day_total()

            print(
                "Fetched Previous Total:",
                previous_day_total
            )
            # =========================
            # Set Previous Day Total
            # Column 25
            # =========================

            self.report_table.item(
                3,
                25
            ).setText(
                str(previous_day_total)
            )

            # =====================
            # Rabi Total
            # Column 18
            # =====================

            rabi_total = 0



            for col in range(11, 18):

                item = self.report_table.item(
                    3,
                    col
                )

                if item and item.text():
                    rabi_total += float(
                        self.convert_bangla_number(
                            item.text()
                        )
                    )

            self.report_table.item(
                3,
                18
            ).setText(
                str(rabi_total)
            )

            # =====================
            # Total Area
            # Column 19
            # =====================

            total_area = 0

            # Kharif-1

            for col in [7, 8]:

                item = self.report_table.item(
                    3,
                    col
                )

                if item and item.text():
                    total_area += float(
                        self.convert_bangla_number(
                            item.text()
                        )
                    )

            # Kharif-2

            for col in [9, 10]:

                item = self.report_table.item(
                    3,
                    col
                )

                if item and item.text():
                    total_area += float(
                        self.convert_bangla_number(
                            item.text()
                        )
                    )

            # Rabi Total Add

            total_area += rabi_total

            self.report_table.item(
                3,
                19
            ).setText(
                str(total_area)
            )

            # =====================
            # Charge Total
            # Column 23
            # =====================

            current_charge = 0

            recharge = 0

            item = self.report_table.item(
                3,
                21
            )

            if item and item.text():
                current_charge = float(
                    self.convert_bangla_number(
                        item.text()
                    )
                )

            item = self.report_table.item(
                3,
                22
            )

            if item and item.text():
                recharge = float(
                    self.convert_bangla_number(
                        item.text()
                    )
                )

            charge_total = (

                    current_charge

                    +

                    recharge

            )

            self.report_table.item(
                3,
                23
            ).setText(
                str(charge_total)
            )
            print(
                "Total Charge:",
                charge_total
            )

            # =====================
            # Growth
            # Column 26
            # =====================

            previous_total = 0

            item = self.report_table.item(
                3,
                25
            )

            if item and item.text():
                previous_total = float(
                    self.convert_bangla_number(
                        item.text()
                    )
                )

            growth = (
                    charge_total
                    -
                    previous_total
            )

            self.report_table.item(
                3,
                26
            ).setText(
                str(growth)
            )

            print(
                "Growth:",
                growth
            )

            # =====================
            # Percentage Difference
            # Column 24
            # =====================

            previous_year_charge = 0

            # Column 20
            item = self.report_table.item(
                3,
                20
            )

            if item and item.text():
                previous_year_charge = float(
                    self.convert_bangla_number(
                        item.text()
                    )
                )

            percentage = 0

            if previous_year_charge > 0:
                percentage = (
                                     (charge_total / previous_year_charge) * 100
                             ) - 100

            self.report_table.item(
                3,
                24
            ).setText(
                str(
                    round(
                        percentage,
                        2
                    )
                )
            )

            print(
                "Percentage Difference:",
                percentage
            )

        except Exception as e:

            print(
                "Calculation Error:",
                e
            )


        finally:

            self.report_table.blockSignals(False)

# =========================
    # Save Report
    # =========================

    def save_report(self):

        report_date = self.date_input.date().toPyDate()

        upazila = self.upazila_box.currentText()

        # =========================
        # Upazila Validation
        # =========================

        if upazila == "-- উপজেলা নির্বাচন করুন --":
            QMessageBox.warning(
                self,
                "Validation Error",
                "Please select Upazila."
            )

            return

        # =========================
        # Find Upazila ID
        # =========================

        with Session(engine) as session:

            upazila_obj = session.query(
                Upazila
            ).filter(
                Upazila.upazila_name == upazila
            ).first()

        if not upazila_obj:
            QMessageBox.warning(
                self,
                "Validation Error",
                "Upazila Not Found."
            )

            return

        upazila_id = upazila_obj.id

        # =========================
        # Duplicate Check
        # =========================

        with Session(engine) as session:


            existing_report = session.query(
                DailyReport
            ).filter(

                DailyReport.upazila_id == upazila_id,

                DailyReport.report_date == report_date

            ).first()

        if existing_report:
            QMessageBox.warning(
                self,
                "Duplicate Report",
                "This report already exists for this date."
            )

            return

        # =========================
        # Read Table Data
        # =========================

        row_data = []

        for column in range(28):

            item = self.report_table.item(
                3,
                column
            )

            if item and item.text():

                row_data.append(
                    item.text()
                )

            else:

                row_data.append(
                    "0"
                )

        print(row_data)

        # =========================
        # Validation
        # =========================

        numeric_columns = [

            2, 3, 4,

            5, 6,

            7, 8, 9, 10,

            11, 12, 13, 14, 15, 16, 17,

            20, 21, 22,

            27

        ]

        for col in numeric_columns:

            try:

                value = float(
                    self.convert_bangla_number(
                        row_data[col]
                    )
                )

                if value < 0:
                    QMessageBox.warning(
                        self,
                        "Validation Error",
                        "Negative value is not allowed."
                    )

                    return



            except ValueError:

                QMessageBox.warning(
                    self,
                    "Validation Error",
                    "Please enter valid number only."
                )

                return

        # =========================
        # Create Report Object
        # =========================

        report = DailyReport(

            upazila_id=upazila_id,

            report_date=report_date,

            # Deep Well

            deep_well_new=int(row_data[2]),

            deep_well_commission=int(row_data[3]),

            deep_well_used=int(row_data[4]),

            # LLP

            llp_used=int(row_data[5]),

            llp_commission=int(row_data[6]),

            # Crop

            # Crop

            aus=float(row_data[7]),

            aus_other=float(row_data[8]),

            aman=float(row_data[9]),

            aman_other=float(row_data[10]),

            boro=float(row_data[11]),

            maize=float(row_data[12]),

            wheat=float(row_data[13]),

            potato=float(row_data[14]),

            mustard=float(row_data[15]),

            lentil=float(row_data[16]),

            other_crop=float(row_data[17]),

            # Charge

            previous_charge=float(row_data[20]),

            current_charge=float(row_data[21]),

            recharge=float(row_data[22]),

            # Farmer

            farmer_family=int(row_data[27]),

            created_by=self.username,

            created_at=str(datetime.now()),

            updated_at=str(datetime.now())

        )

        # =========================
        # Save Database
        # =========================

        try:

            with Session(engine) as session:

                session.add(report)

                session.commit()

                saved_id = report.id

            print(
                "Report Saved ID:",
                saved_id
            )


        except Exception as e:

            print(
                "SAVE ERROR:",
                e
            )

            QMessageBox.warning(
                self,
                "Save Error",
                str(e)
            )

            return

        print("Before Success Popup")

        QMessageBox.information(
            self,
            "Success",
            "Report Saved Successfully"
        )

        print("After Success Popup")

        print("Before Clear Row")

        self.clear_entry_row()

        print("After Clear Row")
# =========================
# Test Run
# =========================


if __name__ == "__main__":


    app = QApplication(sys.argv)


    window = DataEntryWindow(

        "panch_tetulia_zone",

        1

    )


    window.show()


    sys.exit(
        app.exec()
    )