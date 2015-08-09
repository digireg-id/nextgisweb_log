import logging
from .model import LogEntry, LogLevels


class NGWLogHandler(logging.Handler):
    """
    Simple standard log handler for nextgisweb_log
    """

    def __init__(self, level=LogLevels.default_value, component=None, group=None):
        logging.Handler.__init__(self, level=level)
        self.component = component
        self.group = group

    def emit(self, record):

        self.format(record)

        if record.exc_info:
            record.exc_text = logging._defaultFormatter.formatException(record.exc_info)
        else:
            record.exc_text = None

        # Insert log record:
        log_entry = LogEntry()
        log_entry.component = self.component
        log_entry.group = self.group

        log_entry.message_level = record.levelno
        log_entry.message_level_name = record.levelname
        log_entry.message_name = record.name
        log_entry.message_text = record.msg

        log_entry.exc_info = record.exc_text

        log_entry.persist()

