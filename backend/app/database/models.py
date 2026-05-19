from sqlalchemy import Column,Integer,String
from app.database.database import Base

# pylint: disable=too-few-public-methods
class Ticket(Base):
    __tablename__="tickets"

    id=Column(Integer,primary_key=True,index=True)
    message=Column(String)
    category=Column(String)
    sentiment=Column(String)
    priority=Column(String)
    summary=Column(String)
