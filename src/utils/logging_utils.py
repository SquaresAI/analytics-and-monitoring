import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Configure a logger with the given name and log file.

    Args:
        name (str): Name of the logger.
        log_file (str): File path for storing log messages.
        level (int): Logging level (default: logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Get logger and set level
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Example usage of the logging utility
if __name__ == "__main__":
    logger = setup_logger("analytics_logger", "analytics.log")
    logger.info("Logger initialized.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
