from typing import List


def all_the_same(elements: List) -> bool:
    for each in elements:
        if elements[0] != each:
            return False
    else:
        return True
