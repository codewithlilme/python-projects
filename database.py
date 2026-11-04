from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:weedisbae@localhost:5432/Lily.lessons"
engine = create_engine(db_url)
session= sessionmaker(autoflush=False,autocommit=False,bind=engine)