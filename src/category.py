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
    def products(self) -> str:
        """Геттер, возвращающий строку со списком продуктов в отформатированном виде"""
        if not self.__products:
            return ""

        # Формируем строку с продуктами
        result_lines = []
        for product in self.__products:
            # Формат: "Название продукта, X руб. Остаток: X шт."
            line = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            result_lines.append(line)

        # Объединяем строки с переносом
        return "\n".join(result_lines)

    def add_product(self, product: "Product") -> None:
        """
        Метод для добавления товара в категорию
        Принимает объект класса Product и добавляет его в приватный список.
        """
        if product is not None:
            self.__products.append(product)
            Category.product_count += 1
            Category.total_quantity += product.quantity
