from tests.test_cart import  test_add_item, test_add_item_with_multiple_quantity,test_add_different_items

from shoppingcart.cart import ShoppingCart


shopping_cart = ShoppingCart()
shopping_cart.add_item("banana",4)
shopping_cart.add_item("apple",3)
shopping_cart.add_item("banana",2)
shopping_cart.add_item("kiwi",3)
print(shopping_cart.print_receipt())





'''
test_add_item()
test_add_item_with_multiple_quantity()
test_add_different_items()
'''