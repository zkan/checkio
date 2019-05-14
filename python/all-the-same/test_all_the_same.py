from all_the_same import all_the_same


def test_it_should_return_true_when_all_elements_are_the_same():
    result = all_the_same([1, 1, 1])
    assert result == True


def test_it_should_return_false_when_all_elements_are_not_the_same():
    result = all_the_same([1, 2, 1])
    assert result == False


def test_it_should_return_true_when_no_element():
    result = all_the_same([])
    assert result == True
