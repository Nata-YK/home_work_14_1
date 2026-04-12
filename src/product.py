from typing import Any, Dict, Union

from src.base_class import BaseProduct
from src.product_mixin_hw import ProductMixin


class Product(ProductMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int
    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()
        Product.product_count += 1

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Union["Product", float, int]) -> Union[int, float]:
        if isinstance(other, Product):
            cost_product = (self.price * self.quantity) + (other.price * other.quantity)
            return cost_product
        elif isinstance(other, (int, float)):
            return (self.price * self.quantity) + other
        else:
            raise TypeError(f"Неверный тип файла: {type(other).__name__}")

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Класс-метод для создания нового продукта из словаря"""
        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])
