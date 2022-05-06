import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 55, 66, 77]
    test_arr = [11, 12, 22, 25, 34, 55, 64, 66, 77, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 55, 66, 77]
    test_arr = [90, 77, 66, 64, 55, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_req03():
    arr = [64, 34, 25, 12, 22, 11, 90, 55]
    sorting_order=0

    result = Lab3.bubble_sort(arr, sorting_order)

    assert (result == 2)

def test_req02():
    arr = [64, 34, 25, 12, 22, 11, 90, 55, 66, 77, 88]
    sorting_order=0

    result = Lab3.bubble_sort(arr, sorting_order)

    assert (result == 1)

def test_req04():
    arr = []
    sorting_order=0

    result = Lab3.bubble_sort(arr, sorting_order)

    assert (result == 0)

def test_req05():
    arr = [64.4, 34, 25, 12, 22, 11, 90, 55, 66, 77]
    sorting_order = 0

    result = Lab3.bubble_sort(arr, sorting_order)

    assert (result == 3)