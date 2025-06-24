import logging
import functools
import os
from datetime import datetime

# Generate log filename based on today's date
today_str = datetime.now().strftime("%Y-%m-%d")
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"{today_str}.log")

# Set up logger
logger = logging.getLogger("navlogs")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers if imported multiple times
if not logger.hasHandlers():
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# Generic decorator factory
def log_decorator(level):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.log(level, f"{func.__name__} returned {result}")
                return result
            except Exception as e:
                logger.exception(f"Exception in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator

# Specific decorators
debug = log_decorator(logging.DEBUG)
info = log_decorator(logging.INFO)
warning = log_decorator(logging.WARNING)
error = log_decorator(logging.ERROR)
critical = log_decorator(logging.CRITICAL)
