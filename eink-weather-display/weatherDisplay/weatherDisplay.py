#!/usr/bin/python
# -*- coding:utf-8 -*-

from waveshareLibs import epd2in7b
import time
import traceback
from PIL import Image,ImageDraw,ImageFont
from shared import logger
from display.eInkDisplayWaveshare0270 import Display


class WeatherDisplay(object):

    def __init__(self, configData):
        logger.setupLogging()
        self.log = logger.getLogger(__name__)

        self.log.info("WeatherDisplay::init() >> Initializing WeatherDisplay object...")
        self.display = Display(configData)
        self.log.info("WeatherDisplay::init() >> Initializing WeatherDisplay object - DONE.")


    def __del__(self):
        self.log.info("WeatherDisplay::del() >> Destroying WeatherDisplay object...")
        self.log.info("WeatherDisplay::del() >> Destroying WeatherDisplay object - DONE.")


    def displayWeather(self, weatherData):
        result = False

        self.log.debug("WeatherDisplay::displayWeather() >> Getting weather update at {}".format(self.formatDateTimeForLogging(time.localtime())))
        #3 weatherData = self.weatherApi
        display = self.display

        if(weatherData == None):
            self.log.error("WeatherDisplay::displayWeather() >> Error getting weatherData from API!")
            result = False
        else:
            self.log.debug("WeatherDisplay::displayWeather() >> Updating the display with weatherData...")
            display.clear()
            display.writeHeaderText("%s%s at %s" %(weatherData.currentTemperature, weatherData.unitTemperature, weatherData.locationName))

            display.writeBodyText("%s feels like %s%s" %(weatherData.currentWeatherDescription, weatherData.currentTemperatureFeelsLike, weatherData.unitTemperature))

            display.writeFooterText("UV radiation is %s at %s" %(weatherData.currentUvText, weatherData.currentUvLevel))
            display.writeFooterText("Wind speed is %s%s in %s direction" %(weatherData.currentWindSpeed, weatherData.unitSpeed, weatherData.currentWindDirection))
            display.writeFooterText("Humidity is %s%%" %(weatherData.currentHumidity))
            display.writeFooterText("Barometric pressure is %s %s" %(weatherData.currentBarometer, weatherData.unitPressure))
            display.writeFooterText(" ")
            display.writeFooterText("Display updated at %s" %(self.formatDateTimeForUser(time.localtime())))
            display.writeFooterText("Weather updated at %s" %(weatherData.lastUpdatedOn))

            display.displayBuffer()
            self.log.debug("Updating the display with weatherData - DONE.")
            result = True

        return result

    def formatDateTimeForUser(self, datetime):
        return time.strftime("%a, %d %b %Y %H:%M:%S", datetime)

    def formatDateTimeForLogging(self, datetime):
        return time.strftime("%Y-%m-%d %H:%M:%S", datetime)

    def testDisplay01(self):
        self.log.info("WeatherDisplay::testDisplay01() >> Writing text #1 to the display")
        self.display.writeBodyText("testing 1")
        self.display.displayBuffer()
        self.log.debug("WeatherDisplay::testDisplay01() >> Sleeping for 2 seconds")
        time.sleep(2)

        self.display.clear()
        self.log.debug("WeatherDisplay::testDisplay01() >> Writing text #2 to the display")
        self.display.writeBodyText("testing 2")
        self.log.debug("WeatherDisplay::testDisplay01() >> Writing current date-time to the display")
        self.display.writeCurrentDateTime()
