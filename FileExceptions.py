# About class methods:
# https://realpython.com/instance-class-and-static-methods-demystified/

class FileExceptions:
    WRITE_TXT_FILE_EXCEPTION = 'Error while trying to write to txt file'
    GENERAL_EXCEPTION = 'Something went wrong'

    @classmethod
    def print_file_exception(cls):
        print(cls.WRITE_TXT_FILE_EXCEPTION)

    @classmethod
    def print_general_exception(cls):
        print(cls.GENERAL_EXCEPTION)
