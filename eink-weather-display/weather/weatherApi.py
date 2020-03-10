#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
from shared import constants
from shared import logger
from shared import iniConfigFile as weatherConfig
from shared import customException as ce
from .openWeatherMapApi import Weather as OwmWeatherApi

# Module level variables and code
RESPONSE_STATUS = "status"
RESPONSE_DATA = "data"
RESPONSE_ERROR = "error"

# global __weather

def init(configFile):
    global __weather
    weatherConfig.init(configFile)
    __createWeatherProvider(weatherConfig)

def __createWeatherProvider(weatherConfig):
    global __weather
    weatherProviderName = None

    defaultSection = weatherConfig.getSection(constants.CONFIG_DEFAULT)
    if(defaultSection != None):
        weatherProviderName = weatherConfig.getValueBySectionAndKey(defaultSection, constants.CONFIG_DEFAULT_WEATHER_PROVIDER)
    if(weatherProviderName == None):
        raise ce.MissingConfigurationException(missingConfig=constants.CONFIG_DEFAULT_WEATHER_PROVIDER)

    weatherProviderSection = weatherConfig.getSection(weatherProviderName)
    if(weatherProviderSection == None):
        raise ce.MissingConfigurationException(missingConfig=constants.CONFIG_OWM)
    else:
        if(weatherProviderName == constants.CONFIG_OWM):
            __weather = OwmWeatherApi()
            __weather.readConfig(weatherProviderSection)
        else:
            raise ce.MissingConfigurationException(missingConfig=weatherProviderName)

def queryWeather():
    try:
        if(__weather == None):
            raise ce.NotInitializedException(message="Initialize WeatherApi prior to using it!")

        result = __weather.queryWeather()
        if(result == True):
            return __createResult(status=result, data=__weather.weatherData)
        else:
            return __createResult(status=result)

    except Exception as ex:
        return __createResult(
            status=False,
            error="EXCEPTION >> WeatherApi::Weather >> {0} [Exception Type: '{1}']".format(ex.__str__(), type(ex))
        )
    except:
        return __createResult(
            status=False,
            error="EXCEPTION >> WeatherApi::Weather >> Unknown exception has occurred!"
        )

def getResponseStatus(result):
    return result[RESPONSE_STATUS]

def getResponseData(result):
    return result[RESPONSE_DATA]

def getResponseError(result):
    return result[RESPONSE_ERROR]

def __createResult(status, data = None, error = None):
    result = {}

    result[RESPONSE_STATUS] = status
    if(data != None):
        result[RESPONSE_DATA] = data
    if(error != None):
        result[RESPONSE_ERROR] = error

    return result
