from abc import ABC,abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def useful_functin_a(self)->str:pass
