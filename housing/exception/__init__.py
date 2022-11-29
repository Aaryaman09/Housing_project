import os,sys

class HousingException(Exception):

    def __init__(self, error_message: Exception, error_deatil:sys) -> str:
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message = error_message,
                                                                         error_deatil=error_deatil)

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_deatil:sys)->str:
        """
        error message : Exception Object
        error_detail : object of sys module
        """
        
        _,_,exec_tb = error_deatil.exc_info()
        
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f'Error occured in script: [{file_name} at line number: [{line_number}] error message: [{error_message}]]'
        return error_message    

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return HousingException.__name__.str()
