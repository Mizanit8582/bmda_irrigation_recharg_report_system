from database.connection import engine

from sqlalchemy.orm import Session

from models.daily_report import DailyReport

from models.upazila import Upazila


print("Delete Test Data Started")


with Session(engine) as session:


    report = session.query(
        DailyReport
    ).filter(

        DailyReport.id == 4

    ).first()



    if report:

        session.delete(report)

        session.commit()


        print(
            "Test Data Deleted Successfully"
        )


    else:

        print(
            "Test Data Not Found"
        )