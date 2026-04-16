from typing import Union

from src.product import Product

# cоздан класс наследниk Product


class Smartphone(Product):
    """Класс наследник Smartphone класса Product: «Смартфон», который расширен атрибутами:
    производительность (efficiency), модель (model), объем встроенной памяти (memory), цвет (color)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: Union[str, float],
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Union["Smartphone", int, float]) -> Union[int, float]:
        if type(other) is not type(self):
            raise TypeError(f"Товар не относится к классу {Smartphone.__name__}")
        cost_product = (self.price * self.quantity) + (other.price * other.quantity)
        return cost_product


# cоздан класс наследниk Product
class LawnGrass(Product):
    """Класс наследник LawnGrass класса Product: «Смартфон» который расширен атрибутами: страна-производитель
    (country), срок прорастания (germination_period), цвет (color)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Union["LawnGrass", int, float]) -> Union[int, float]:
        if type(other) is not type(self):
            raise TypeError(f"Товар не относится к классу {LawnGrass.__name__}")
        cost_product = (self.price * self.quantity) + (other.price * other.quantity)
        return cost_product
