from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL database connection
DATABASE_URL = "postgresql://postgres:123@localhost/user_profile"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Mongo database connection
mongo_host = "localhost"
mongo_port = 27017
mongo_database = "user_profile"
mongo_client = MongoClient(mongo_host, mongo_port)
mongo_db = mongo_client[mongo_database]
mongo_collection = mongo_db["users"]
Base.metadata.create_all(bind=engine)
