import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower (Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), )
    username = Column(String(50), nullable=False, unique=True)
    email = Column (String(50),nullable=False, unique=True)
    password = Column(String(20),nullable=False)

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), )
    username = Column(String(50), nullable=False, unique=True)
    email = Column (String(50),nullable=False, unique=True)
    password = Column(String(20),nullable=False)
    follower_id = Column(Integer,ForeignKey('follower.id'))
    follower = relationship(Follower)

class Like (Base):
    __tablename__= 'like'
    id = Column(Integer,primary_key=True)

class Image (Base):
    __tablename__= 'image'
    id = Column(Integer,primary_key=True)

class Comment (Base):
    __tablename__='comment'
    id = Column(Integer,primary_key=True)
    text= Column(String(500))
    hashtag=Column(String(20))

class Post (Base):
    __tablename__='post'
    id = Column(Integer,primary_key=True)
    like_id = Column(Integer, ForeignKey('like.id'))
    like = relationship(Like)
    comment_id = Column(Integer,ForeignKey('comment.id'))
    comment = relationship(Comment)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    image_id = Column(Integer,ForeignKey('image.id'))
    image = relationship(Image)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e