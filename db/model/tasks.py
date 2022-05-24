from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)

    task_id = Column(Integer)
    task_text = Column(String)

    parent_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users", back_populates="tasks")

    def __repr__(self):
       return "<User(task_id='%s', task_text='%s')>" % (
                                self.task_id, self.task_text)
