from src.category import Category
from src.product import Product
from src.utils import read_json, objects_from_json

if __name__ == "__main__":
    # product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    # product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # print(product3.name)
    # print(product3.description)
    # print(product3.price)
    # print(product3.quantity)
    #
    # category1 = Category(
    #     "Смартфоны",
    #     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    #     [product1, product2, product3],
    # )
    #
    # print(category1.name == "Смартфоны")
    # print(category1.description)
    # #print(len(category1.products))
    # print(category1.category_count)
    # print(category1.product_count)
    #
    # #print(category1.products)
    #
    # product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    # category2 = Category(
    #     "Телевизоры",
    #     "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    #     [product4],
    # )
    #
    # print(category2.name)
    # print(category2.description)
    # #print(len(category2.products))
    # #print(category2.products)
    #
    # print(Category.category_count)
    # print(Category.total_quantity)
    #
    # raw_dict = read_json("data/products.json")
    # objects_category = objects_from_json(raw_dict)
    # print(f"{objects_category[0].name}, {objects_category[1].name}")
    # print(objects_category[0].products, objects_category[1].products)

    # homwork14_2****************************
    # product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    # product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # category1 = Category(
    #     "Смартфоны",
    #     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    #     [product1, product2, product3],
    # )
    # # Категория с одним продуктом
    # print(category1.total_quantity)
    #
    # product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    # category1.add_product(product4)
    # print(category1.products)
    # print(category1.product_count)
    #
    # new_product = Product.new_product(
    #     {
    #         "name": "Samsung Galaxy S23 Ultra",
    #         "description": "256GB, Серый цвет, 200MP камера",
    #         "price": 180000.0,
    #         "quantity": 5,
    #     }
    # )
    # print(new_product.name)
    # print(new_product.description)
    # print(new_product.price)
    # print(new_product.quantity)
    #
    # new_product.price = 800
    # print(new_product.price)
    #
    # new_product.price = -100
    # print(new_product.price)
    # new_product.price = 0
    # print(new_product.price)

    print("# homwork14_3****************************", 20 * "*")
    category2 = [
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

    # Выводим каждую категорию
    print("=== Вывод категорий ===")
    for category in category2:
        print(category)

    # Выводим список категорий (будет использовать __repr__)
    print("\n=== Список категорий ===")
    print(category2)

    # Выводим общую статистику
    print(f"\n=== Статистика ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего продуктов (наименований): {Category.product_count}")
    print(f"Всего товаров (штук): {Category.total_quantity}")

    # print(category1.total_quantity)
