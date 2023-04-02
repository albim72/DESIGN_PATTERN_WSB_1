from abstract_a import AbstractProductA

class ConcreteProductA1(AbstractProductA):
    def useful_functin_a(self) -> str:
        return "wynik: produkt A1"
    
class ConcreteProductA2(AbstractProductA):
    def useful_functin_a(self) -> str:
        return "wynik: produkt A2"
