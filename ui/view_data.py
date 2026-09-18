from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QDateEdit,
    QComboBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

from PyQt6.QtCore import QDate, Qt

from sqlalchemy.orm import Session

from database.connection import engine

from models.daily_report import DailyReport
from models.upazila import Upazila
from ui.custom_table import CustomReportTable
from PyQt6.QtGui import QFont



class ViewDataDialog(QDialog):


    def __init__(self, parent=None):

        super().__init__(parent)


        self.setWindowTitle(
            "View Report Data"
        )


        self.setGeometry(
            200,
            100,
            1100,
            600
        )


        self.create_ui()



    # =========================
    # UI
    # =========================

    def create_ui(self):


        title = QLabel(
            "View Report Data",
            self
        )


        title.setGeometry(
            400,
            20,
            300,
            40
        )


        title.setStyleSheet(
            """
            font-size:24px;
            font-weight:bold;
            color:green;
            """
        )



        # =========================
        # From Date
        # =========================


        from_label = QLabel(
            "From Date:",
            self
        )


        from_label.setGeometry(
            50,
            90,
            100,
            30
        )


        self.from_date = QDateEdit(
            self
        )


        self.from_date.setDate(
            QDate.currentDate()
        )


        self.from_date.setCalendarPopup(
            True
        )


        self.from_date.setDisplayFormat(
            "dd-MM-yyyy"
        )


        self.from_date.setGeometry(
            150,
            90,
            180,
            35
        )



        # =========================
        # To Date
        # =========================


        to_label = QLabel(
            "To Date:",
            self
        )


        to_label.setGeometry(
            380,
            90,
            100,
            30
        )


        self.to_date = QDateEdit(
            self
        )


        self.to_date.setDate(
            QDate.currentDate()
        )


        self.to_date.setCalendarPopup(
            True
        )


        self.to_date.setDisplayFormat(
            "dd-MM-yyyy"
        )


        self.to_date.setGeometry(
            470,
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
            720,
            90,
            100,
            30
        )


        self.upazila_box = QComboBox(
            self
        )


        self.upazila_box.setGeometry(
            800,
            90,
            220,
            35
        )


        self.upazila_box.addItems([

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
            "Search",
            self
        )


        self.search_button.setGeometry(
            470,
            150,
            150,
            40
        )


        self.search_button.clicked.connect(
            self.search_report
        )

        # =========================
        # Get Previous Year Charge
        # =========================





        # =========================
        # Table
        # =========================

        self.table = QTableWidget(
            self
        )

        # =========================
        # Table Style
        # =========================

        self.table.setStyleSheet(
            """

           QTableWidget
            {
                gridline-color: green;
                font-family: "Nirmala UI";
                font-size: 12px;
            }


            QHeaderView::section
            {
                background-color: #cae0e2;
                color: black;
                font-family: "Nirmala UI";
                font-size: 11px;
                font-weight: bold;
                border: 1px solid green;
                padding: 5px;
            }


            QTableWidget::item
            {
                border: 1px solid green;
                padding: 5px;
            }

            """
        )
        # =========================
        # Row Height
        # =========================

        self.table.verticalHeader().setDefaultSectionSize(
            45
        )

        # =========================
        # Table Font Fix
        # =========================

        table_font = QFont(
            "Nirmala UI",
            11
        )

        self.table.setFont(
            table_font
        )
        self.table.setGeometry(
            50,
            220,
            1000,
            280
        )
        # =========================
        # View Data Header
        # =========================

        headers = [

            "ক্রমিক\nনং",

            "তারিখ",

            "উপজেলা",

            "গভীর নলকূপ\nকমিশন",

            "গভীর নলকূপ\nকমিশন",

            "গভীর নলকূপ\nব্যবহার",

            "LLP\nব্যবহার",

            "LLP\nকমিশন",

            "আউশ",

            "অন্যান্য\n(আউশ)",

            "আমন",

            "অন্যান্য\n(আমন)",

            "বোরো",

            "ভুট্টা",

            "গম",

            "আলু",

            "সরিষা",

            "মসুর",

            "অন্যান্য\nফসল",

            "মোট\nএলাকা",

            "মানি রশিদ এ \nআদায়",

            "রিচার্জ",

            "মোট\nসেচচার্জ",

            "গত বছরের\nসেচচার্জ",

            "পার্থক্য",

            "উপকৃত কৃষক \nপরিবার"

        ]

        self.table.setColumnCount(
            len(headers)
        )

        self.table.setHorizontalHeaderLabels(
            headers
        )

        self.table.horizontalHeader().setDefaultSectionSize(
            120
        )

        self.table.horizontalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # =========================
        # Header Font
        # =========================

        header_font = QFont(
            "Nirmala UI",
            9
        )

        header_font.setBold(
            True
        )

        self.table.horizontalHeader().setFont(
            header_font
        )
        # =========================
        # Header Height
        # =========================

        self.table.horizontalHeader().setMinimumHeight(
            70
        )
        # =========================
        # Column Width Setting
        # =========================

        header = self.table.horizontalHeader()

        # Serial No
        self.table.setColumnWidth(
            0,
            60
        )

        # Date
        self.table.setColumnWidth(
            1,
            100
        )

        # Upazila
        self.table.setColumnWidth(
            2,
            140
        )

        # Numeric Columns
        for col in range(3, 19):
            self.table.setColumnWidth(
                col,
                90
            )

        # Total Area
        self.table.setColumnWidth(
            19,
            100
        )

        # Charge Columns
        for col in range(20, 25):
            self.table.setColumnWidth(
                col,
                120
            )

        # Farmer Family
        self.table.setColumnWidth(
            25,
            120
        )
        # =========================
        # Report Table
        # =========================

        # headers = [
        #
        #     "Date",
        #
        #     "Upazila",
        #
        #     "Deep Well New",
        #
        #     "Deep Well Commission",
        #
        #     "Deep Well Used",
        #
        #     "LLP Used",
        #
        #     "LLP Commission",
        #
        #     "AUS",
        #
        #     "AUS Other",
        #
        #     "Aman",
        #
        #     "Aman Other",
        #
        #     "Boro",
        #
        #     "Maize",
        #
        #     "Wheat",
        #
        #     "Potato",
        #
        #     "Mustard",
        #
        #     "Lentil",
        #
        #     "Other Crop",
        #
        #     "Previous Charge",
        #
        #     "Current Charge",
        #
        #     "Recharge",
        #
        #     "Total Charge",
        #
        #     "Farmer Family"
        #
        # ]
        #
        # self.table.setColumnCount(
        #     len(headers)
        # )
        #
        # self.table.setHorizontalHeaderLabels(
        #     headers
        # )
        #
        # self.table.horizontalHeader().setDefaultSectionSize(
        #     120
        # )
        # self.table.horizontalHeader().setDefaultAlignment(
        #     Qt.AlignmentFlag.AlignCenter
        # )

    # =========================
    # Get Previous Year Charge
    # =========================

    def get_previous_year_charge(
            self,
            report_date,
            upazila_id
    ):

        try:

            print(
                "Inside Previous Year Function"
            )


            previous_year_date = report_date.replace(
                year=report_date.year - 1
            )


            print(
                "Searching Previous Date:",
                previous_year_date
            )


            with Session(engine) as session:

                previous_report = session.query(
                    DailyReport
                ).filter(

                    DailyReport.upazila_id == upazila_id,

                    DailyReport.report_date == previous_year_date

                ).first()


            if previous_report:

                previous_charge = (

                    float(
                        previous_report.current_charge or 0
                    )

                    +

                    float(
                        previous_report.recharge or 0
                    )

                )

                print(
                    "Previous Year Charge:",
                    previous_charge
                )

                return previous_charge


            else:

                print(
                    "Previous Year Report Not Found"
                )

                return 0


        except Exception as e:

            print(
                "Previous Year Charge Error:",
                e
            )

            return 0

    # =========================
    # Search Report
    # =========================

    def search_report(self):

        start_date = (
            self.from_date
            .date()
            .toPyDate()
        )

        end_date = (
            self.to_date
            .date()
            .toPyDate()
        )

        upazila_name = (
            self.upazila_box
            .currentText()
        )

        if upazila_name == "-- উপজেলা নির্বাচন করুন --":
            QMessageBox.warning(

                self,

                "Search Error",

                "Please Select Upazila"

            )

            return

        with Session(engine) as session:

            upazila = session.query(
                Upazila
            ).filter(
                Upazila.upazila_name ==
                upazila_name
            ).first()

            if not upazila:
                QMessageBox.warning(

                    self,

                    "Error",

                    "Upazila Not Found"

                )

                return

            reports = session.query(
                DailyReport
            ).filter(

                DailyReport.upazila_id ==
                upazila.id,

                DailyReport.report_date >=
                start_date,

                DailyReport.report_date <=
                end_date

            ).order_by(

                DailyReport.report_date

            ).all()

        print(
            "Total Reports Found:",
            len(reports)
        )

        # Clear Previous Data

        self.table.clearContents()

        self.table.setRowCount(
            len(reports)
        )

        print(
            "Table Rows Created:",
            self.table.rowCount()
        )

        print(
            "Table Columns:",
            self.table.columnCount()
        )

        for index, report in enumerate(reports):

            row = index

            # =========================
            # Previous Year Charge Test
            # =========================

            previous_year_charge = report.previous_charge

            print(
                "Loaded Previous Year Charge:",
                previous_year_charge
            )

            # =========================
            # Difference Calculation
            # =========================

            total_charge = (

                    float(report.current_charge or 0)

                    +

                    float(report.recharge or 0)

            )

            difference = (

                    total_charge

                    -

                    previous_year_charge

            )

            #==============
            #[VALUE]
            # ==============
            print(
                "TEST NUMBER:",
                self.convert_to_bangla_number(12345)
            )
            values = [

                str(index + 1),  # 0 ক্রমিক নং

                self.convert_date_bangla(
                    report.report_date
                ),  # 1 তারিখ

                upazila_name,  # 2 উপজেলা

                self.convert_to_bangla_number(
                    report.deep_well_new
                ),

                self.convert_to_bangla_number(
                    report.deep_well_commission
                ),

                self.convert_to_bangla_number(
                    report.deep_well_used
                ),

                self.convert_to_bangla_number(
                    report.llp_used
                ),

                self.convert_to_bangla_number(
                    report.llp_commission
                ),
                self.convert_to_bangla_number(
                    report.aus
                ),

                self.convert_to_bangla_number(
                    report.aus_other
                ),

                self.convert_to_bangla_number(
                    report.aman
                ),

                self.convert_to_bangla_number(
                    report.aman_other
                ),

                self.convert_to_bangla_number(
                    report.boro
                ),

                self.convert_to_bangla_number(
                    report.maize
                ),

                self.convert_to_bangla_number(
                    report.wheat
                ),

                self.convert_to_bangla_number(
                    report.potato
                ),

                self.convert_to_bangla_number(
                    report.mustard
                ),

                self.convert_to_bangla_number(
                    report.lentil
                ),

                self.convert_to_bangla_number(
                    report.other_crop
                ),

                self.convert_to_bangla_number(

                    float(
                        report.aus or 0
                    )

                    +

                    float(
                        report.aus_other or 0
                    )

                    +

                    float(
                        report.aman or 0
                    )

                    +

                    float(
                        report.aman_other or 0
                    )

                    +

                    float(
                        report.boro or 0
                    )

                    +

                    float(
                        report.maize or 0
                    )

                    +

                    float(
                        report.wheat or 0
                    )

                    +

                    float(
                        report.potato or 0
                    )

                    +

                    float(
                        report.mustard or 0
                    )

                    +

                    float(
                        report.lentil or 0
                    )

                    +

                    float(
                        report.other_crop or 0
                    )

                ),  # 19 মোট এলাকা

                self.convert_to_bangla_number(
                    report.current_charge
                ),

                self.convert_to_bangla_number(
                    report.recharge
                ),

                self.convert_to_bangla_number(
                    self.clean_number(
                        total_charge
                    )
                ),

                self.convert_to_bangla_number(
                    self.clean_number(
                        previous_year_charge
                    )
                ),

                self.convert_to_bangla_number(
                    self.clean_number(
                        difference
                    )
                ),

                self.convert_to_bangla_number(
                    report.farmer_family
                ),  # 25 কৃষক পরিবার

            ]

            # =========================
            # Insert Data Into Table
            # =========================

            for col, value in enumerate(values):
                item = QTableWidgetItem(
                    value
                )

                item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )

                self.table.setItem(

                    row,

                    col,

                    item

                )
    # =========================
    # Convert English Number
    # To Bangla Number
    # =========================

    def convert_to_bangla_number(
        self,
        value
    ):

        english = "0123456789"

        bangla = "০১২৩৪৫৬৭৮৯"

        translation = str.maketrans(
            english,
            bangla
        )

        return str(value).translate(
            translation
        )
    # =========================
    # Remove Decimal
    # =========================

    def clean_number(
        self,
        value
    ):

        try:

            number = float(value)

            if number.is_integer():

                return int(number)

            else:

                return round(
                    number,
                    2
                )


        except:

            return value
    # =========================
    # Date Bangla Format
    # =========================

    def convert_date_bangla(
        self,
        date_value
    ):

        date_text = date_value.strftime(
            "%d-%m-%Y"
        )


        return self.convert_to_bangla_number(
            date_text
        )