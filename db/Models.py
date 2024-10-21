from sqlalchemy import String, Boolean, Integer, Column, Text, ForeignKey
from .database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    at_sale = Column(Boolean, default=False)
    inventory = Column(Integer, default=0)