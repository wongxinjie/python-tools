#-*- coding: utf-8 -*-
import logging
from logging import handlers

def setup_logger(logger, log_path):
    logger.setLevel(logging.DEBUG)
    handler = handlers.TimedRotatingFileHandler(log_path, when='d', interval=1)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def get_logger(name, path):
    logger = logging.getLogger(name)
    setup_logger(logger, path)
    return logger
