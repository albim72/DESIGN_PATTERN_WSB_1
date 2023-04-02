from abstract_a import AbstractProductA
from abstract_b import AbstractProductB

class ConreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "wynik: produkt B1"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_functin_a()
        return f"wynik dla B1 {result}"


class ConreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "wynik: produkt B2"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        result = collaborator.useful_functin_a()
        return f"wynik dla B2 {result}"
