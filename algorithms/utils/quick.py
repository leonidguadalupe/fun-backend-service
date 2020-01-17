import copy
import json
from .sort import Sort
        

class QuickSort(Sort):
    def __init__(self, array):
        super().__init__(array)
        self.sort() # sort after array init
    
    def _swap(self: object, array: list, left: int, right: int) -> list:
        array[left], array[right] = array[right], array[left]
        return array

    def _doQuickSort(self: object, array: list, pivot: int, left: int, right: int) -> None:
        if left >= right:
            return
        while right >= left:
            if array[pivot] < array[left] and array[pivot] > array[right]:
                self._swap(array, left, right)
                self.result.append({
                    "list": copy.deepcopy(array),
                    "right": right,
                    "left": left,
                    "pivot": pivot
                })
                continue #cut here to show swap change in frontend
            if array[pivot] >= array[left]:
                left += 1
            if array[pivot] <= array[right]:
                right -= 1
            self.result.append({
                    "list": copy.deepcopy(array),
                    "right": right,
                    "left": left,
                    "pivot": pivot
            })
        # swap pivot with right
        self._swap(array, pivot, right)
        self.result.append({
                "list": copy.deepcopy(array),
                "right": right,
                "left": left,
                "pivot": pivot
        })
        # divide and conquer
        self._doQuickSort(array, pivot, pivot+1, right-1)
        self._doQuickSort(array, left, left+1, len(array)-1)
        
        return 
    
    def sort(self):
        self._doQuickSort(self.array, 0, 1, len(self.array)-1)
        return self.result
    
    # Let's sort and serialize boiz
    def serialize(self) -> str:
        return json.dumps(self.result)