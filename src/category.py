from typing import List, Optional, Union

from src.heir_class import LawnGrass, Smartphone
from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    product_count: int = 0  # общее количество продуктов (сумма quantity всех продуктов)
    category_count: int = 0  # общее количество категорий
    total_quantity: int = 0  # общее количество товаров (сумма quantity всех продуктов)
    total_quantity_in_category: int = 0  # общее количество товаров (сумма quantity отдельно по категории)

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
                self.total_quantity_in_category += product.quantity  # сумма quantity счётчик для каждой категории

    def __str__(self) -> str:
        """Возвращает строковое представление категории с общим количеством товаров"""
        if self.name:
            if not self.__products:
                return f"{self.name}, количество продуктов: 0 шт."
        total_quantity_in_category = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity_in_category} шт."

    @classmethod
    def total_quantity_all_categories(cls) -> int:
        """Возвращает общее количество товаров во всех категориях"""
        return cls.total_quantity

    @property
    def products(self) -> str:
        """Геттер, возвращающий строку со списком продуктов в отформатированном виде"""
        if not self.__products:
            return ""

        # Формируем строку с продуктами
        result_lines = []
        for product in self.__products:
            # Формат: "Название продукта, X руб. Остаток: X шт."
            line = f"{str(product)}"
            result_lines.append(line)

        # Объединяем строки с переносом
        return "\n".join(result_lines)

    def add_product(self, product: Union[Product, Smartphone, LawnGrass]) -> None:
        """
        Класс-метод для добавления товара в категорию
        Принимает только объекты Product, Smartphone или LawnGrass
        """

        if isinstance(product, (Smartphone, LawnGrass, Product)):

            if product is not None:
                self.__products.append(product)
                Category.product_count += 1
                Category.total_quantity += product.quantity
                print(
                    f"Не возникла ошибка TypeError при добавлении продукта: {type(product).__name__}. "
                    f"Ожидается Product, Smartphone или LawnGrass"
                )

        else:
            raise TypeError(f"Возникла ошибка TypeError при добавлении не продукта. Получен: {type(product).__name__}")
