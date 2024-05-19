#!/usr/bin/env python3
"""
Module of index_range function
"""


def index_range(page: int, page_size: int) -> tuple:
    """ Return a tuple of size two containing
    a start index and an end index corresponding to
    the range of indexes to return in a list for
    those particular pagination parameters. """
    start = (page - 1) * page_size
    return (start, start + page_size)
