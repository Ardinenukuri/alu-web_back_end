#!/usr/bin/env python3
"""
define a function called filter_datum
function get_logger
"""

import logging
import re
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    logging.Formatter
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """class initialization"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
                self.fields, self.REDACTION, message, self.SEPARATOR
                )


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    filter_datum functioni
    parameters:
        fieds: list
        redaction: string
        message: string
        separator
    """

    pattern = '|'.join(f'(?<={field}=)[^{separator}]+' for field in fields)
    return re.sub(pattern, redaction, message)


def get_logger() -> logging.Logger:
    """function get logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
