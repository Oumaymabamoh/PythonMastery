class Product:
    def __init__(self, price):
        self.price = price

    # decorator
    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative,")
        self.price = value


product = Product(-10)
print(product.price)
