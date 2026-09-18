from PyQt6.QtWidgets import (
    QTableWidget,
    QHeaderView,
    QTableWidgetItem
)

from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class CustomReportTable(QTableWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        # Total Column
        self.setColumnCount(28)

        # Header + Data Row
        self.setRowCount(4)


        self.setup_font()

        self.setup_style()

        self.setup_headers()

        self.merge_headers()

        self.format_headers()

        self.set_editable_cells()



    # =========================
    # Font
    # =========================

    def setup_font(self):

        self.setFont(
            QFont("NikoshBAN", 12)
        )



    # =========================
    # Style
    # =========================

    def setup_style(self):

        self.setStyleSheet("""

        QTableWidget {

            border: 1px solid green;

            gridline-color: green;

        }


        QTableWidget::item {

            border: 1px solid green;

        }


        QHeaderView::section {

            background-color: #d9ead3;

            font-family: NikoshBAN;

            font-size: 12px;

            font-weight: bold;

            border: 1px solid green;

        }

        """)


        # Hide default column numbers

        self.horizontalHeader().setVisible(False)


        # Enable Word Wrap

        self.setWordWrap(True)

        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Fixed
        )



    # =========================
    # Add Header
    # =========================

    def add_header(self, row, col, text):

        item = QTableWidgetItem(text)


        item.setTextAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        self.setItem(
            row,
            col,
            item
        )



    # =========================
    # Header Text
    # =========================

    def setup_headers(self):


        # Fixed Column

        self.add_header(
            0,
            0,
            "ক্রমিক নং"
        )


        self.add_header(
            0,
            1,
            "জোনের নাম"
        )



        # =========================
        # Deep Tube Well
        # =========================

        self.add_header(
            0,
            2,
            "মোট গভীর নলকূপ"
        )


        self.add_header(
            1,
            2,
            "খনন"
        )


        self.add_header(
            1,
            3,
            "কমিশন"
        )


        self.add_header(
            1,
            4,
            "ব্যবহার"
        )



        # =========================
        # LLP
        # =========================

        self.add_header(
            0,
            5,
            "এলএলপি"
        )


        self.add_header(
            1,
            5,
            "ব্যবহার"
        )


        self.add_header(
            1,
            6,
            "কমিশন"
        )



        # =========================
        # Irrigated Area
        # =========================

        self.add_header(
            0,
            7,
            "সেচকৃত এলাকা (হেক্টর)"
        )


        self.add_header(
            1,
            7,
            "খরিপ-১"
        )


        self.add_header(
            1,
            9,
            "খরিপ-২"
        )


        self.add_header(
            1,
            11,
            "রবি"
        )



        crop_headers = {

            7: "আউশ",
            8: "অন্যান্য",

            9: "আমন",
            10: "অন্যান্য",

            11: "বোরো",
            12: "ভুট্টা",
            13: "গম",
            14: "আলু",
            15: "সরিষা",
            16: "মসুর",
            17: "অন্যান্য",
            18: "মোট"

        }


        for col, text in crop_headers.items():

            self.add_header(
                2,
                col,
                text
            )



        # Total Area

        self.add_header(
            0,
            19,
            "সর্বমোট (হেক্টর)"
        )



        # =========================
        # Irrigation Charge
        # =========================

        self.add_header(
            0,
            20,
            "আদায়কৃত সেচচার্জ (টাকা)"
        )


        self.add_header(
            1,
            20,
            "০২.০৯.২৫"
        )


        self.add_header(
            1,
            21,
            "০২.০৯.২০২৬"
        )


        self.add_header(
            2,
            21,
            "মানি রশিদ"
        )


        self.add_header(
            2,
            22,
            "রিচার্জ"
        )


        self.add_header(
            2,
            23,
            "মোট"
        )



        # =========================
        # Other Columns
        # =========================

        self.add_header(
            0,
            24,
            "পার্থক্যের শতকরা হার (%)"
        )


        self.add_header(
            0,
            25,
            "০১.০৯.২০২৬"
        )


        self.add_header(
            0,
            26,
            "বৃদ্ধি"
        )


        self.add_header(
            0,
            27,
            "উপকৃত কৃষক পরিবার"
        )

    # =========================
    # Merge Header
    # =========================

    def merge_headers(self):


        # Fixed Column

        self.setSpan(
            0,0,
            3,1
        )


        self.setSpan(
            0,1,
            3,1
        )



        # =========================
        # Deep Tube Well
        # =========================

        self.setSpan(
            0,2,
            1,3
        )


        self.setSpan(
            1,2,
            2,1
        )


        self.setSpan(
            1,3,
            2,1
        )


        self.setSpan(
            1,4,
            2,1
        )



        # =========================
        # LLP
        # =========================

        self.setSpan(
            0,5,
            1,2
        )


        self.setSpan(
            1,5,
            2,1
        )


        self.setSpan(
            1,6,
            2,1
        )



        # =========================
        # Crop Area
        # =========================

        self.setSpan(
            0,7,
            1,12
        )


        self.setSpan(
            1,7,
            1,2
        )


        self.setSpan(
            1,9,
            1,2
        )


        self.setSpan(
            1,11,
            1,8
        )



        # Total Area

        self.setSpan(
            0,19,
            3,1
        )



        # =========================
        # Irrigation Charge
        # =========================

        self.setSpan(
            0,20,
            1,4
        )


        # ০২.০৯.২৫

        self.setSpan(
            1,20,
            2,1
        )


        # ০২.০৯.২০২৬

        self.setSpan(
            1,21,
            1,3
        )



        # =========================
        # Other Columns
        # =========================

        self.setSpan(
            0,24,
            3,1
        )


        self.setSpan(
            0,25,
            3,1
        )


        self.setSpan(
            0,26,
            3,1
        )


        self.setSpan(
            0,27,
            3,1
        )



    # =========================
    # Format Header
    # =========================

    def format_headers(self):


        self.verticalHeader().setVisible(False)



        # Row Height

        self.setRowHeight(
            0,
            45
        )


        self.setRowHeight(
            1,
            55
        )


        self.setRowHeight(
            2,
            45
        )

        # =========================
        # Data Row Height
        # =========================

        for row in range(
                self.rowCount()
        ):
            self.setRowHeight(
                row,
                60
            )

        # =========================
        # Cell Alignment
        # =========================

        for row in range(
                self.rowCount()
        ):

            for col in range(
                    self.columnCount()
            ):

                item = self.item(
                    row,
                    col
                )

                if item:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignHCenter |
                        Qt.AlignmentFlag.AlignVCenter
                    )
        # Column Width
        print("CUSTOM TABLE WIDTH LOADED")
        widths = {

            0: 60,
            1: 120,

            2: 70,
            3: 70,
            4: 70,

            5: 70,
            6: 70,

            7: 70,
            8: 70,

            9: 70,
            10: 70,

            11: 70,
            12: 70,
            13: 70,
            14: 70,
            15: 70,
            16: 70,
            17: 70,

            18: 80,

            19: 110,

            # =========================
            # Irrigation Charge
            # =========================

            20: 140,  # Previous Year Date

            21: 120,  # Current Date / Money Receipt

            22: 120,  # Recharge

            23: 120,  # Total

            24: 110,  # Percentage Difference

            25: 140,  # Previous Day Date

            26: 120,  # Growth

            27: 90  # Farmer Family
        }

        for col, width in widths.items():
            self.setColumnWidth(
                col,
                width
            )


    # =========================
    # Editable Cells
    # =========================

    def set_editable_cells(self):

        editable_columns = [

            # =====================
            # Deep Well
            # =====================

            2,  # Deep Well New
            3,  # Deep Well Commission
            4,  # Deep Well Used

            # =====================
            # LLP
            # =====================

            5,  # LLP Used
            6,  # LLP Commission

            # =====================
            # Crop Area
            # =====================

            7, 8,  # Aus
            9, 10,  # Aman

            11, 12, 13,
            14, 15, 16, 17,  # Rabi Crops

            # =====================
            # Irrigation Charge
            # =====================

            20,  # Previous Year Same Date Charge ✅

            21,  # Current Money Receipt

            22,  # Recharge

            # =====================
            # Farmer Family
            # =====================

            27

        ]

        for col in range(28):

            item = QTableWidgetItem("")

            if col in editable_columns:

                item.setFlags(

                    Qt.ItemFlag.ItemIsSelectable |

                    Qt.ItemFlag.ItemIsEditable |

                    Qt.ItemFlag.ItemIsEnabled

                )

                item.setBackground(
                    Qt.GlobalColor.white
                )


            else:

                item.setFlags(

                    Qt.ItemFlag.ItemIsSelectable |

                    Qt.ItemFlag.ItemIsEnabled

                )

            item.setTextAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            self.setItem(
                3,
                col,
                item
            )