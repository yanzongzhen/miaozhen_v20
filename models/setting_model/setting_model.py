#coding:utf-8
from uuid import uuid4
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from libs.db.dbsession import Base
from libs.db.dbsession import dbSession


class Setting(Base):
    """设置"""
    __tablename__ = 'setting'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    createtime = Column(DateTime, index=True, default=datetime.now)
    title = Column(String(50),nullable=False)
    se_title = Column(String(50))
    url = Column(Text)
    keywords = Column(String(50),nullable=False)
    desc = Column(Text)
    Email = Column(String(50))
    ICP = Column(String(50))
    limit_time = Column(Integer)

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
    def by_title(cls, title):
        return dbSession.query(cls).filter_by(title=title).first()