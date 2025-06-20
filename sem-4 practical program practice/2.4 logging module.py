#Using logging module:

import logging
logging.basicConfig(filename='errors.log', level=logging.ERROR)

try:
    result = 10 / 1
except Exception as e:
    logging.error("Exception occurred", exc_info=True)