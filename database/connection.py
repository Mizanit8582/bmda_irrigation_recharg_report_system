from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


DATABASE_URL = (
    "postgresql://postgres:1234@localhost:5432/irrigation_report_db"
)


engine = create_engine(DATABASE_URL)

Base = declarative_base()


try:
    connection = engine.connect()
    print("Database Connected Successfully")
    connection.close()

except Exception as e:
    print("Database Connection Failed")
    print(e)