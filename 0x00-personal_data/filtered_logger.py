#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import (List, Mapping, Tuple)
import re


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        pattern = r'(?<=' + field + r'=)[^' + separator + ']+'
        message = re.sub(pattern, redaction, message)
    return message
