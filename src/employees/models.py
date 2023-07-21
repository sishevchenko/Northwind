from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import SmallInteger, String, DATE, TEXT, LargeBinary

from src.db import BaseMeta


class Employees(BaseMeta):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=10), nullable=False)
    title: Mapped[str] = mapped_column(String(length=30), nullable=True)
    title_of_courtesy: Mapped[str] = mapped_column(String(length=25), nullable=True)
    birth_date: Mapped[date] = mapped_column(DATE, nullable=True)
    hire_date: Mapped[date] = mapped_column(DATE, nullable=True)
    address: Mapped[str] = mapped_column(String(length=60), nullable=True)
    city: Mapped[str] = mapped_column(String(length=15), nullable=True)
    region: Mapped[str] = mapped_column(String(length=15), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(length=10), nullable=True)
    country: Mapped[str] = mapped_column(String(length=15), nullable=True)
    home_phone: Mapped[str] = mapped_column(String(length=24), nullable=True)
    extension: Mapped[str] = mapped_column(String(length=4), nullable=True)
    photo: Mapped[bytes] = mapped_column(LargeBinary, nullable=True)
    notes: Mapped[str] = mapped_column(TEXT, nullable=True)
    reports_to: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    photo_path: Mapped[str] = mapped_column(String(length=255), nullable=True)


# --
# -- Name: employee_territories; Type: TABLE; Schema: public; Owner: -; Tablespace:
# --
#
# CREATE TABLE employee_territories (
#     employee_id smallint NOT NULL,
#     territory_id character varying(20) NOT NULL
# );
