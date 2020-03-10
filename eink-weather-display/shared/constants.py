#!/usr/bin/python
# -*- coding:utf-8 -*-

CONFIG_FILENAME = "eink-weather-display.ini"

CONFIG_DEFAULT = "default"
CONFIG_DEFAULT_WEATHER_PROVIDER = "weatherProvider"

CONFIG_OWM = "openWeatherMap"
CONFIG_OWM_API_URL = "apiUrl"
CONFIG_OWM_API_TOKEN = "apiToken"
CONFIG_OWM_LOCATION_CODE = "locationCode"
CONFIG_OWM_UNIT = "unit"
CONFIG_OWM_LANGUAGE = "language"
DEFAULT_OWM_LOCATION_CODE = 1277333 # Bengaluru
DEFAULT_OWM_UNIT = "metric"
DEFAULT_OWM_LANGUAGE = "en"

CONFIG_DISPLAY = "display"
CONFIG_DISPLAY_UPDATE_INTERVAL = "updateIntervalInSeconds"
CONFIG_DISPLAY_MAX_NUMBER_OF_DISPLAY_UPDATES = "maxNumberOfDisplayUpdates"
CONFIG_DISPLAY_FONT_HEADER = "fontHeader"
CONFIG_DISPLAY_FONT_BODY = "fontBody"
CONFIG_DISPLAY_FONT_FOOTER = "fontFooter"
DEFAULT_DISPLAY_UPDATE_INTERVAL = 60
DEFAULT_DISPLAY_MAX_NUMBER_OF_DISPLAY_UPDATES = -1


DICTIONARY_KEY_CONFIG_FILENAME = "configFileName"
DICTIONARY_KEY_DISPLAY_UPDATE_INTERVAL = CONFIG_DISPLAY_UPDATE_INTERVAL
DICTIONARY_KEY_MAX_NUMBER_OF_UPDATES = CONFIG_DISPLAY_MAX_NUMBER_OF_DISPLAY_UPDATES