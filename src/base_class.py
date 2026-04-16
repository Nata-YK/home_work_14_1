from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> "BaseProduct":
        """Класс-метод для создания нового продукта"""
        pass
