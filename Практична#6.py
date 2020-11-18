from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, String, Integer
class News(Base):
 __tablename__ = "news"
 id = Column(Integer, primary_key = True)
 title = Column(String)
 author = Column(String)
 url = Column(String)
 comments = Column(Integer)
points = Column(Integer)
label = Column(String)
from sqlalchemy import create_engine
engine = create_engine("sqlite:///news.db")
Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
s = session()
>>> news = News(title='Lab 7',
 author='dementiy',
 url='https://dementiy.gitbooks.io/-python/content/lab7.html',
 comments=0,
 points=0)
>>> news.id, news.title
(None, Lab 7)
>>> s.add(news)
>>> s.commit()
>>> news.id, news.title