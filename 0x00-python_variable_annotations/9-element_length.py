#!/usr/bin/env python3
""""""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Squence]) ->
List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
