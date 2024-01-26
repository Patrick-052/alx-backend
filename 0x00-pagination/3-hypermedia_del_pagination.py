#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> dict:
        """ Returns a dictionary containing pagination stats """
        assert type(index) is int and type(page_size) is int
        assert 0 <= index < len(self.indexed_dataset())
        indexed_dataset = self.indexed_dataset()
        next_index = index + page_size
        next_index = min(next_index, len(indexed_dataset))
        data = [
            value for key, value in indexed_dataset.items()
            if index <= key < next_index and key in indexed_dataset
        ]
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }
