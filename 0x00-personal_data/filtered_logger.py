#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import (List, Mapping, Tuple)
import re
import logging
import time
import csv
import mysql.connector
import os


with open('user_data.csv') as csfile:
    csvreader = csv.reader(csfile)
    fields = next(csvreader)


fields.remove('ip')
fields.remove('last_login')
fields.remove('user_agent')
PII_FIELDS = tuple(fields)


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


def get_logger() -> logging.Logger:
    """create Logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function that returns a connector to the database """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        port=3306,
        database=db_name
        )


def main() -> None:
    """ function that takes no arguments
    and returns nothing"""
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        formatted_msg = f'name={row[0]}; email={row[1]}; phone={row[2]};\
 ssn={row[3]}; password={row[4]}; ip={row[5]}; last_login={row[6]}; user_agent={row[7]}'
        logger.info(formatted_msg)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
