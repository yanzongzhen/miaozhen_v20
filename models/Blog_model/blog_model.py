#coding=utf-8
from uuid import uuid4
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from libs.db.dbsession import Base
from libs.db.dbsession import dbSession



class SecondComment(Base):
    """二级评论"""
    __tablename__ = 'blog_second_comment'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    content = Column(Text)
    createtime = Column(DateTime, index=True, default=datetime.now)
    #与文章表建立外键关系
    comment_id = Column(Integer, ForeignKey('blog_comment.id', ondelete="CASCADE"))
    #与用户表建立外键关系
    user_id = Column(Integer, ForeignKey('user.id'))


    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()


class Comment(Base):
    """评论表"""
    __tablename__ = 'blog_comment'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    content = Column(Text)
    createtime = Column(DateTime, index=True, default=datetime.now)
    #与文章表建立外键关系
    article_id = Column(Integer, ForeignKey('blog.id', ondelete="CASCADE"))
    #与用户表建立外键关系
    user_id = Column(Integer, ForeignKey('user.id'))

    # 建立orm查询关系,评论表与二级评论表的一对多关系
    second_comments = relationship('SecondComment', backref='comment', order_by=-SecondComment.createtime)

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()



class Blog(Base):
    """博客表"""
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    title = Column(String(50))
    desc = Column(Text)
    thumbnail = Column(Text)
    readnum = Column(Integer, default=0)
    content = Column(Text)
    createtime = Column(DateTime, index=True, default=datetime.now)
    state =Column(Boolean,default=False)
    opened = Column(Boolean,default=False)

    # 与用户建立外键关系
    user_id = Column(Integer, ForeignKey('user.id'))

    # 建立orm查询关系,文章表与评论表的一对多关系
    comments = relationship('Comment', backref='blog', passive_deletes=True, order_by=-Comment.createtime)

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()






