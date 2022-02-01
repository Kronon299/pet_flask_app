from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://user:password@localhost:5432/aws_api")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    added = Column(String, nullable=False, default=False)
