"""
Author: Golemon
Created: 2025.1.8 
Version: 1.0

Description:
This script defines a `Printer` class that allows controlled printing based on an internal flag. The `enable_print` flag determines whether print statements will output to the console. 
"""

class Printer:
    """
    A class that controls printing based on an internal flag.
    
    Attributes:
        enable_print (bool): Flag to control whether to print or not.
    """

    def __init__(self, enable_print=True):
        """
        Initialize the Printer instance with a given print control flag.
        
        Args:
            enable_print (bool): Set to True to allow printing, False to suppress.
        """
        self.__enable_print = enable_print

    def info(self, *args, **kwargs):
        """
        Print messages if `enable_print` is True, else suppress the output.
        """
        if self.__enable_print:
            print(*args, **kwargs)

    def set_print_control(self, enable_print: bool):
        """
        Set the print control flag.
        
        Args:
            enable_print (bool): Set to True to allow printing, False to suppress.
        """
        self.__enable_print = enable_print

# Example usage
def main(printer: Printer):
    printer.info("abc", type("abc"))  # Controlled by Printer's enable_print flag
    print("This is a regular print statement, not controlled.")  # Uncontrolled

if __name__ == "__main__":
    # Create Printer instance with initial flag set to True
    printer = Printer(enable_print=True)
    
    print("When the global control variable is True:")
    main(printer)

    # Change the print control flag to False
    printer.set_print_control(False)
    print("\nWhen the global control variable is False:")
    main(printer)


##########################################################################################
# Example usage in another file:
# from utils.info_print import Printer  # Import the Printer class
# console = Printer()  # Create an instance of Printer
# console.info("abc", type("abc"))  # Print information to the console
# console.set_print_control(False)  # Disable console output
# console.info("abc", type("abc"))  # No output will be shown
##########################################################################################