# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import logging
from nextgisweb.file_storage import FileObj

from nextgisweb.models import declarative_base
from nextgisweb import db
from sqlalchemy.sql import func

Base = declarative_base()


class LogLevels:

    critical = logging.CRITICAL
    error = logging.ERROR
    warning = logging.WARNING
    info = logging.INFO
    debug = logging.DEBUG
    notset = logging.NOTSET

    enum = (critical, error, warning, info, debug, notset)
    names_enum = (logging.getLevelName(level) for level in enum)

    default_value = notset
    default_value_name = logging.getLevelName(default_value)

    @staticmethod
    def get_name(level):
        return logging.getLevelName(level)



class LogEntry(Base):
    __tablename__ = 'log_entry'

    id = db.Column(db.Integer, primary_key=True)
    append_dt = db.Column(db.DateTime, default=func.now())
    component = db.Column(db.Unicode(250))
    group = db.Column(db.Unicode(250))

    message_level = db.Column(db.Integer, default=LogLevels.default_value)
    message_level_name = db.Column(db.Enum(*LogLevels.names_enum), default=LogLevels.default_value_name)
    message_name = db.Column(db.Unicode)
    message_text = db.Column(db.Unicode)

    exc_info = db.Column(db.Unicode)

    @staticmethod
    def log(mess_text, mess_level=LogLevels.default_value, mess_name=None, component=None, group=None, exc_info=None, append_dt=None):
        log_entry = LogEntry()
        log_entry.component = component
        log_entry.group = group

        log_entry.message_level = mess_level
        log_entry.message_level_name = LogLevels.get_name(mess_level)
        log_entry.message_name = mess_name
        log_entry.message_text = mess_text

        log_entry.exc_info = exc_info

        if append_dt:
            log_entry.append_dt = append_dt

        log_entry.persist()

    @staticmethod
    def info(mess_text, **kwargs):
        LogEntry.log(mess_text, mess_level=LogLevels.info, **kwargs)

    @staticmethod
    def debug(mess_text, **kwargs):
        LogEntry.log(mess_text, mess_level=LogLevels.debug, **kwargs)

    @staticmethod
    def critical(mess_text, **kwargs):
        LogEntry.log(mess_text, mess_level=LogLevels.critical, **kwargs)

    @staticmethod
    def error(mess_text, **kwargs):
        LogEntry.log(mess_text, mess_level=LogLevels.error, **kwargs)

    @staticmethod
    def warning(mess_text, **kwargs):
        LogEntry.log(mess_text, mess_level=LogLevels.warning, **kwargs)

