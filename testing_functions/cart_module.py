# cart_module.py

class Item:
    def __init__(self, name, price, qty):
        self.product_name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total = 0.0
        for i in self.items:
            total += i.price * i.qty
        return total

    def isEmpty(self):
        return len(self.items) == 0

    def allCart(self):
        for i in self.items:
            if i.product_name in self.dictionary:
                self.dictionary[i.product_name] += i.qty
            else:
                self.dictionary.update({i.product_name: i.qty})
