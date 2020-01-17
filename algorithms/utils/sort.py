from abc import ABC, abstractmethod

class Sort(ABC):
    def __init__(self, array):
        self.array = array
        self.result = []
        super().__init__()
    @abstractmethod
    def sort(self):
        pass
    @abstractmethod
    def serialize(self):
        pass