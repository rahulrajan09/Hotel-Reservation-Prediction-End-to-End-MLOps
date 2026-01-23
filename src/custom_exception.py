import traceback
import sys

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = self._get_detailed_error_message(error_message)
        
        
    @staticmethod
    def _get_detailed_error_message(error_message):
        _ , _ ,exc_tb = sys.exc_info()
        if exc_tb is not None:
            filename=exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f" Error occured in file [{filename}] at line [{line_number}] | error_message: [{error_message}]"
        else:
            return f"Error : {error_message}"
    
    def __str__(self):
        return self.error_message