#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import logging
import time
from shared import constants
from shared import logger
from shared import iniConfigFile
from weather import weatherApi
from weatherDisplay.weatherDisplay import WeatherDisplay

# Module Constants and level code
sys.path.append("..")
sys.tracebacklimit = 0
logger.setupLogging()
log = logger.getLogger(__name__)

# Module Methods
def main():
    returnResult = 0
    methodName = "eink-weather-display::main() >>"

    try:
        log.info("")
        log.info("{0} Application started...".format(methodName))
        configFile = constants.CONFIG_FILENAME

        configData = readConfigFile(configFile)
        returnResult = run(configData)
        # returnResult = testRun01(configData)

    except Exception as ex:
        log.exception("{0} {1} was caught in main()".format(methodName, type(ex)))
        returnResult = -1
    except:
        log.exception("{0} Unknown exception was caught in main()".format(methodName))
        returnResult = -1
    finally:
        log.info("{0} Application exiting with code {1}".format(methodName, returnResult))

    return returnResult


def readConfigFile(configFile):
    configData = {}

    configData[constants.DICTIONARY_KEY_CONFIG_FILENAME] = configFile
    iniConfigFile.init(configFile)

    section = iniConfigFile.getSection(constants.CONFIG_DISPLAY)
    if(section == None):
        displayUpdateIntervalInSecs = constants.DEFAULT_DISPLAY_UPDATE_INTERVAL
        maxNumberOfDisplayUpdates = constants.DEFAULT_DISPLAY_MAX_NUMBER_OF_DISPLAY_UPDATES
    else:
        displayUpdateIntervalInSecs = iniConfigFile.getValueBySectionAndKeyDefValue(
            section,
            constants.CONFIG_DISPLAY_UPDATE_INTERVAL,
            constants.DEFAULT_DISPLAY_UPDATE_INTERVAL)
        maxNumberOfDisplayUpdates = iniConfigFile.getValueBySectionAndKeyDefValue(
            section,
            constants.CONFIG_DISPLAY_MAX_NUMBER_OF_DISPLAY_UPDATES,
            constants.DEFAULT_DISPLAY_MAX_NUMBER_OF_DISPLAY_UPDATES)
        configData[constants.CONFIG_DISPLAY_FONT_HEADER] = iniConfigFile.getValueBySectionAndKey(
            section,
            constants.CONFIG_DISPLAY_FONT_HEADER)
        configData[constants.CONFIG_DISPLAY_FONT_BODY] = iniConfigFile.getValueBySectionAndKey(
            section,
            constants.CONFIG_DISPLAY_FONT_BODY)
        configData[constants.CONFIG_DISPLAY_FONT_FOOTER] = iniConfigFile.getValueBySectionAndKey(
            section,
            constants.CONFIG_DISPLAY_FONT_FOOTER)

    configData[constants.DICTIONARY_KEY_DISPLAY_UPDATE_INTERVAL] = int(displayUpdateIntervalInSecs, 10)
    configData[constants.DICTIONARY_KEY_MAX_NUMBER_OF_UPDATES] = int(maxNumberOfDisplayUpdates, 10)
    return configData


def run(configData):
    returnResult = 0
    methodName = "eink-weather-display::run() >>"

    try:
        displayUpdateIntervalInSecs = configData[constants.DICTIONARY_KEY_DISPLAY_UPDATE_INTERVAL]
        maxNumberOfDisplayUpdates = configData[constants.DICTIONARY_KEY_MAX_NUMBER_OF_UPDATES]
        log.info("{0} Displaying weather at {1} seconds interval (MaxNumberOfDisplayUpdates: {2})...".format(
            methodName, displayUpdateIntervalInSecs, maxNumberOfDisplayUpdates))

        weatherDisplay = WeatherDisplay(configData)
        weatherApi.init(configData[constants.DICTIONARY_KEY_CONFIG_FILENAME])

        quitLoop = 0
        loopCount = 0
        while quitLoop == 0:
            queryResult = weatherApi.queryWeather()
            if(weatherApi.getResponseStatus(queryResult) == False):
                log.error(weatherApi.getResponseError(queryResult))
            else:
                resultDisplayWeather = weatherDisplay.displayWeather(
                    weatherApi.getResponseData(queryResult))
                if resultDisplayWeather == False:
                    log.error("{0} Encountered error while displaying weather!".format(methodName))
                    quitLoop = 1
                else:
                    loopCount += 1
                    if maxNumberOfDisplayUpdates >= 0 and loopCount >= maxNumberOfDisplayUpdates:
                        quitLoop = 1
                    else:
                        time.sleep(displayUpdateIntervalInSecs)
                    log.info("    {0} Looping - loopCount: {1}, quitLoop: {2}, maxNumberOfDisplayUpdates: {3}".format(
                        methodName, loopCount, quitLoop, maxNumberOfDisplayUpdates))

    except KeyboardInterrupt:
        log.info("{0} Stopping the weather update as Ctrl-C was pressed".format(methodName))
        returnResult = 0
    except:
        log.error(
            "{0} EXCEPTION was caught".format(methodName), exc_info=True)
        returnResult = -1
    finally:
        log.info(
            "{0} Finishing displaying weather. Return result is {1}".format(methodName, returnResult))

    return returnResult


def testRun01(configData):
    returnResult = 0

    weatherApi.init(configData[constants.DICTIONARY_KEY_CONFIG_FILENAME])
    queryResult = weatherApi.queryWeather()
    if(weatherApi.getResponseStatus(queryResult) == False):
        log.error(weatherApi.getResponseError(queryResult))
        returnResult = -1
    else:
        log.info(weatherApi.getResponseData(queryResult))
        returnResult = 0

    return returnResult


if __name__ == "__main__":
    # from setuptools import setup, find_packages
    # setup(name="eink-weather-display", version="1.0", packages=find_packages())

    result = main()
    exit(result)
