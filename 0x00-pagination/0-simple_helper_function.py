#!/usr/bin/env python3
"""0x00. Pagination"""


def index_range(page: int, page_size: int) -> (int, int):
    """ function named index_range that takes two integer arguments
        page and page_size.
    """
    res = None
    if page == 1:
        res = (0, page_size)
    else:
        cpt = 1
        begin_index = 0
        while cpt < page:
            begin_index += page_size
            cpt += 1
        res = (begin_index, begin_index + page_size)
    return res
