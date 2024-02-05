import logging
from scrape_config import log_path
logging.basicConfig(filename= log_path, encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger()

def log_error(e):
    print(e)
    logger.error(e)

