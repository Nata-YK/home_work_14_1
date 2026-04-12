import pytest

from src.category import Category
from src.heir_class import LawnGrass, Smartphone


def test_add_product_with_none(single_category_fixture: Category) -> None:
    """Тест добавления None в категорию - должно вызывать TypeError"""
    initial_count = Category.product_count
    initial_quantity = Category.total_quantity
    initial_products_len = len(single_category_fixture._Category__products)

    # Проверяем, что добавление None вызывает TypeError
    with pytest.raises(TypeError) as exc_info:
        single_category_fixture.add_product(None)

    # Проверяем сообщение об ошибке
    error_message = str(exc_info.value)
    assert "Возникла ошибка TypeError" in error_message or "Получен: NoneType" in error_message

    # Проверяем, что ничего не изменилось
    assert len(single_category_fixture._Category__products) == initial_products_len
    assert Category.product_count == initial_count
    assert Category.total_quantity == initial_quantity


def get_products_count(category: Category) -> int:
    """Вспомогательная функция для получения количества продуктов"""
    try:
        # Пытаемся использовать метод, если он есть
        if hasattr(category, "get_products_count"):
            return category.get_products_count()
    except AttributeError:
        pass

    # Используем строковое представление
    products_str = category.products
    if not products_str:
        return 0
    return len(products_str.split("\n"))


def test_add_prod_with_none(single_category_fixture_for_smart: Category) -> None:
    """Тест добавления None в категорию - должно вызывать TypeError"""
    initial_count = Category.product_count
    initial_quantity = Category.total_quantity
    initial_products_len = get_products_count(single_category_fixture_for_smart)

    with pytest.raises(TypeError):
        single_category_fixture_for_smart.add_product(None)  # type: ignore

    assert get_products_count(single_category_fixture_for_smart) == initial_products_len
    assert Category.product_count == initial_count
    assert Category.total_quantity == initial_quantity


def test_smartphone_add_with_none() -> None:
    """Тест сложения смартфона с None"""
    phone = Smartphone("Test", "Desc", 100, 5, "95%", "Model", 128, "Black")

    with pytest.raises(TypeError):
        phone + None


def test_lawn_grass_add_with_none() -> None:
    """Тест сложения газонной травы с None"""
    grass = LawnGrass("Test", "Desc", 50, 100, "USA", "7 days", "Green")

    with pytest.raises(TypeError):
        grass + "Not a smartphonene"


def test_add_product_with_valid_prod(single_category_fixture_for_smart: Category, smartphone: Smartphone) -> None:
    """Тест добавления валидного продукта - должно успешно добавиться"""
    initial_count = Category.product_count
    initial_quantity = Category.total_quantity

    # Сохраняем начальное строковое представление
    initial_products_str = single_category_fixture_for_smart.products
    initial_products_count = len(initial_products_str.split("\n")) if initial_products_str else 0

    # Добавляем валидный продукт
    single_category_fixture_for_smart.add_product(smartphone)

    # Проверяем, что продукт добавился
    new_products_str = single_category_fixture_for_smart.products
    new_products_count = len(new_products_str.split("\n")) if new_products_str else 0

    assert new_products_count == initial_products_count + 1
    assert Category.product_count == initial_count + 1
    assert Category.total_quantity == initial_quantity + smartphone.quantity


def test_sum_smartphone() -> None:
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
    product_smart_2 = Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=205.0,
        model="15",
        memory=256,
        color="violet",
    )

    smartphone_sum_1 = product_smart_1 + product_smart_2

    assert smartphone_sum_1 == 2580000.0


def test_sum_lawngrass() -> None:
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0
