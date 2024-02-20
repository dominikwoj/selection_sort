from main import selection_sort
def test__empty_array():
    assert selection_sort([]) == []

def test__one_element_array():
    assert selection_sort([2]) == [2]

def test__ten_elements_array():
    assert selection_sort([71, 65, 39, 38, 38, 19, 42, 85, 33]) == [19, 33, 38, 38, 39, 42, 65, 71, 85]
