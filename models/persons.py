import uuid
from datetime import date
from sqlalchemy import Column, String, Date, Numeric
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base

class Person(Base):
    __tablename__ = "cd_persons"
    __table_args__ = {"schema": "common", "comment": "физлица"}
    
    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: str = Column(String(500), name="c_name", nullable=False, comment="имя")
    email: str = Column(String(500), name="c_email", nullable=False, comment="email")
    phone: str = Column(String(500), name="c_phone", comment="телефон")
    # birth_date: date = Column(Date, name="d_birth_date", nullable=False, comment="дата рождения")
    # department: str = Column(String(500), name="c_department", nullable=False, comment="подразделение")
    # salary: float = Column(Numeric(10, 2), name="n_salary", nullable=False, comment="зарплата")
