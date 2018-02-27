#coding:utf-8
from uuid import uuid4
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from libs.db.dbsession import Base
from libs.db.dbsession import dbSession


class Flink(Base):
    """设置"""
    __tablename__ = 'flink'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    createtime = Column(DateTime, index=True, default=datetime.now)
    name = Column(String(50),nullable=False)
    url = Column(Text)
    pic_url = Column(Text)
    state = Column(Boolean,default=False)
    desc = Column(Text)
    updatetime = Column(DateTime, index=True, default=datetime.now)
    target = Column(String(30))
    rel = Column(String(30))

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