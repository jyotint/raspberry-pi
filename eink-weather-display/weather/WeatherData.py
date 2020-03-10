#!/usr/bin/python
# -*- coding:utf-8 -*-

class WeatherData(object):
    def __init__(self):
        self.locationCode = ""
        self.locationName = ""

        self.unit = ""
        self.unitDistance = ""
        self.unitPressure = ""
        self.unitRainfall = ""
        self.unitSpeed = ""
        self.unitTemperature = ""

        self.lastUpdatedOn = ""
        self.currentTemperature = 0
        self.currentTemperatureFeelsLike = 0
        self.minTemperature = 0
        self.maxTemperature = 0
        self.currentWeatherDescription = ""
        self.currentBarometer = 0.0
        self.currentHumidity = 0
        self.currentWindSpeed = 0
        self.currentWindDirection = 0
        self.currentUvLevel = ""
        self.currentUvText = ""

        self.sunrise = ""
        self.sunset = ""
        # self.day = ["", "", "", ""]
        # self.icon = [0, 0, 0, 0]
        # self.rain = ["", "", "", ""]
        # self.temps = [["", ""], ["", ""], ["", ""], ["", ""]]

    def setUnitType(self, unitType):
        self.unit = unitType
        if(unitType == "metric"):
            self.unitDistance = ""
            self.unitPressure = "hPa"
            self.unitRainfall = ""
            self.unitSpeed = "meters/sec"
            self.unitTemperature = "C"
        elif(unitType == "default"):
            self.unitDistance = ""
            self.unitPressure = "hPa"
            self.unitRainfall = ""
            self.unitSpeed = "meters/sec"
            self.unitTemperature = "K" # "Kelvin"
        elif(unitType == "imperial"):
            self.unitDistance = ""
            self.unitPressure = "hPa"
            self.unitRainfall = ""
            self.unitSpeed = "miles/sec"
            self.unitTemperature = "F"
        else:
            self.unitDistance = ""
            self.unitPressure = ""
            self.unitRainfall = ""
            self.unitSpeed = ""
            self.unitTemperature = ""

    def __str__(self):
        return "Code: '{0}', Name: '{1}', Unit: '{2}', LastUpdatedOn: '{3}', Temperature: {4}, TemperatureFeelsLike: {5}, MinTemperature: {6}, MaxTemperature: {7}, Description: '{8}', Barometer: {9}, Humidity: {10}, WindSpeed: {11}, WindDirection: {12}, Sunrise: {13}, Sunset: {14}, UnitDistance: '{15}', UnitPressure: '{16}', UnitRainfall: '{17}', UnitSpeed: '{18}', UnitTemperature: '{19}'".format(
            self.locationCode,
            self.locationName,
            self.unit,
            self.lastUpdatedOn,
            self.currentTemperature,
            self.currentTemperatureFeelsLike,
            self.minTemperature,
            self.maxTemperature,
            self.currentWeatherDescription,
            self.currentBarometer,
            self.currentHumidity,
            self.currentWindSpeed,
            self.currentWindDirection,
            self.sunrise,
            self.sunset,
            self.unitDistance,
            self.unitPressure,
            self.unitRainfall,
            self.unitSpeed,
            self.unitTemperature,
        )
