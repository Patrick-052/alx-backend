#!/usr/bin/env python3
""" Paginating a CSV file """
import csv
import math
from typing import List


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
        """ Returns the page of the dataset """
        assert type(page) is int and type(page_size) \
            is int and page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        result_set = []
        for i in range(start, end):
            if i < len(dataset):
                result_set.append(dataset[i])
            else:
                return []
        return result_set

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns a dictionary containing paginationation stats """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page':
            page + 1 if len(self.get_page(page, page_size)) > 0 else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple containing a range of indexes """
    return ((page - 1) * page_size, page * page_size)
