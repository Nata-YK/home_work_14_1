from typing import Generator, List

import pytest

from src.category import Category
from src.heir_class import Smartphone
from src.product import Product


@pytest.fixture
def product_fixture() -> Product:
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def category_fixture() -> List[Category]:
    """Фикстура для создания тестовых категорий"""
    # Сбрасываем счетчики
    Product.product_count = 0
    Category.product_count = 0
    Category.category_count = 0
    Category.total_quantity = 0
    Category.total_quantity_in_category = 0

    return [
        Category(
            name="Смартфоны",
            description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций "
            "для удобства жизни",
            products=[
                Product(
                    name="Samsung Galaxy S23 Ultra",
                    description="256GB, Серый цвет, 200MP камера",
                    price=180000.0,
                    quantity=5,
                ),
                Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
                Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14),
            ],
        ),
        Category(
            name="Телевизоры",
            description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом "
            "и помощником",
            products=[Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)],
        ),
    ]


@pytest.fixture(autouse=True)
def reset_counters() -> Generator[None, None, None]:
    """Автоматически сбрасывает счетчики перед каждым тестом"""
    Product.product_count = 0
    Category.product_count = 0
    Category.category_count = 0
    Category.total_quantity = 0
    yield
    # После теста тоже сбрасываем (на всякий случай)
    Product.product_count = 0
    Category.product_count = 0
    Category.category_count = 0
    Category.total_quantity = 0


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для создания тестового продукта"""
    return Product("Sample Product", "Sample Description", 1000.0, 10)


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    """Фикстура для создания тестовой категории"""
    return Category("Sample Category", "Sample Description", [sample_product])


@pytest.fixture
def single_category_fixture() -> Category:
    """Фикстура для создания одной категории"""
    Category.product_count = 0
    Category.category_count = 0
    Category.total_quantity = 0

    product1 = Product("Phone 1", "Description 1", 50000.0, 10)
    product2 = Product("Phone 2", "Description 2", 60000.0, 5)

    return Category("Smartphones", "Best smartphones", [product1, product2])


@pytest.fixture
def single_category_fixture_for_smart() -> Category:
    """Фикстура для создания категории с одним продуктом"""
    Category.product_count = 0
    Category.category_count = 0
    Category.total_quantity = 0
    product_smart_1 = Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=512,
        color="blue",
    )
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций "
        "для удобства жизни",
        products=[product_smart_1],
    )


@pytest.fixture
def smartphone() -> Smartphone:
    """Фикстура для создания смартфона"""
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=110.0,
        model="15",
        memory=256,
        color="violet",
    )
