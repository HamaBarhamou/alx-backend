#!/usr/bin/env python3
"""0x00. Pagination"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        self.dataset()
        if type(page) is int and type(page_size) is int:
            ind_debut, index_end = index_range(page, page_size)
            return(self.__dataset[ind_debut: index_end])
        """ else:
            raise ValueError() """
