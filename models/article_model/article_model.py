#coding=utf-8
from uuid import uuid4
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from libs.db.dbsession import Base
from libs.db.dbsession import dbSession



class Article(Base):
    """文章表"""
    __tablename__ = 'article_article'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    title = Column(String(50))
    desc = Column(Text)
    thumbnail = Column(Text)
    keywords = Column(String(50))
    tags = Column(String(50))
    readnum = Column(Integer, default=0)
    content = Column(Text)
    createtime = Column(DateTime, index=True, default=datetime.now)
    article_pic_name = Column(String(50))
    state =Column(Boolean,default=False)
    opened = Column(Boolean,default=False)

    # 与用户建立外键关系
    user_id = Column(Integer, ForeignKey('user.id'))

    #与分类建立外键关系
    category_id = Column(Integer, ForeignKey('article_category.id'))

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



class Category(Base):
    """分类表"""
    __tablename__ = 'article_category'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True,  default=lambda:str(uuid4()))
    name = Column(String(50), unique=True, )
    nickname = Column(String(50), unique=True, )
    createtime = Column(DateTime, index=True, default=datetime.now)
    keywords = Column(String(50), unique=True, )
    desc = Column(Text)
    tags = Column(String(50))
    # 建立orm查询关系,分类表与文章表的一对多关系
    articles = relationship('Article', backref='category')

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

    @classmethod
    def by_nickname(cls, nickname):
        return dbSession.query(cls).filter_by(nickname=nickname).first()





