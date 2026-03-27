from typing import Any, List

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

    # Проверяем, что products возвращает строку
    assert isinstance(category_fixture[0].products, str)
    assert isinstance(category_fixture[1].products, str)

    # Проверяем количество продуктов через количество строк
    # .split('\n') разделит строку на строки, и мы получим список строк
    products_lines_1 = category_fixture[0].products.split("\n")
    products_lines_2 = category_fixture[1].products.split("\n")

    # В первой категории 3 продукта, значит 3 строки
    assert len(products_lines_1) == 3
    # Во второй категории 1 продукт, значит 1 строка
    assert len(products_lines_2) == 1

    # Проверяем содержимое каждой строки
    expected_products_1 = [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]

    for expected in expected_products_1:
        assert expected in products_lines_1

    expected_product_2 = '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
    assert expected_product_2 in products_lines_2


def test_category_creation(category_fixture: List[Category]) -> None:
    """Тест создания категорий"""
    category1, category2 = category_fixture

    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    # Проверяем содержимое первой категории
    products1 = category1.products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products1
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products1
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products1
    assert len(products1.split("\n")) == 3

    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    # Проверяем содержимое второй категории
    products2 = category2.products
    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.' in products2
    assert len(products2.split("\n")) == 1


def test_category_count_increment(single_category_fixture: Category) -> None:
    """Тест увеличения счетчика категорий"""
    initial_count = Category.category_count
    Category("New Category", "Description", [])
    assert Category.category_count == initial_count + 1


def test_product_count_in_category(category_fixture: List[Category]) -> None:
    """Тест подсчета количества продуктов в категории"""
    # В первой категории 3 продукта, во второй 1 продукт
    assert Category.product_count == 4


def test_total_quantity_in_category(category_fixture: List[Category]) -> None:
    """Тест подсчета общего количества товаров"""
    # 5 + 8 + 14 + 7 = 34
    assert Category.total_quantity == 34


def test_add_product(single_category_fixture: Category) -> None:
    """Тест добавления продукта в категорию"""
    initial_count = Category.product_count
    initial_quantity = Category.total_quantity
    products_str = single_category_fixture.products
    if products_str:
        initial_products_count = len(products_str.split("\n"))
    else:
        initial_products_count = 0

    # Создаем и добавляем новый продукт
    new_product = Product("Phone 3", "Description 3", 70000.0, 3)
    single_category_fixture.add_product(new_product)

    # Проверяем количество продуктов после добавления
    new_products_str = single_category_fixture.products
    new_products_count = len(new_products_str.split("\n"))

    # Количество продуктов должно увеличиться на 1
    assert new_products_count == initial_products_count + 1

    # Проверяем, что новый продукт присутствует в строке
    assert "Phone 3, 70000.0 руб. Остаток: 3 шт." in new_products_str

    # Проверяем, что старые продукты остались
    assert "Phone 1, 50000.0 руб. Остаток: 10 шт." in new_products_str
    assert "Phone 2, 60000.0 руб. Остаток: 5 шт." in new_products_str

    # Проверяем счетчики
    assert Category.product_count == initial_count + 1
    assert Category.total_quantity == initial_quantity + new_product.quantity


def test_add_product_with_none(single_category_fixture: Category) -> None:
    """Тест добавления None в категорию - ничего не происходит"""
    initial_count = Category.product_count
    initial_quantity = Category.total_quantity
    initial_products_len = len(single_category_fixture.products)

    # Добавляем None - метод должен обработать это корректно
    single_category_fixture.add_product(None)

    # Проверяем, что ничего не изменилось
    assert len(single_category_fixture.products) == initial_products_len
    assert Category.product_count == initial_count
    assert Category.total_quantity == initial_quantity


def test_products_property_returns_list(single_category_fixture: Category) -> None:
    """Тест свойства products (должно возвращать str)"""
    products = single_category_fixture.products
    assert isinstance(products, str)
    assert products == "Phone 1, 50000.0 руб. Остаток: 10 шт.\nPhone 2, 60000.0 руб. Остаток: 5 шт."


def test_samsung_product_price(category_fixture: List[Category]) -> None:
    """Тест проверяет цену Samsung в первой категории"""
    samsung = category_fixture[0].products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in samsung
    assert "Samsung Galaxy S23 Ultra" in samsung
    assert "180000.0" in samsung
    assert "5 шт." in samsung


def test_iphone_product_description(category_fixture: List[Category]) -> None:
    """Тест проверяет описание iPhone"""
    iphone = category_fixture[0].products
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in iphone
    assert "Iphone 15" in iphone
    assert "210000.0" in iphone
    assert "8 шт." in iphone


def test_tv_product_name(category_fixture: List[Category]) -> None:
    """Тест проверяет название телевизора"""
    tv = category_fixture[0].products
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in tv
    assert "Xiaomi Redmi Note 11" in tv
    assert "31000.0" in tv
    assert "14 шт." in tv


def test_total_products_in_all_categories(category_fixture: List[Category]) -> None:
    """Тест проверяет общее количество продуктов во всех категориях"""
    products_str_1 = category_fixture[0].products
    products_line_1 = products_str_1.split("\n")
    products_str_2 = category_fixture[1].products
    products_line_2 = products_str_2.split("\n")
    assert len(products_line_1 + products_line_2) == 4


def test_product_creation(product_fixture: "Product") -> None:
    """Тест создания продукта"""
    assert product_fixture.name == "Samsung Galaxy C23 Ultra"
    assert product_fixture.description == "256GB, Серый цвет, 200MP камера"
    assert product_fixture.price == 180000.0
    assert product_fixture.quantity == 5


def test_price_getter(product_fixture: "Product") -> None:
    """Тест получения цены через property"""
    assert product_fixture.price == 180000.0


def test_price_setter_valid(product_fixture: "Product") -> None:
    """Тест установки корректной цены"""
    product_fixture.price = 200000.0
    assert product_fixture.price == 200000.0


def test_price_setter_zero(product_fixture: "Product", capsys: Any) -> None:
    """Тест установки нулевой цены"""
    original_price = product_fixture.price
    product_fixture.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_fixture.price == original_price
