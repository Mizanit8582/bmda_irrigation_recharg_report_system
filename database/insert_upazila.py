from database.connection import engine
from models.zone import Zone
from models.upazila import Upazila
from sqlalchemy.orm import Session

with Session(engine) as session:

    upazilas = [
        Upazila(zone_id=1, upazila_name="পঞ্চগড় উপজেলা"),
        Upazila(zone_id=1, upazila_name="তেতুলিয়া উপজেলা"),
        Upazila(zone_id=2, upazila_name="বোদা উপজেলা"),
        Upazila(zone_id=3, upazila_name="দেবীগঞ্জ উপজেলা"),
        Upazila(zone_id=4, upazila_name="আটোয়ারী উপজেলা"),
    ]

    session.add_all(upazilas)
    session.commit()


print("Upazila Data Inserted Successfully")