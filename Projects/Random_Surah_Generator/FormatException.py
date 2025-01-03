""" custom exception class that inherits from the base class Exception """
class FormatException(BaseException):

    def __init__(self, value, message="Invalid range. Please enter a valid range between 1 and 30."):
        super().__init__(message)  # Call the base class constructor
        self.message = message
        self.value = value

    def __str__(self):
        return "Invalid range. Please enter a valid range between 1 and 30."
    
    def __reduce__(self):
        return (self.__class__, (self.message,self.value))
    