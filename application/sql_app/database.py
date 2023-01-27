from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Service :// username : password @ machine IP or hostname / DBName
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:admin1@mysql/garden"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
