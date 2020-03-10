# Raspberry Pi Project(s)

All projects related/using to Raspberry Pi. Application is written using Python v3.

**Technologies Used:** Python v3.7.4

## Project(s)

### eink-weather-display

Displays weather data for preconfigured location. Updates are predefined intervals. eInk Weather display uses Raspberry Pi Zero and Waveshare eInk 2.7 inche Display.

#### Setup

1.

#### Third Party Libraries

* pyyaml
* coloredlogs
* pywapi (Python wrapper around the Yahoo! Weather, Weather.com, and National Oceanic and Atmospheric Administration (NOAA) APIs)

#### Added feature list

1. Git Branch: "feature/001-basic-application-structure"
    1. Created a basic application structure
    2. Added Waveshare display python libraries
    3. Added logging configuration (logging.yaml) and logging support
2. Git Branch: "feature/002-added-weather-api"
    1. Added framework and INI configuration file for weather providers
    2. Integrated with [OpenWeatherMap](https://openweathermap.org/api) API
