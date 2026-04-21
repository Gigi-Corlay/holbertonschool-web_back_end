#!/usr/bin/env python3
"""
Hypermedia pagination module.
"""

import csv
import math
from typing import List, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end indexes for pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a dataset of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = list(reader)
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return pagination metadata.
        """
        data = self.get_page(page, page_size)
        dataset_len = len(self.dataset())

        total_pages = math.ceil(dataset_len / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
