from src.product import Product

# cоздан класс наследниk Product

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError (f'Товар не относится к классу {Smartphone}')
        return self




# cоздан класс наследниk Product 
class LawnGrass (Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError(f'Товар не относится к классу {LawnGrass}')
        return self
