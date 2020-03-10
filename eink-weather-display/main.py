#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys;
import logging
from shared import logger
from shared import customException
from weather import weatherApi

INI_CONFIG_FILE = "eink-weather-display.ini"

sys.path.append("..")
sys.tracebacklimit = 0

def main():
    result = 0
    logger.setupLogging()
    log = logger.getLogger(__name__)

    try:
        log.info("")
        log.info("eink-weather-display >> Application started...")

        weatherApi.init(configFile=INI_CONFIG_FILE)
        queryResult = weatherApi.queryWeather()
        if(weatherApi.getResponseStatus(queryResult) == True):
            log.info(weatherApi.getResponseData(queryResult))
        else:
            log.error(weatherApi.getResponseError(queryResult))

    except Exception as ex:
        log.exception("eink-weather-display >> {0} was caught in main()".format(type(ex)))
        result = -1
    except:
        log.exception("eink-weather-display >> Unknown exception was caught in main()")
        result = -1
    finally:
        log.info("eink-weather-display >> Application exiting with code {}".format(result))

    return result


if __name__ == "__main__":
    # from setuptools import setup, find_packages
    # setup(name="eink-weather-display", version="1.0", packages=find_packages())

    result = main()
    exit(result)
