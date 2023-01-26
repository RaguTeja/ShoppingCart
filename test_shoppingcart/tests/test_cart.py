from shoppingcart.cart import ShoppingCart
from shoppingcart.prod_prices_in_currencies import display_prod_prices_diff_currency

# Adding an Item to the Cart
def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()
    assert receipt[0] == "apple - 1 - 1.00 euros ----- 1.09 dollars ----- 88.00 rupees"

# Adding an Item with multiple quantity to the Cart
def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2) 

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 2 - 2.00 euros ----- 2.18 dollars ----- 176.00 rupees"

# Adding multiple Items to the Cart
def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt()
    assert receipt[0] == "banana - 1 - 1.10 euros ----- 1.20 dollars ----- 96.80 rupees"
    assert receipt[1] == "kiwi - 1 - 3.00 euros ----- 3.27 dollars ----- 264.00 rupees"

# Deleting multiple items from the cart
def test_del_different_items():
    
    cart = ShoppingCart()
    cart.add_item("banana",4)
    cart.add_item("apple",3)
    cart.add_item("banana",2)
    cart.add_item("kiwi",3)

    cart.delete_item("banana")
    cart.delete_item("kiwi")

    receipt = cart.print_receipt()
    print(receipt)
    assert receipt[0] == "apple - 3 - 3.00 euros ----- 3.27 dollars ----- 264.00 rupees"


# Checking the Display of printing the receipt

def test_print_receipt():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt()
    print(receipt)
    assert receipt[0] == "banana - 1 - 1.10 euros ----- 1.20 dollars ----- 96.80 rupees"
    assert receipt[1] == "kiwi - 1 - 3.00 euros ----- 3.27 dollars ----- 264.00 rupees"



# Checking the dispay of product prices in different currencies.
def test_prod_prices_diff_currencies():
    cart = ShoppingCart()
    price_dict=display_prod_prices_diff_currency()
    print(price_dict)
    assert price_dict['apple'] == ['1.00 euros', '1.09 dollars', '88.00 rupees']



# Checking the quantity while quantity is non integer datatype.
def test_quantity_as_nonint_datatype():
    cart = ShoppingCart()
    cart.add_item("apple", "numb") 
