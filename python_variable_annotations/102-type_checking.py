#!/usr/bin/env python3
"""
    Return a list with elements repeated factor times.
    _extended_summary_
"""
from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Each element in the input list is duplicated factor times
    in the output list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


# Example usage
array = [12, 72, 91]

# Zoom array 2x (default factor)
zoom_2x = zoom_array(array)

# Zoom array 3x
zoom_3x = zoom_array(array, 3)
