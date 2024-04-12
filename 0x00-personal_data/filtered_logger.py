#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import (List, Mapping, Tuple)
import re
import logging
import time


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        pattern = r'(?<=' + field + r'=)[^' + separator + ']+'
        message = re.sub(pattern, redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self._fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to filter values in incoming log
        records using filter_datum"""
        record.message = filter_datum(
            self._fields, RedactingFormatter.REDACTION,
            record.msg, RedactingFormatter.SEPARATOR
            )
        record.asctime = time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime(record.created)
            )
        formatted_msg = RedactingFormatter.FORMAT % record.__dict__
        return formatted_msg
