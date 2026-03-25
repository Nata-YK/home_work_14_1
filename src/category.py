from typing import List, Optional

from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    product_count = 0  # общее количество продуктов (сумма quantity всех продуктов)
    category_count = 0  # общее количество категорий
    total_quantity = 0  # общее количество товаров (сумма quantity всех продуктов)

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Считаем общее количество продуктов и товаров
        if products:
            for product in products:
                Category.product_count += 1  # каждый объект Product
                Category.total_quantity += product.quantity  # сумма quantity

    @property
    def products(self) -> None:
        """Свойство, возвращающее список продуктов"""
        return self.__products


    def add_product(self, product: 'Product') -> None:
        """
        Метод для добавления товара в категорию
        Принимает объект класса Product и добавляет его в приватный список.
        """
        if product:
            self.__products.append(product)
            Category.product_count += 1
            Category.total_quantity += product.quantity

    def get_info(self) -> str:
        """Метод для получения информации о категории"""
        return f"Категория: {self.name}, Товаров: {len(self.__products)}"

