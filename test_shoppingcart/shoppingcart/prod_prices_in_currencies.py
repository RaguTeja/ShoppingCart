from shoppingcart.cart import ShoppingCart
from shoppingcart.exception import (ShoppingCartException,
                                   )
from shoppingcart.logger import logging
import sys

# Be able to display the product prices in different currencies (not only Euro).

def display_prod_prices_diff_currency():

    try:
        prod_price_currency_dict = {}
        prices_dict = ShoppingCart.product_prices
        rate_dict = ShoppingCart.rate_conversions

        for item,price in prices_dict.items():
            if item not in prod_price_currency_dict:
                prod_price_currency_dict[item]=[]

            price_in_dollars = price * rate_dict['euro_to_dollar']
            price_in_rupees = price * rate_dict['euro_to_rupee']
            prod_price_currency_dict[item].extend(["%.2f" % price + ' euros',"%.2f" % price_in_dollars + ' dollars',
                                    "%.2f" % price_in_rupees + ' rupees' ])
        logging.info("Displayed Product prices for One quantity in different Currencies")
    
        return prod_price_currency_dict

    except Exception as e:
        raise ShoppingCartException(e,sys)

