import typing
from . import abc
import json
import os

# loaded the product prices from json file
product_prices_file = open('shoppingcart\data\product_prices.json')
rate_conversions_file = open('shoppingcart\data\rate_conversions.json')


class ShoppingCart(abc.ShoppingCart):
    
    # Convert JSON obj to Dictionary to access the data easily.
    product_prices = json.load(product_prices_file)
    rate_conversions = json.load(rate_conversions_file)
    
    def __init__(self):
        self._items = dict()

        # Initialized total_price to show total amount charged for each Customer
        self.total_price = 0.0

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity


# Add a 'Total' line to the receipt. This should be the full price we should charge the customer
    def print_receipt(self) -> typing.List[str]:
        lines = []

        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]
            
            # adding price of each item
            self.total_price += price
            
            price_string = "€%.2f" % price

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

        # Rounding the total price 
        total_price_string = "€%.2f" % self.total_price

        # At the end, Append the Total to the list of items.
        lines.append("Total" + ' - ' + total_price_string)
        return lines







# Be able to fetch product prices from an external source (json file, database ...)
    def _get_product_price(self, product_code: str) -> float:

        return ShoppingCart.product_prices[product_code]

'''
    
    def _get_product_price(self, product_code: str) -> float:
        price = 0.0

        if product_code == 'apple':
            price = 1.0

        elif product_code == 'banana':
            price = 1.1

        elif product_code == 'kiwi':
            price = 3.0

        return price
    '''