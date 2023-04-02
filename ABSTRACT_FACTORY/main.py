from abstract import AbstractFactory
from conretefactory import ConcreteFactory1, ConcreteFactory2

def client_code(factory:AbstractFactory)->None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")

print("Klient: testowanie klienta w pierwszym typie fabryki")
client_code(ConcreteFactory1())
print("\n")

print("Klient: testowanie klienta w drugim typie fabryki")
client_code(ConcreteFactory2())
print("\n")

