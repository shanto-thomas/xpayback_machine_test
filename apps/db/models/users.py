from sqlalchemy import Column, String, Integer
from apps.db.session import Base


# User table model
class UserInfo(Base):
    __tablename__ = "userinfos"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
