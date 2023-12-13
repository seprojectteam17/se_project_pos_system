#tests for cart

import unittest
from cart_module import Item, Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_item(self):
        item1 = Item("Product1", 10.0, 2)
        self.cart.add_item(item1)
        self.assertEqual(len(self.cart.items), 1)

    def test_remove_item(self):
        item1 = Item("Product1", 10.0, 2)
        self.cart.add_item(item1)
        self.cart.remove_item()
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_items(self):
        item1 = Item("Product1", 10.0, 2)
        item2 = Item("Product2", 5.0, 3)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.cart.remove_items()
        self.assertEqual(len(self.cart.items), 0)

    '''def test_total(self):
        item1 = Item("Product1", 10.0, 2)
        item2 = Item("Product2", 5.0, 3)
        print(f"Items added to the cart: {item1.__dict__}, {item2.__dict__}")
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        actual_total = self.cart.total()
        print(f"Actual Total: {actual_total}")
        self.assertEqual(self.cart.total(), 2 * 10.0 + 3 * 5.0)'''
    
    def test_total(self):
        item1 = Item("Product1", 10.0, 2)
        item2 = Item("Product2", 5.0, 3)

        print(f"Items added to the cart: {item1.__dict__}, {item2.__dict__}")

        self.cart.add_item(item1)
        self.cart.add_item(item2)

        actual_total = self.cart.total()
        print(f"Actual Total: {actual_total}")

        self.assertEqual(actual_total, 100.0)  

    def test_isEmpty(self):
        self.assertTrue(self.cart.isEmpty())
        item1 = Item("Product1", 10.0, 2)
        self.cart.add_item(item1)
        self.assertFalse(self.cart.isEmpty())

    def test_allCart(self):
        item1 = Item("Product1", 10.0, 2)
        item2 = Item("Product2", 5.0, 3)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.cart.allCart()
        self.assertEqual(self.cart.dictionary, {"Product1": 2, "Product2": 3})

if __name__ == '__main__':
    unittest.main()
