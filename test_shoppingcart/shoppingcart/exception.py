import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class ShoppingCartException(Exception):
    def __init__(self, error_message, error_detail:sys):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

class CartEmptyException(Exception):
 
  def __str__(self):
    return "Your cart is Empty, Please fill the Cart"
  
class FileEmptyException(Exception):
 
  def __str__(self):
    return "One of Your Source files is Empty, Please check it once"
  
class ItemNotFound(Exception):
 
  def __str__(self):
    return "Item not found, Please check again"
