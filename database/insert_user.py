from database.connection import engine
from models.zone import Zone
from models.user import User
from sqlalchemy.orm import Session


with Session(engine) as session:

    users = [
        User(
            username="admin",
            password="1234",
            role="Regional Admin",
            zone_id=None
        ),

        User(
            username="panch_tetulia_zone",
            password="1234",
            role="Zone User",
            zone_id=1
        ),

        User(
            username="boda_zone",
            password="1234",
            role="Zone User",
            zone_id=2
        ),

        User(
            username="debigonj_zone",
            password="1234",
            role="Zone User",
            zone_id=3
        ),

        User(
            username="atwari_zone",
            password="1234",
            role="Zone User",
            zone_id=4
        ),
    ]

    session.add_all(users)
    session.commit()


print("User Data Inserted Successfully")