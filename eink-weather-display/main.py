#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
from helpers import logger;

def main():
    result = 0
    logger.setupLogging()
    log = logger.getLogger(__name__)

    try:
        log.info("")
        log.info("eink-weather-display >> Application started...")



    except:
        log.error("eink-weather-display >> EXCEPTION was caught in main()", exc_info=True)
    finally:
        log.info("eink-weather-display >> Application exiting with code {}".format(result))
    return result


if __name__ == "__main__":
    result = main()
    exit(result)
