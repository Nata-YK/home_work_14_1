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


def test_category_creation(category_fixture):
    """Тест создания категорий"""
    category1, category2 = category_fixture

    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category2.products) == 1


def test_category_count_increment(single_category_fixture):
    """Тест увеличения счетчика категорий"""
    initial_count = Category.category_count
    Category("New Category", "Description", [])
    assert Category.category_count == initial_count + 1


def test_product_count_in_category(category_fixture):
    """Тест подсчета количества продуктов в категории"""
    # В первой категории 3 продукта, во второй 1 продукт
    assert Category.product_count == 4


def test_total_quantity_in_category(category_fixture):
    """Тест подсчета общего количества товаров"""
    # 5 + 8 + 14 + 7 = 34
    assert Category.total_quantity == 34


def test_add_product(single_category_fixture):
    """Тест добавления продукта в категорию"""
    initial_count = Category.product_count
    initial_quantity = Category.total_quantity
    initial_products_len = len(single_category_fixture.products)

    new_product = Product("Phone 3", "Description 3", 70000.0, 3)
    single_category_fixture.add_product(new_product)

    assert len(single_category_fixture.products) == initial_products_len + 1
    assert new_product in single_category_fixture.products
    assert Category.product_count == initial_count + 1
    assert Category.total_quantity == initial_quantity + new_product.quantity


def test_add_product_with_none(single_category_fixture):
    """Тест добавления None в категорию"""
    initial_count = Category.product_count
    single_category_fixture.add_product(None)
    assert Category.product_count == initial_count  # Счетчик не должен увеличиться


def test_products_property_returns_list(single_category_fixture):
    """Тест свойства products (должно возвращать список)"""
    products = single_category_fixture.products
    assert isinstance(products, list)
    assert len(products) == 2


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


def test_product_creation(product_fixture):
    """Тест создания продукта"""
    assert product_fixture.name == "Samsung Galaxy C23 Ultra"
    assert product_fixture.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixture.price == 180000.0
    assert product_fixture.quantity == 5


def test_price_getter(product_fixture):
    """Тест получения цены через property"""
    assert product_fixture.price == 180000.0


def test_price_setter_valid(product_fixture):
    """Тест установки корректной цены"""
    product_fixture.price = 200000.0
    assert product_fixture.price == 200000.0


def test_price_setter_zero(product_fixture, capsys):
    """Тест установки нулевой цены"""
    original_price = product_fixture.price
    product_fixture.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_fixture.price == original_price
