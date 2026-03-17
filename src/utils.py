import json
import os
from typing import Any, Dict, List, cast

from src.category import Category
from src.product import Product


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """Функция для чтения JSON файла, которая возвращает список словарей"""
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="UTF-8") as file:
        dict_file = json.load(file)
        # Явно приводим тип
        if isinstance(dict_file, list):
            return cast(List[Dict[str, Any]], dict_file)
        else:
            return [cast(Dict[str, Any], dict_file)]


def objects_from_json(dict_file: List[Dict[str, Any]]) -> List[Category]:
    """Функция для принимает словарь-файл, а возвращает лист объектов и классов."""
    class_objects = []
    for file_dict in dict_file:
        products = []
        for product in file_dict["products"]:
            products.append(Product(**product))
        file_dict["products"] = products
        class_objects.append(Category(**file_dict))
    return class_objects
