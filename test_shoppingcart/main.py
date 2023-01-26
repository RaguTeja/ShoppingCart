from tests.test_cart import  (
    test_add_item, 
    test_add_item_with_multiple_quantity,
    test_add_different_items,
    test_del_different_items,
    test_print_receipt,
    test_quantity_as_nonint_datatype,
    test_prod_prices_diff_currencies
    )

from shoppingcart.cart import ShoppingCart
from shoppingcart.prod_prices_in_currencies import display_prod_prices_diff_currency

shopping_cart = ShoppingCart()

test_add_item()
print("------------------------------------------------------------------------")
test_add_item_with_multiple_quantity()
print("------------------------------------------------------------------------")
test_add_different_items()
print("------------------------------------------------------------------------")
test_print_receipt()
print("------------------------------------------------------------------------")
test_del_different_items()
print("------------------------------------------------------------------------")
#test_quantity_as_nonint_datatype()
test_prod_prices_diff_currencies()
print("------------------------------------------------------------------------")



#shopping_cart.add_item("banana",4)
#shopping_cart.add_item("apple",3)
#shopping_cart.add_item("banana",2)
#shopping_cart.add_item("kiwi",3)

#shopping_cart.add_item("banana","haha")
#shopping_cart.add_item("kiwi",1)

#print(shopping_cart.print_receipt())

#shopping_cart.delete_item("kiwi")

#shopping_cart.add_item("xtree",4)

#shopping_cart.add_item("fish",3)
#shopping_cart.add_item("kiwi",2)

#print(shopping_cart.print_receipt())
#print(display_prod_prices_diff_currency())

#test_prod_prices_diff_currencies()



