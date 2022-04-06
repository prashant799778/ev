
from decimal import Decimal
from email.policy import default
from multiprocessing import context
from os import name
from tkinter.tix import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy_utils.functions.orm import table_name
import uuid 
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
# from boto3.dynamodb.conditions import Key, Attr
# from botocore.exceptions import ClientError
from datetime import datetime
from ev_setting import settings

from pydantic import condecimal
from typing import Any

ENVIRONMENT=settings.ENVIRONMENT


if ENVIRONMENT== "dev":
    ENVIRONMENT="Dev"
if ENVIRONMENT=="prod":
    ENVIRONMENT=="Prod"
if ENVIRONMENT=="qa":
    ENVIRONMENT="QA"
from database import Base,engine

from sqlalchemy import Column, Integer, String,VARCHAR


def generate_uuid():
    return str(uuid.uuid4())

class Address(Base):
    table_name="AddressDetails"
    __tablename__ = "_".join([ENVIRONMENT,table_name])
    name = Column(VARCHAR(1024))
    longitude = Column(sqlalchemy.Numeric(12, 2),default=0)
    userId = Column(VARCHAR(1024), primary_key=True, default=generate_uuid)
    latitude = Column(sqlalchemy.Numeric(12, 2),default=0)
    status=Column(sqlalchemy.Integer())









