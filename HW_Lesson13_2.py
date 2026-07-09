class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return self.name + ", Price: " + str(self.price)

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return self.name + " " + str(self.surname)

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt
        self.total = self.total + cnt * item.price

    def __str__(self):
        # str_res = "User: " + str(self.user.name) + " " + str(self.user.surname) + "\n"
        str_res = "User: " + str(self.user) + "\n"
        str_res = str_res + "Items:" + "\n"
        for product in self.products:
            str_res = str_res + "\t" + str(product) + "\n"

        str_res = str_res + "Total: " + str(self.get_total()) + "\n"

        return str_res

    def get_total(self):
        return self.total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
banan = Item('banan', 7, "yellow", "middle", )
print(lemon)
print(apple)
print()

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)
print()

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

cart.add_item(banan, 10)
print(cart)