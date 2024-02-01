
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
format_str = '%(message)%(levelname)%(name)%(asctime)'
formatter = jsonlogger.JsonFormatter(format_str)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
