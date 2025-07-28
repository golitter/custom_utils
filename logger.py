"""
Author: Golemon
Updated: 2025.7.28
Version: 1.0

Description:
This script defines a customizable `Logger` class that provides various logging levels (debug, info, warning, error, and critical). 
It allows you to log messages to both a file and the console, based on the specified configuration. 
The logger is designed to be flexible and can be tailored to different logging needs.
"""

import logging

class Logger:
    """
    A customizable logger class for logging messages with different levels.

    Attributes:
        logger_name (str): The name of the logger, name must be imported using __name__.
        log_file (str): File path to save the log messages (do not include the file extension).
        log_level (int): Logging level (default is logging.DEBUG).
    """

    def __init__(self, logger_name: str, log_file: str = "application", log_level=logging.DEBUG):
        """
        Initialize the Logger instance.

        Args:
            logger_name (str): The name of the logger.
            log_file (str): The file path for log output.
            log_level (int): Logging level (default: DEBUG).
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s -: %(message)s"
        )

        # Create file handler
        file_handler = logging.FileHandler(log_file + ".log")
        file_handler.setFormatter(formatter)

        # Create console handler
        console_handler = logging.StreamHandler()
        # Whether to print to the console; uncomment to print to the console
        # console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message: str):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message: str):
        """Log a critical message."""
        self.logger.critical(message)


# Example usage
if __name__ == "__main__":
    # Create a logger instance
    # 2025.7.28 : The log name must be imported using __name__.
    app_logger = Logger(logger_name=__name__)

    # Log messages at different levels
    app_logger.debug("This is a debug message.")
    app_logger.info("This is an info message.")
    app_logger.warning("This is a warning message.")
    app_logger.error("This is an error message.")
    app_logger.critical("This is a critical message.")