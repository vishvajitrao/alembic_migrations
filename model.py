from sqlalchemy import String, Column, DateTime, Boolean
import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
import calendar

Base = declarative_base()

current_datetime = datetime.datetime.utcnow()
current_timetuple = current_datetime.utctimetuple()
current_timestamp = calendar.timegm(current_timetuple)


class CallNotes(Base):
    __tablename__ = "call_notes"

    id = Column(String(40), primary_key=True, default=uuid.uuid4, unique=True)
    user_phone = Column(String(20), nullable=False)
    note = Column(String, nullable=False)
    account_id = Column(String)
    card_id = Column(String)
    bag_id = Column(String)
    status = Column(String(20), default="Open")

    #Add column
    deleted = Column(Boolean, default=False)
    created_by = Column(String(40), nullable=True)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.datetime.utcnow)
    created_on_timestamp = Column(String, default=current_timestamp)


class Authentication(Base):
    __tablename__ = "authentication"
    id = Column(String(40), primary_key=True, default=uuid.uuid4, unique=True)
    access_token = Column(String(1500), nullable=False)
    expires_in = Column(String(10), nullable=False)
    refresh_expires_in = Column(String(20), nullable=False)
    refresh_token = Column(String(700), nullable=False)
    token_type = Column(String(50), nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.datetime.utcnow)
