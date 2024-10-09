class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, key, value):
        if key == 'price':
            if not (isinstance(value, int) and value > 0):
                raise ValueError('Price должен быть положительным целым числом.')
        elif key == 'quantity':
            if not (isinstance(value, int) and value >= 0):
                raise ValueError('Quantity должен быть неотрицательным целым числом.')
        super(Product, self).__setattr__(key, value)

    def __str__(self):
        return f'{self.name = }, {self.price = }, {self.quantity = }'


if __name__ == '__main__':
    try:
        prod = Product("Laptop", 1000, 10)
        prod.price = 1200
        prod.quantity = -1
        print(prod)
    except ValueError as e:
        print(e)
