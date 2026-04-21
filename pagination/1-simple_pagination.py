#!/usr/bin/env python3
"""
Pagination module for handling a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start and end indexes for pagination.

    Args:
        page (int): page number (starting from 1)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: start index and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class that provides pagination for a dataset of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the server with no cached dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset.

        If the dataset is not already loaded, it is read from the CSV file.

        Returns:
            List[List]: list of rows from the dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = list(reader)
            self.__dataset = dataset[1:]  # skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        The page is defined by the page number and page size.
        If the page is out of range, an empty list is returned.

        Args:
            page (int): page number (must be > 0)
            page_size (int): number of items per page (must be > 0)

        Returns:
            List[List]: list of rows for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
