import json
import pytest
from algorithms.utils import QuickSort

def test_quicksort_url_return_is_valid_json():
    request = rf.get('/sort/quick')
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

    assert isinstance(a,list)

    # check if array is multi dimensional
    assert isinstance(a.sort()[0],dict)

def test_quicksort_check_keys():
    sample_array = [6,5,4,3,8,9]
    a = QuickSort(sample_array)
    keys = a[0].keys()
    assert "list" in keys

def test_quicksort_output():
    """
        Test for final result of the sorting algorithm
    """
    sample_array = [6,5,4,3,1,9]
    a = QuickSort(sample_array)
    a.sort()
    assert sorted(sample_array) == a.array[-1]["list"]

