import module_1
import module_2


class Product:

    def __init__(self, title: str, price: int | float):
        if not isinstance(title, str):
            raise TypeError()
        if not isinstance(price, int | float):
            raise TypeError()
        self.price = price
        self.title = title

    def __str__(self):
        return f'{self.title}: {self.price} грн.'


class GroupIter:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        raise StopIteration


pr_1 = Product('banana', 45)
pr_2 = Product('apple', 21)
pr_3 = Product('orange', 22)

customer_1 = module_1.Customer('Ivan', 'Ivanov', '123456789')
customer_2 = module_1.Customer('Ivan', 'Petrov', '223456789')

order_1 = module_2.Cart(customer_1)
order_2 = module_2.Cart(customer_2)

order_1.add_product(pr_1, 2.5)
order_1.add_product(pr_2, 3.)
order_1.add_product(pr_1, 2)
order_2.add_product(pr_1, 1)
order_2.add_product(pr_2, 1)
order_2.add_product(pr_3, 1)
print(customer_2)
print(order_1)
print(order_1.customer)
print(order_1)
print(order_1.quantities)
print(order_2)

for Product in order_1:
    print(Product)
