from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from config import PATH_DATABASE, MODE_DEBUG
import datetime

CONN = f"sqlite:///{PATH_DATABASE}"
engine = create_engine(CONN,echo=MODE_DEBUG)
Session =  sessionmaker(bind=engine)
session = Session()
Base = declarative_base()





class Parametros(Base):
    __tablename__ = 'parametros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    url = Column(String, nullable=False)

class Texto(Base):
    __tablename__ = 'texto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String, nullable=False)
    alteracao = Column(DateTime, default=datetime.datetime.utcnow)

class Logs(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, default=datetime.datetime.utcnow)
    cod_ticket = Column(String, nullable=False)
    responsavel = Column(String, nullable=False)
    sistema = Column(String, nullable=False)
    texto = Column(String, nullable=False)
    usuario = Column(String, nullable=False)

if not os.path.exists(PATH_DATABASE):
    Base.metadata.create_all(bind=engine) 


if __name__=='__main__':
    Base.metadata.create_all(bind=engine)
    pass