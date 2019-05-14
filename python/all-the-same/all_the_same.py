from typing import Any, List


def all_the_same(elements: List[Any]) -> bool:
    return all(map(lambda x: elements[0] == x, elements))
