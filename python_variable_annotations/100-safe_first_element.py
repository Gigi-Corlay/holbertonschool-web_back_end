#!/usr/bin/env python3
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of a sequence or None.
    If the sequence is empty, returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
