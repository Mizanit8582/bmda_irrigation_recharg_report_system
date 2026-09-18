from database.connection import engine
from models.zone import Zone
from sqlalchemy.orm import Session


with Session(engine) as session:

    zones = [
        Zone(zone_name="Zone-1"),
        Zone(zone_name="Zone-2"),
        Zone(zone_name="Zone-3"),
        Zone(zone_name="Zone-4"),
    ]

    session.add_all(zones)
    session.commit()


print("Zone Data Inserted Successfully")