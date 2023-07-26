import sys
import logging


def error_message_deatil(error,error_description):
    _,_,exc_tb=error_description.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occurred in python[{0}] line number [{1}] error message[{2}]".format(

    file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message,error_detaill:sys):
        super().__init__(error_message)
        self.error_message=error_message_deatil(error_message,error_message_deatil=error_detaill)

    def __str__(self):
        return self.error_message
    



    