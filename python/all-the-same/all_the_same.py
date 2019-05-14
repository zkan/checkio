from typing import List


def all_the_same(elements: List) -> bool:
    first_element = elements[0]
    for each in elements:
        if first_element != each:
            return False
    else:
        return True
