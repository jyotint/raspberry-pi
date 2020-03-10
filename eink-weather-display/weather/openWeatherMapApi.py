#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests
from shared import constants
from shared import customException as ce
from .weatherData import WeatherData

# API Key from https://home.openweathermap.org/api_keys: eink-weather-display

class Weather(object):
    def __init__(self):
        self.apiUrl = None
        self.apiToken = None
        self.locationCode = None
        self.measurementUnit = None
        self.language = None
        self.configName = None
        self.initialized = False

    def readConfig(self, configDictionary):
        self.configName = configDictionary.name

        self.apiUrl = configDictionary.get(constants.CONFIG_OWM_API_URL)
        self.apiToken = configDictionary.get(constants.CONFIG_OWM_API_TOKEN)
        self.locationCode = configDictionary.get(constants.CONFIG_OWM_LOCATION_CODE, constants.DEFAULT_OWM_LOCATION_CODE)
        self.measurementUnit = configDictionary.get(constants.CONFIG_OWM_UNIT, constants.DEFAULT_OWM_UNIT)
        self.language = configDictionary.get(constants.CONFIG_OWM_LANGUAGE, constants.DEFAULT_OWM_LANGUAGE)
        self.locationName = ""
        self.weatherJson = ""
        self.weatherData = None

        self.validateParams()
        self.initialized = True

    def validateParams(self):
        if(self.apiUrl == None):
            raise ce.MissingConfigurationException(missingConfig=self.getConfigKeyName(constants.CONFIG_OWM_API_URL))
        if(self.apiToken == None):
            raise ce.MissingConfigurationException(missingConfig=self.getConfigKeyName(constants.CONFIG_OWM_API_TOKEN))
        if(self.locationCode == None):
            raise ce.MissingConfigurationException(missingConfig=self.getConfigKeyName(constants.CONFIG_OWM_LOCATION_CODE))

    def getConfigKeyName(self, key):
        return "{0}::{1}".format(self.configName, key)

    def queryWeather(self):
        if(self.initialized == False):
            raise ce.NotInitializedException(message="Initialize OpenWatherMapApi prior to using it!")

        api_headers = {
            "Content-Type": "application/json"
        }
        api_params = {
            "id": "{0}".format(self.locationCode),
            "lang": "{0}".format(self.language),
            "units": "{0}".format(self.measurementUnit),
            "appid": "{0}".format(self.apiToken)
        }

        rawResponse = requests.get(self.apiUrl, params=api_params, headers=api_headers)
        if(rawResponse.status_code != requests.codes.ok):
            # This means something went wrong.
            errorData = rawResponse.json()
            raise ce.ApiException(
                rawResponse.status_code,
                "GET: {0}".format(errorData["message"]))
        else:
            self.weatherJson = rawResponse.json()
            self.weatherData = self.decodeWeatherData(
                self.locationCode,
                self.measurementUnit,
                self.language,
                self.weatherJson)
            return True

    def decodeWeatherData(self, locationCode, unit, language, weatherJson):
        weatherData = WeatherData()
        weatherData.setUnitType(unit)

        weatherData.locationCode = weatherJson["id"]
        weatherData.locationName = weatherJson["name"]

        weatherData.lastUpdatedOn = weatherJson["dt"]
        weatherData.currentTemperature = weatherJson["main"]["temp"]
        weatherData.currentTemperatureFeelsLike = weatherJson["main"]["feels_like"]
        weatherData.minTemperature = weatherJson["main"]["temp_min"]
        weatherData.maxTemperature = weatherJson["main"]["temp_max"]
        weatherData.currentWeatherDescription = weatherJson["weather"][0]["description"]
        weatherData.currentBarometer = weatherJson["main"]["pressure"]
        weatherData.currentHumidity = weatherJson["main"]["humidity"]
        weatherData.currentWindSpeed = weatherJson["wind"]["speed"]
        weatherData.currentWindDirection = weatherJson["wind"]["deg"]
        # weatherData.currentUvLevel = weatherJson["main"]["temp"]
        # weatherData.currentUvText = weatherJson["main"]["temp"]

        weatherData.sunrise = weatherJson["sys"]["sunrise"]
        weatherData.sunset = weatherJson["sys"]["sunset"]

        return weatherData
