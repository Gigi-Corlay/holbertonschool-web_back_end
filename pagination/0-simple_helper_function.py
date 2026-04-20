#!/usr/bin/env python3
"""
Module that provides a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of the start and end indexes corresponding
    to the range of items to return for the given pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
