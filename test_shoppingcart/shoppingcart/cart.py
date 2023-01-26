import typing
from . import abc
import json
import os,sys
from collections import OrderedDict
from shoppingcart.exception import (ShoppingCartException,
                                    FileEmptyException,
                                    CartEmptyException,
                                    ItemNotFound)
from shoppingcart.constant import product_prices_file_path,rate_conversions_file_path
from shoppingcart.logger import logging

# loaded the product prices from json file and created exception when file don't exist
try:
    product_prices_file = open(product_prices_file_path)
    rate_conversions_file = open(rate_conversions_file_path)
except Exception as e:
    raise ShoppingCartException(e,sys)


class ShoppingCart(abc.ShoppingCart):
    
    # Convert JSON obj to Dictionary to access the data easily.
    product_prices = json.load(product_prices_file)
    rate_conversions = json.load(rate_conversions_file)
    logging.info("All the Source files are loaded successfully")
    
    def __init__(self):

        # Checking whether are Source files are empty or not
        if ShoppingCart.isProductPriceFileEmpty() or ShoppingCart.isRateConversionFileEmpty():
            raise FileEmptyException()

        logging.info("All the Source files are Validated successfully")
        self._items = OrderedDict()     # From Python 3.7 there is no much difference b/w standard and ordered dict

        
    def add_item(self, product_code: str, quantity: int):

        try:
            if product_code not in self._items:
                self._items[product_code] = quantity
            else:
                q = self._items[product_code]
                self._items[product_code] = q + quantity
            logging.info("{0} with quantity of {1} has added successfully".format(product_code,quantity))
            print("{0} with quantity of {1} has added successfully".format(product_code,quantity))
            
        except Exception as e:
            raise ShoppingCartException(e,sys)


    def delete_item(self,product_code: str):
        
        try:
            if product_code not in self._items.keys():
                raise ItemNotFound()
            removed_item=self._items.pop(product_code)
            logging.info("The {} is removed successfully".format(product_code))
            print("The {} is removed successfully".format(product_code))
        except Exception as e:
            logging.info("The Item you wanted to delete is not found")
            raise ShoppingCartException(e,sys)
            

    
# Add a 'Total' line to the receipt. This should be the full price we should charge the customer
    def print_receipt(self) -> typing.List[str]:
        
        # Initialized total_price to show total amount charged for each Customer
        total_price = 0.0

        try:
            lines = []

            if self.isCartEmpty():
                raise CartEmptyException()
            
            logging.info("Confirmed that Cart is not Empty")
            for item in self._items.items():
                price = self._get_product_price(item[0]) * item[1]

                
                # adding price of each item
                total_price += price
                
                price_string = "€%.2f" % price

                lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

            # Rounding the total price 
            total_price_string = "%.2f" % total_price
            logging.info("Calculated Total Price of all the Items")
            # Be able to display the product prices in different currencies (not only Euro).
            # Converting from euros to dollar
            total_price_in_dollars = total_price * ShoppingCart.rate_conversions['euro_to_dollar']
            total_price_dollars_string = "%.2f" % total_price_in_dollars
            
            # Converting from euros to rupee
            total_price_in_rupees = total_price * ShoppingCart.rate_conversions['euro_to_rupee']
            total_price_rupees_string = "%.2f" % total_price_in_rupees
            logging.info("Calculated the Total Price and Converted into different Currencies.")
            # At the end, Append the Total to the list of items.
            lines.append("Total" + ' - ' + total_price_string+ 
            ' euros'+' ----- '+total_price_dollars_string+' dollars'+' ----- '+total_price_rupees_string+' rupees')

            logging.info("Displayed the Receipt.")
            return lines

        except Exception as e:
            raise ShoppingCartException(e,sys)
    

# Be able to fetch product prices from an external source (json file, database ...)
    def _get_product_price(self, product_code: str) -> float:

        try:
            return ShoppingCart.product_prices[product_code]
        except Exception as e:
            logging.info("The Product code is Invalid")
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