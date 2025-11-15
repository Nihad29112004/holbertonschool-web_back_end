#!/usr/bin/env python3
"""
Filtered logger module
"""

import os
import re
import logging
import mysql.connector
from typing import List, Tuple


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    pattern = r"(" + "|".join(fields) + r")=[^" + separator + r"]*"
    return re.sub(pattern, lambda m: m.group(1) + "=" + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR
        )
        return super().format(record)


def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, email, phone, ssn, password FROM users;")
    headers = [desc[0] for desc in cursor.description]

    logger = get_logger()

    for row in cursor:
        msg = ""
        for key, value in zip(headers, row):
            msg += f"{key}={value};"
        logger.info(msg)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
