# Raspberry Pi Project(s)

All projects related/using to Raspberry Pi. Application is written using Python v3.
Status: In Development.

**Technologies Used:** Python v3.7.4

## Project(s)

### eink-weather-display

Displays weather data for preconfigured location. Updates are predefined intervals. eInk Weather display uses Raspberry Pi Zero and Waveshare eInk 2.7 inche Display.

#### Hardware Pre-requisites

1. Raspberry Pi Zero/3/4
2. Waveshare eInk Display HAT - Size 2.7 inches

#### Software Pre-requisites

1. Raspbian

#### Third Party Libraries

* pyyaml
* coloredlogs
* requests
* epd2in7b (Waveshare eInk Display driver)
* epdconfig (Waveshare eInk Display driver)
* spidev (A python module for interfacing with SPI devices from user space via the spidev linux kernel driver)
* RPi.GPIO (A package provides a class to control the GPIO on a Raspberry Pi)
* Pillow (Python Imaging Library [PIL] fork)

#### Setup

1.

#### Added feature list

1. Git Branch: "feature/001-basic-application-structure"
    1. Created a basic application structure
    2. Added Waveshare display python libraries
    3. Added logging configuration (logging.yaml) and logging support
2. Git Branch: "feature/002-added-weather-api"
    1. Added framework and INI configuration file for weather providers
    2. Integrated with [OpenWeatherMap](https://openweathermap.org/api) API
3. Git Branch: "feature/003-basic-display-support"
    1. Added Waveshare 2.7 inch eInk display support
    2. Added display specific INI configurations
    3. Refactored code for better organization, added contstants
    4. Created mock for epdconfig and RPi.GPIO for testing program logic on Windows platform
