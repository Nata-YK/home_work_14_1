from src.category import Category
from src.heir_class import LawnGrass, Smartphone
from src.product import Product

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
    print("\n=== Статистика ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего продуктов (наименований): {Category.product_count}")
    print(f"Всего товаров (штук): {Category.total_quantity}")

    # print(category1.total_quantity)
    print("# homwork14_4****************************", 20 * "*")

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
