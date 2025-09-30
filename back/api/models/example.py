from sqlalchemy import Column, Integer, String
from db.base_class import Base


class ExampleModel(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(String, nullable=False)
