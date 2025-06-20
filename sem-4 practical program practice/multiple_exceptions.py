#program that handles multiple exceptions and logs them.

import logging

# Setup logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
def risky_operations():
    try:
        num = int("abc") # ValueError
        result = 10 / 0 # ZeroDivisionError
    except ValueError as ve:
        logging.error("ValueError occurred", exc_info=True)
        print("Handled ValueError.")
    except ZeroDivisionError as zde:
        logging.error("ZeroDivisionError occurred", exc_info=True)
        print("Handled ZeroDivisionError.")
    except Exception as e:
        logging.error("Some other exception occurred", exc_info=True)
        print("Handled General Exception.")

risky_operations()