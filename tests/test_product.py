from typing import List

from src.category import Category
from src.product import Product


def test_product(product_fixture: Product) -> None:
    """Тест проверяет классовые атрибуты Product"""
    assert product_fixture.name == "Samsung Galaxy C23 Ultra"
    assert product_fixture.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixture.price == 180000.0
    assert product_fixture.quantity == 5


def test_category_class_attributes(category_fixture: List[Category]) -> None:
    """Тест проверяет классовые атрибуты Category"""
    assert Category.category_count == 2  # две категории
    assert Category.product_count == 4  # четыре продукта (3 + 1)


def test_category(category_fixture: List[Category]) -> None:
    """Тест проверяет атрибут name, description, products по индексу Category"""
    assert len(category_fixture) == 2
    assert category_fixture[0].name == "Смартфоны"
    assert category_fixture[1].name == "Телевизоры"
    assert (
        category_fixture[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert (
        category_fixture[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_fixture) == 2
    assert len(category_fixture[0].products) == 3
    assert len(category_fixture[1].products) == 1


def test_samsung_product_price(category_fixture: List[Category]) -> None:
    """Тест проверяет цену Samsung в первой категории"""
    samsung = category_fixture[0].products[0]
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_iphone_product_description(category_fixture: List[Category]) -> None:
    """Тест проверяет описание iPhone"""
    iphone = category_fixture[0].products[1]
    assert iphone.description == "512GB, Gray space"


def test_tv_product_name(category_fixture: List[Category]) -> None:
    """Тест проверяет название телевизора"""
    tv = category_fixture[1].products[0]
    assert tv.name == '55" QLED 4K'
    assert tv.price == 123000.0
    assert tv.quantity == 7


def test_total_products_in_all_categories(category_fixture: List[Category]) -> None:
    """Тест проверяет общее количество продуктов во всех категориях"""
    total_products = sum(len(category.products) for category in category_fixture)
    assert total_products == 4  # 3 + 1
