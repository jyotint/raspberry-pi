#Mock01
# Mocking GPIO for running application on Windows platform

# import spidev
# import RPi.GPIO as GPIO
import time

# Pin definition
RST_PIN         = 17
DC_PIN          = 25
CS_PIN          = 8
BUSY_PIN        = 24

# SPI device, bus = 0, device = 0
# SPI = spidev.SpiDev(0, 0)

def digital_write(pin, value):
    pass

def digital_read(pin):
    pass

def delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_writebyte(data):
    pass

def module_init():
    return 0

### END OF FILE ###
