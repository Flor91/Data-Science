import logging
import pprint


def logger(logfile, level=logging.DEBUG):
    logger = logging.basicConfig(
        filename=logfile,
        format="%(asctime)s ¡ %(levelname)s >>> %(message)s",
        filemode="w",
        level=level,
    )
    
    logging.info(f" Started ".center(30, "*"))
