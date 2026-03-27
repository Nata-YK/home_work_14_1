import json
import os
from unittest.mock import patch, mock_open

from src.utils import objects_from_json, read_json


def test_read_json(single_category_fixture) -> None:
    """Тест чтения JSON файла"""
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Телефоны",
            "products": [{"name": "Samsung", "description": "desc", "price": 100, "quantity": 5}],
        }
    ]

    # Сериализуем тестовые данные в JSON строку
    mock_json_data = json.dumps(test_data, ensure_ascii=False)

    # Используем mock_open для имитации чтения файла
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_json("test.json")

    # Проверяем результат
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["name"] == "Смартфоны"
    assert result[0]["description"] == "Телефоны"
    assert len(result[0]["products"]) == 1
    assert result[0]["products"][0]["name"] == "Samsung"


def test_read_json_empty_file() -> None:
    """Тест чтения пустого JSON файла"""
    with patch("builtins.open", mock_open(read_data="[]")):
        result = read_json("empty.json")

    assert isinstance(result, list)
    assert len(result) == 0


def test_objects_from_json_two_categories() -> None:
    """Тест с двумя категориями"""
    test_data = [
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

    result = objects_from_json(test_data)

    assert len(result) == 2
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert result[0].products == "Samsung, 100 руб. Остаток: 5 шт."
    assert result[1].products == "LG, 200 руб. Остаток: 3 шт."
    assert len(result[1].products.split("\n")) == 1


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
