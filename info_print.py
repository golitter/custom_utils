"""
Author: Golemon
Created: 2025.1.8 
Version: 1.0

Description:
This script defines a `Console` class that allows controlled printing based on an internal flag. 
The `enable_print` flag determines whether `info` method calls will output to the console. 
Direct calls to Python's built-in `print` function are unaffected by this control.
"""

class Console:
    """
    A class that controls printing based on an internal flag.
    
    Attributes:
        __enable_print (bool): Private flag to control whether to print or suppress output.
    """

    def __init__(self, enable_print=True):
        """
        Initialize the Console instance with a given print control flag.
        
        Args:
            enable_print (bool): Set to True to allow printing, False to suppress output.
        """
        self.__enable_print = enable_print

    def info(self, *args, **kwargs):
        """
        Print messages if `__enable_print` is True; suppress output otherwise.
        
        Args:
            *args: Positional arguments to pass to the print function.
            **kwargs: Keyword arguments to pass to the print function.
        """
        if self.__enable_print:
            print(*args, **kwargs)

    def set_print_control(self, enable_print: bool):
        """
        Set the internal print control flag.
        
        Args:
            enable_print (bool): Set to True to allow printing, False to suppress.
        """
        self.__enable_print = enable_print

# Example usage
def main(console: Console):
    """
    Demonstrates the behavior of the Console class.
    
    Args:
        console (Console): An instance of the Console class.
    """
    console.info("abc", type("abc"))  # Controlled by Console's internal flag
    print("This is a regular print statement, not controlled by Console.")  # Uncontrolled

if __name__ == "__main__":
    # Create Console instance with initial flag set to True
    console = Console(enable_print=True)
    
    print("When the global control variable is True:")
    main(console)

    # Change the print control flag to False
    console.set_print_control(False)
    print("\nWhen the global control variable is False:")
    main(console)


##########################################################################################
# Example usage in another file:
# from utils.info_print import Console  # Import the Console class
# console = Console()  # Create an instance of Console
# console.info("abc", type("abc"))  # Print information to the console
# console.set_print_control(False)  # Disable console output
# console.info("abc", type("abc"))  # No output will be shown
##########################################################################################