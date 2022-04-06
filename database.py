

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database
from ev_setting import settings

ENVIRONMENT="dev"


if ENVIRONMENT== "dev":
    ENVIRONMENT="Dev"
if ENVIRONMENT=="prod":
    ENVIRONMENT=="Prod"
if ENVIRONMENT=="qa":
    ENVIRONMENT="QA"

if ENVIRONMENT=="demo":
    ENVIRONMENT="Demo"


# databaseName= "_".join([ENVIRONMENT,'EV'])
# # dbname is the database name
# # user_id and user_password are what you put in above

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:echo@localhost/EV"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()







