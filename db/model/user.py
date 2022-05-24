from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)
    tasks = relationship("Tasks")

    def __repr__(self):
       return "<User(user_id='%s')>" % (
                                self.user_id)