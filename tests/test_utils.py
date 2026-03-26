from src.utils import objects_from_json, read_json


def test_read_json() -> None:
    """Тест чтения JSON файла"""
    data = read_json("data/products.json")
    assert isinstance(data, list)
    assert len(data) > 0


def test_objects_from_json_two_categories():
    """Тест с двумя категориями"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Телефоны",
            "products": [{"name": "Samsung", "description": "desc", "price": 100, "quantity": 5}],
        },
        {
            "name": "Телевизоры",
            "description": "TV",
            "products": [{"name": "LG", "description": "desc", "price": 200, "quantity": 3}],
        },
    ]

    result = objects_from_json(data)

    assert len(result) == 2
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert len(result[0].products) == 1
    assert len(result[1].products) == 1


def test_objects_from_json_empty_products() -> None:
    """Тест с категорией без продуктов"""
    data = [{"name": "Пустая категория", "description": "Нет продуктов", "products": []}]

    result = objects_from_json(data)

    assert len(result) == 1
    assert result[0].name == "Пустая категория"
    assert len(result[0].products) == 0


def test_objects_from_json_empty_list() -> None:
    """Тест с пустым списком"""
    result = objects_from_json([])

    assert result == []
    assert len(result) == 0
