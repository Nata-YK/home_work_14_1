# HomeWork from 17/03/2026

## creating modules and functions on a topic "Введение в ООП"

### module: product.py
class Product, класса Product определяет следующие свойства:
* название (name),
* описание (description),
* цена (price),
* количество в наличии (quantity);

### module: category.py
class Category, класса Category определет следующие свойства:
* название (name),
* описание (description),
* список товаров категории (products);

### module: utils.py
1. Функция read_json(file_path) для чтения JSON-файла принимает путь к файлу JSON в качестве аргумента и возвращает список словарей с данными категорий и продуктов.
2. Функция objects_from_json(dict_file) для чтения и отражения файлов для создания объектыв и классов.