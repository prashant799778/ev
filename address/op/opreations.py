

from http.client import UnknownTransferEncoding
from os import name
from sqlalchemy.orm import Session
from . import models
import address.serializers as schemas
def address_submit(db: Session,addressSubmit):
    print(addressSubmit)
    db_user = models.Address(name=addressSubmit['name'],longitude=addressSubmit['longitude'],latitude=addressSubmit['latitude'],status=1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_userDetails_by_userId(db: Session,userId:str):
    return db.query(models.Address).filter(models.Address.userId ==userId).all()


def get_userDetails_by_name(db: Session,name:str):
    return db.query(models.Address).filter(models.Address.name ==name).all()

def update_address(db: Session, item: models.Address, updates):
    update_data = updates
    for key, value in update_data.items():
        setattr(item, key, value)
    db.commit()



def get_all_userDetails(db: Session):
    return db.query(models.Address).filter(models.Address.status ==1).all()