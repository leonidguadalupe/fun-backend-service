import json
import pytest
from abc import ABC
from algorithms.utils import Sort

def test_sort_is_abstract():
    """
        Test expects Sort class to be  subclass of
        abstract base class
    """
    assert issubclass(Sort,ABC)