from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

# Database connection
DATABASE_URI = "mysql+pymysql://root:system@localhost/violations_db"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define SQLAlchemy models
class Driver(Base):
    __tablename__ = 'drivers'
    driver_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    license_number = Column(String(20), unique=True)
    contact = Column(String(15))

class Vehicle(Base):
    __tablename__ = 'vehicles'
    vehicle_id = Column(String(20), primary_key=True)
    type = Column(String(50))
    owner_id = Column(Integer, ForeignKey('drivers.driver_id'))
    make = Column(String(50))
    model = Column(String(50))

class Violation(Base):
    __tablename__ = 'violations'
    violation_code = Column(String(10), primary_key=True)
    description = Column(String(255))
    fine_amount = Column(Float)

class Challan(Base):
    __tablename__ = 'challans'
    challan_id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(Integer, ForeignKey('drivers.driver_id'))
    vehicle_id = Column(String(20), ForeignKey('vehicles.vehicle_id'))
    violation_code = Column(String(10), ForeignKey('violations.violation_code'))
    issue_date = Column(Date)
    location = Column(String(100))
    paid = Column(Boolean, default=False)

# Create tables (run once)
Base.metadata.create_all(engine)