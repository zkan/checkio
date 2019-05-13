from typing import List


def all_the_same(elements: List) -> bool:
    count = 0
    first_element = elements[0]
    for each in elements:
        if first_element == each:
            count = count + 1

    if count == len(elements):
        return True
