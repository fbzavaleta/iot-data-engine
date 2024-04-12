from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""


class Models:
    Base = declarative_base()

    class EngineEndpoint(Base):
        __tablename__ = "engine_endpoint"
        id = Column(Integer, primary_key=True)
        channel = Column(String(255), nullable=False, unique=True)
        token = Column(String(255), nullable=False)
        is_active = Column(Boolean, nullable=False, default=True)

    class EngineEndpointDescription(Base):
        __tablename__ = "engine_endpoint_description"
        id = Column(Integer, primary_key=True, autoincrement=True)
        engine_endpoint_id = Column(
            Integer, ForeignKey("engine_endpoint.id"), nullable=False
        )
        channel_name = Column(String(255), nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        elevation = Column(String, nullable=True)
        last_row = Column(Integer, nullable=True)

    class EngineEndpointDescriptionField(Base):
        __tablename__ = "engine_endpoint_description_fields"
        id = Column(Integer, primary_key=True, autoincrement=True)
        engine_endpoint_description_id = Column(
            Integer, ForeignKey("engine_endpoint_description.id"), nullable=False
        )
        field1_name = Column(String(255), nullable=True)
        field2_name = Column(String(255), nullable=True)
        field3_name = Column(String(255), nullable=True)
        field4_name = Column(String(255), nullable=True)
        field5_name = Column(String(255), nullable=True)
        field6_name = Column(String(255), nullable=True)
        field7_name = Column(String(255), nullable=True)
        field8_name = Column(String(255), nullable=True)

    class EngineDataSample(Base):
        __tablename__ = "engine_data_sample"
        id = Column(Integer, primary_key=True)
        engine_endpoint_id = Column(
            Integer, ForeignKey("engine_endpoint.id"), nullable=False
        )
        entry_id = Column(Integer, nullable=False)
        created_at = Column(DateTime, nullable=False)
        field1 = Column(Float, nullable=True)
        field2 = Column(Float, nullable=True)
        field3 = Column(Float, nullable=True)
        field4 = Column(Float, nullable=True)
        field5 = Column(Float, nullable=True)
        field6 = Column(Float, nullable=True)
        field7 = Column(Float, nullable=True)
        field8 = Column(Float, nullable=True)
