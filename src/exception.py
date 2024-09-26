# import sys
# from src.logger import logging

# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
#      file_name,exc_tb.tb_lineno,str(error))

#     return error_message

    

# class CustomException(Exception):
#     def __init__(self,error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
#     def __str__(self):
#         return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e :
#         logging.info("DIvide by zero")
#         raise CustomException(e,sys)


# Exception.py
import sys
from src.logger import logging

# Error message function to capture detailed error information
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}] at line [{1}], error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Testing exception is working or not 
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("An error occurred: Divide by zero")  # Simple log before raising
#         custom_exception = CustomException(e, sys)  # Instantiate the custom exception
#         logging.error(f"Custom Exception: {str(custom_exception)}")  # Log the custom exception
#         raise custom_exception  # Raise the exception
