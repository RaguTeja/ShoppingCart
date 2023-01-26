import typing
from . import abc
import json
import os,sys
from collections import OrderedDict
from shoppingcart.exception import ShoppingCartException,FileEmptyException,CartEmptyException
from . import constant


# loaded the product prices from json file and created exception when file don't exist
try:
    product_prices_file = open(constant.product_prices_file_path)
    rate_conversions_file = open(constant.rate_conversions_file_path)
except Exception as e:
    raise ShoppingCartException(e,sys)


class ShoppingCart(abc.ShoppingCart):
    
    # Convert JSON obj to Dictionary to access the data easily.
    product_prices = json.load(product_prices_file)
    rate_conversions = json.load(rate_conversions_file)
    
    
    def __init__(self):

        # Checking whether are Source files are empty or not
        if ShoppingCart.isProductPriceFileEmpty() or ShoppingCart.isRateConversionFileEmpty():
            raise FileEmptyException()

        self._items = OrderedDict()

        # Initialized total_price to show total amount charged for each Customer
        self.total_price = 0.0

    def add_item(self, product_code: str, quantity: int):

        try:
            if product_code not in self._items:
                self._items[product_code] = quantity
            else:
                q = self._items[product_code]
                self._items[product_code] = q + quantity
        except Exception as e:
            raise ShoppingCartException(e,sys)


    
# Add a 'Total' line to the receipt. This should be the full price we should charge the customer
    def print_receipt(self) -> typing.List[str]:

        try:
            lines = []

            if self.isCartEmpty():
                raise CartEmptyException()
            
            for item in self._items.items():
                price = self._get_product_price(item[0]) * item[1]

                
                # adding price of each item
                self.total_price += price
                
                price_string = "€%.2f" % price

                lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

            # Rounding the total price 
            total_price_string = "%.2f" % self.total_price

            # Converting from euros to dollar
            total_price_in_dollars = self.total_price * ShoppingCart.rate_conversions['euro_to_dollar']
            total_price_dollars_string = "%.2f" % total_price_in_dollars
            
            # Converting from euros to rupee
            total_price_in_rupees = self.total_price * ShoppingCart.rate_conversions['euro_to_rupee']
            total_price_rupees_string = "%.2f" % total_price_in_rupees

            # At the end, Append the Total to the list of items.
            lines.append("Total" + ' - ' + total_price_string+ 
            ' euros'+' ----- '+total_price_dollars_string+' dollars'+' ----- '+total_price_rupees_string+' rupees')

            
            return lines
        except Exception as e:
            raise ShoppingCartException(e,sys)
    

# Be able to fetch product prices from an external source (json file, database ...)
    def _get_product_price(self, product_code: str) -> float:

        try:
            return ShoppingCart.product_prices[product_code]
        except Exception as e:
            raise ShoppingCartException(e,sys)

    def isCartEmpty(self):
            if len(self._items.keys())==0:
                return True
            return False

    @classmethod
    def isProductPriceFileEmpty(cls):
        if len(cls.product_prices.keys())==0:
            return True
        return False

    @classmethod
    def isRateConversionFileEmpty(cls):
        if len(cls.rate_conversions.keys())==0:
            return True
        return False


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