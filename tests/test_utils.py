from src.utils import read_json


def test_read_json() -> None:
    """Тест чтения JSON файла"""
    data = read_json("data/products.json")
    assert isinstance(data, list)
    assert len(data) > 0
