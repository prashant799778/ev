from decimal import Decimal
from .imports import *
from ev_setting.settings import APP_NAME, ENVIRONMENT, HOST_ADDRESS
from fastapi import Request, HTTPException,File, Form, UploadFile
from typing import Dict, Type, TypeVar, Generic, NewType
from fastapi import Depends, FastAPI
from pydantic import BaseModel, BaseSettings, Json

from pydantic import ConstrainedDecimal
StringId = NewType('StringId', str)
class DefaultResponse(BaseModel):
    success : bool = Field(True, description="return success if request processed successfully", example=True)
    currentDT: datetime = Field(datetime.today().strftime("%s"), example=datetime.today().strftime("%s"), description="return current date with time")
    resultBody: Optional[Dict] = Field({}, example={"ABCD": "ABC", "ED":"EIK"})
    serverIp: str = Field(HOST_ADDRESS)
    message: Optional[str] = Field(example="this is message", description="return message response from api")
    environment: str = Field(ENVIRONMENT, example=ENVIRONMENT)
    roleName: str = Field(APP_NAME, example=APP_NAME)


class addressSubmit(BaseModel):
    name:str=Field(description="name of user",example='anil')
    longitude:ConstrainedDecimal =Field(description='longitude of address given by user')
    latitude:ConstrainedDecimal=Field(description='latitude of address given by user')
    class Config:
        orm_mode = True

class Updateaddress(BaseModel):
    userId:str=Field(description="userId",example='')
    longitude:ConstrainedDecimal =Field(description='longitude of address given by user')
    latitude:ConstrainedDecimal=Field(description='latitude of address given by user')
    class Config:
        orm_mode = True



class nearestlocation(BaseModel):
    longitude:ConstrainedDecimal =Field(description='longitude of address given by user')
    latitude:ConstrainedDecimal=Field(description='latitude of address given by user')
    class Config:
        orm_mode = True



   
   