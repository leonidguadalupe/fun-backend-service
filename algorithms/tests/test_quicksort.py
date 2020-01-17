import json
import pytest
from algorithms.utils import QuickSort

def test_quicksort_url_return_is_valid_json(rf):
    request = rf.get('/sort/quick')
    print(request)
    with pytest.raises(Exception):
        json.loads(request)

def test_quicksort_returns_list():
    """
        Test for if quicksort function returns a list type 
        and if it is a multi dimensional array with dictionary objects
        inside.
    """
    sample_array = [6,5,4,3,8,9]
    a = QuickSort(sample_array)
    a.sort()
    # check if array is list
    assert isinstance(a.result,list)

    # check if array is multi dimensional
    assert isinstance(a.result[0],dict)

def test_quicksort_check_keys():
    sample_array = [6,5,4,3,8,9]
    a = QuickSort(sample_array)
    a.sort()
    assert "list" in a.result[0]

def test_quicksort_output():
    """
        Test for final result of the sorting algorithm
    """
    sample_array = [6,5,4,3,1,9]
    a = QuickSort(sample_array)
    a.sort()
    assert a.array == sorted(sample_array)

