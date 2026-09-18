from database.connection import engine

from sqlalchemy.orm import Session

from models.daily_report import DailyReport

from models.upazila import Upazila



print("Database Checking Started")


with Session(engine) as session:


    # =========================
    # Check All Reports
    # =========================

    reports = session.query(
        DailyReport
    ).order_by(
        DailyReport.report_date
    ).all()


    print("\n===== ALL REPORTS =====")


    for report in reports:

        print(
            "ID:",
            report.id,
            "| Date:",
            report.report_date,
            "| Upazila ID:",
            report.upazila_id,
            "| Current Charge:",
            report.current_charge,
            "| Recharge:",
            report.recharge
        )


    print(
        "\nTotal Reports:",
        len(reports)
    )



    # =========================
    # Check Previous Year Date
    # =========================

    print("\n===== CHECK 2025-09-02 =====")


    check_report = session.query(
        DailyReport
    ).filter(

        DailyReport.report_date ==
        "2025-09-02"

    ).all()



    for r in check_report:

        print(
            "FOUND:",
            r.id,
            r.report_date,
            r.upazila_id,
            r.current_charge,
            r.recharge
        )


    if len(check_report) == 0:

        print(
            "NO DATA FOUND FOR 2025-09-02"
        )