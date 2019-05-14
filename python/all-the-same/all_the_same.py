from typing import List


def all_the_same(elements: List) -> bool:
    return all(map(lambda x: elements[0] == x, elements))
