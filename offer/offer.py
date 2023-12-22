from sqlalchemy import create_engine, Column, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Offer(Base):

    def __init__(self, offerUrl, title, company, salary):
        self.offerUrl = offerUrl
        self.title = title
        self.company = company
        self.salary = salary

    __tablename__ = 'offers'

    offerUrl = Column(VARCHAR(200), primary_key=True)
    title = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    salary = Column(String(100), nullable=False)

    def __repr__(self):
        return f"offerUrl={self.offerUrl}, title={self.title}, company={self.company}, salary={self.salary}"

    def to_json(self):
        return {
            "offerUrl": self.offerUrl,
            "title": self.title,
            "company": self.company,
            "salary": self.salary
        }