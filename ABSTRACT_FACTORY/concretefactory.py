from abstract import AbstractFactory
from abstract_a import AbstractProductA
from abstract_b import AbstractProductB
from conc_prodA import ConcreteProductA1,ConcreteProductA2
from conc_prodB import ConreteProductB1, ConreteProductB2


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConreteProductB2()
