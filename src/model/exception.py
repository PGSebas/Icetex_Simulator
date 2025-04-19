"""This module contains the custom exceptions for the model module."""
class CollegeEnrollmentError(Exception):
    """Exception raised for errors in the college enrollment amount."""
    def __init__(self, message="Invalid college enrollment. Please enter a valid number."):
        self.message = message

        super().__init__(self.message)

class CollegeEnrollmentMenorThanZeroError(Exception):
    """Exception raised for errors in the college enrollment amount."""
    def __init__(self, message="College enrollment cannot be less than zero. Enter a value greater than zero."):
        self.message = message 

        super().__init__(self.message)

class SemestersError(Exception):
    """Exception raised for errors in the number of semesters."""
    def __init__(self, message="Invalid number of semesters. Enter a positive number between 1 and 12"):
        self.message = message

        super().__init__(self.message)

class CreditTypeError(Exception):
    """Exception raised for errors in the credit type."""
    def __init__(self, message="Invalid credit type"):
        self.message = message

        super().__init__(self.message)

class NotPressBottonError(Exception):
    """ Exception raised for errors when a button is not pressed."""
    def __init__(self, message="You must select a credit type before proceeding. Press any of the buttons"):
        self.message = message
        
        super().__init__(self.message)
        
class NotCollegeEnrollmentError(Exception):
    """Exception raised for errors in the college enrollment amount."""
    def __init__(self, message="Invalid college enrollment. Enter the value of your college enrollment (eg 7854100)"):
        self.message = message

        super().__init__(self.message)
