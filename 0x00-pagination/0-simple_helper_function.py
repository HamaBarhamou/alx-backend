#!/usr/bin/env python3
"""0x00. Pagination"""


def index_range(page: int, page_size: int) -> (int, int):
    """ function named index_range that takes two integer arguments
        page and page_size.
    """
    if page == 1:
        return (0, page_size)

    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
