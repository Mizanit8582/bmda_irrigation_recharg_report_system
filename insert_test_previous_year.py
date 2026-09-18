from database.connection import engine

from sqlalchemy.orm import Session

from models.daily_report import DailyReport

from models.upazila import Upazila
from datetime import date



print("Insert Test Previous Year Started")


test_report = DailyReport(

    upazila_id=1,

    report_date="2025-09-02",


    # Deep Well

    deep_well_new=50,

    deep_well_commission=50,

    deep_well_used=45,


    # LLP

    llp_used=3,

    llp_commission=2,


    # Crop

    aus=100,

    aus_other=20,

    aman=500,

    aman_other=50,

    boro=200,

    maize=30,

    wheat=40,

    potato=20,

    mustard=10,

    lentil=5,

    other_crop=5,


    # Charge

    previous_charge=0,

    current_charge=0,

    recharge=50000,


    # Farmer

    farmer_family=2000,


    created_by="TEST",

    created_at="2025-09-02",

    updated_at="2025-09-02"

)


with Session(engine) as session:

    session.add(test_report)

    session.commit()


    print(
        "Inserted ID:",
        test_report.id
    )


print(
    "Test Previous Year Report Insert Complete"
)