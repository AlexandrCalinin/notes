import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f'postgresql://{os.getenv("DB_PG_USER")}:{os.getenv("DB_PG_PASSWORD")}@{os.getenv("DB_PG_HOST")}:{os.getenv("DB_PG_PORT")}/{os.getenv("DB_PG_DB_NAME")}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, execution_options={'isolation_level': 'READ COMMITTED'})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
