# -*- coding: utf-8 -*-
"""日志记录模块
usage:
    from log import get_logger
    ....
    logger = get_logger("name", path)
    ...
    logger.info(...)
    logger.error(...)
"""
import logging
from logging import handlers


def setup_logger(logger, log_path, level="debug"):
    level_dict = {"critical": logging.CRITICAL,
                  "error": logging.ERROR,
                  "warning": logging.WARNING,
                  "info": logging.INFO,
                  "debug": logging.DEBUG}
    log_level = level_dict.get(level, logging.DEBUG)
    logger.setLevel(log_level)
    handler = handlers.TimedRotatingFileHandler(log_path, when='d', interval=1)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def get_logger(name, path):
    logger = logging.getLogger(name)
    setup_logger(logger, path)
    return logger
