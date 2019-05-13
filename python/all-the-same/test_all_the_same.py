from all_the_same import all_the_same


def test_it_should_return_true_if_all_elements_are_the_same():
    result = all_the_same([1, 1, 1])
    assert result == True
