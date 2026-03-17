class Category:
    name: str
    description: str
    products: list
    product_count = 0  # общее количество продуктов (сумма quantity всех продуктов)
    category_count = 0  # общее количество категорий
    total_quantity = 0  # общее количество товаров (сумма quantity всех продуктов)

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Считаем общее количество продуктов и товаров
        if products:
            for product in products:
                Category.product_count += 1  # каждый объект Product
                Category.total_quantity += product.quantity  # сумма quantity
