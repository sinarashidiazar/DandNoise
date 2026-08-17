from abc import ABC, abstractmethod

class FilterBase(ABC):

    name = "BaseFilter"

    def __init__(self):
        self.enabled = True

    @abstractmethod
    def update(self, value):
        pass
