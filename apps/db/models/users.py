from sqlalchemy import Column, Integer, String, ForeignKey
from apps.db.session import Base


# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(String, unique=True, index=True)


# Define the Profile model
class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    profile_picture = Column(String)
