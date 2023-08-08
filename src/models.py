import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table User.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email  = Column(String(80), nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table Post.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

class Comment(Base):
    __tablename__ = " Comment"
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    Post_id = Column(Integer, ForeignKey("Post.id"))
    Post = relationship(Post)
    author_id = Column(Integer, ForeignKey("User.id"))
    User = relationship(User)

class Follower(Base):
    __tablename__ = "Follower"
    user_from_id = Column(Integer, ForeignKey("User.id"))
    user_to_id = Column(Integer, ForeignKey("User.id"))
    User = relationship(User)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
