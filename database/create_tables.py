from database.connection import engine, Base
from models.zone import Zone
from models.upazila import Upazila
from models.user import User
from models.daily_report import DailyReport

Base.metadata.create_all(bind=engine)


print("All Tables Created Successfully")


print(
    Base.metadata.tables.keys()
)