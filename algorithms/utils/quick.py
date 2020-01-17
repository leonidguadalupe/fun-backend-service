import json
from .sort import Sort

class QuickSort(Sort):
    def __init__(self, array):
        super().__init__(array)
    
    # My own algorithm for quick sort
    def sort(self):
        pass
    
    # Let's sort and serialize boiz
    def serialize(self):
        self.result = self.sort()
        return json.dumps(self.result)