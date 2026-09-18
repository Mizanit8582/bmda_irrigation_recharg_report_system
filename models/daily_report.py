from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from database.connection import Base


class DailyReport(Base):

    __tablename__ = "daily_reports"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # Upazila Information

    upazila_id = Column(
        Integer,
        ForeignKey("upazilas.id"),
        nullable=False
    )


    # Report Date

    report_date = Column(
        Date,
        nullable=False
    )


    # Deep Tube Well
    # Deep Tube Well

    deep_well_new = Column(Integer, default=0)

    deep_well_commission = Column(Integer, default=0)

    deep_well_used = Column(Integer, default=0)


    # LLP
    llp_used = Column(Integer, default=0)

    llp_commission = Column(Integer, default=0)


    # Irrigated Area (Hectare)

    # Irrigated Area (Hectare)

    aus = Column(
        Float,
        default=0
    )

    aus_other = Column(
        Float,
        default=0
    )

    aman = Column(
        Float,
        default=0
    )

    aman_other = Column(
        Float,
        default=0
    )

    boro = Column(Float, default=0)

    maize = Column(Float, default=0)

    wheat = Column(Float, default=0)

    potato = Column(Float, default=0)

    mustard = Column(Float, default=0)

    lentil = Column(Float, default=0)

    other_crop = Column(Float, default=0)


    # Irrigation Charge

    previous_charge = Column(Float, default=0)

    current_charge = Column(Float, default=0)

    recharge = Column(Float, default=0)


    # Farmer Family

    farmer_family = Column(Integer, default=0)


    # Created Information

    created_by = Column(String(100))

    created_at = Column(String(100))

    updated_at = Column(String(100))