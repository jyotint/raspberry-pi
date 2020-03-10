#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import traceback
from waveshareLibs import epd2in7b
from PIL import Image,ImageDraw,ImageFont
from shared import logger
from shared import constants


class Display(object):

    def __init__(self, configData):
        try:
            logger.setupLogging()
            self.log = logger.getLogger(__name__)

            self.log.info("Display::init() >> Initializing Display object...")
            # self.canvasX = 5
            # self.canvasY = 2
            self.fontSizeHeader = 20
            self.lineSpacingHeader = 5
            self.fontSizeBody = 16
            self.lineSpacingBody = 2
            self.fontSizeFooter = 12
            self.lineSpacingFooter = 2

            self.fontHeader = ImageFont.truetype(configData[constants.CONFIG_DISPLAY_FONT_HEADER], self.fontSizeHeader)
            self.fontBody = ImageFont.truetype(configData[constants.CONFIG_DISPLAY_FONT_BODY], self.fontSizeBody)
            self.fontFooter = ImageFont.truetype(configData[constants.CONFIG_DISPLAY_FONT_FOOTER], self.fontSizeFooter)


            # eInkDisplay initialization
            self.epd = epd2in7b.EPD()
            self.epd.init()
            # self.log.debug("Display::init() - Clearing eInkDisplay...")
            # self.epd.Clear(0xFF)
            # self.log.debug("Display::init() - Cleared eInkDisplay.")
            # Its developer's responsibility to clear the display before writing
            # self.clear()

            # Drawing on the Horizontal image
            self.log.debug("Display::init() >> Horizontal black/red image...")
            self.HBlackimage = Image.new("1", (epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH), 255)  # 298*126
            self.HRedimage = Image.new("1", (epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH), 255)  # 298*126

            self.log.debug("Display::init() >> Drawing...")
            self.canvasBlack = ImageDraw.Draw(self.HBlackimage)
            self.canvasRed = ImageDraw.Draw(self.HRedimage)

        except:
            self.log.error("Display::init() >> traceback.format_exc():\n%s",traceback.format_exc())
            exit()
        finally:
            self.log.info("Display::init() >> Initializing Display object - DONE.")


    def __del__(self):
        self.log.info("Display::del() >> Destroying object...")
        self.log.debug("Display::del() >> Final sleep.")
        self.epd.sleep()
        self.log.info("Display::del() >> Destroying object - DONE.")


    def clear(self):
        self.log.info("Display::clear() >> Clearing Display...")
        self.canvasX = 5
        self.canvasY = 2

        self.log.debug("Display::clear() >> Clearing epd...")
        self.epd.init()
        self.epd.Clear(0xFF)
        self.log.debug("Display::clear() >> Cleared epd.")
        self.log.info("Display::clear() >> Clearing Display - DONE.")


    def writeHeaderText(self, message):
        currentFont = self.fontHeader
        self.canvasRed.text((self.canvasX, self.canvasY), message, font = currentFont, fill = 0)
        self.canvasY += currentFont.getsize(message)[1] + self.lineSpacingHeader
        self.log.debug("Display::writeHeaderText() >> Current font height is {}".format(currentFont.getsize(message)[1]))


    def writeBodyText(self, message):
        currentFont = self.fontBody
        self.canvasBlack.text((self.canvasX, self.canvasY), message, font = currentFont, fill = 0)
        self.canvasY += currentFont.getsize(message)[1] + self.lineSpacingBody
        self.log.debug("Display::writeBodyText() >> Current font height is {}".format(currentFont.getsize(message)[1]))


    def writeFooterText(self, message):
        currentFont = self.fontFooter
        self.canvasBlack.text((self.canvasX, self.canvasY), message, font = currentFont, fill = 0)
        self.canvasY += currentFont.getsize(message)[1] + self.lineSpacingFooter
        self.log.debug("Display::writeFooterText() >> Current font height is {}".format(currentFont.getsize(message)[1]))


    def writeCurrentDateTime(self):
        message = "Current Date Time"
        self.writeHeaderText(message)

        message = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        self.writeBodyText(message)


    def displayBuffer(self):
        self.log.info("Display::displayBuffer() >> Displaying final buffer...")
        self.epd.display(self.epd.getbuffer(self.HBlackimage), self.epd.getbuffer(self.HRedimage))

        # self.log.debug("Display::displayBuffer() >> Sleeping for 2 seconds")
        # self.time.sleep(2)

        self.log.debug("Display::displayBuffer() >> Setting display to sleep until next update...")
        self.epd.sleep()
        self.log.info("Display::displayBuffer() >> Displaying final buffer - DONE.")
