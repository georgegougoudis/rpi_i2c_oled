from __future__ import division
import logging
# import SSD1306.I2C as I2C
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106

SH1106_I2C_ADDRESS = 0x3C

class SH1106Base(object):
  def __init__(self, width, height, i2c_address=SH1106_I2C_ADDRESS, busnum=1):
    self._log = logging.getLogger('SH1106 Base constructor...')
    self.width = width
    self.height = height
    self._pages = height//8
    self._buffer = None
    self._address = i2c_address
    self._driver = None

    # Handle hardware I2C
    self._log.debug('Using hardware I2C with platform I2C provider.')
    self._bus = i2c(port=busnum, address=i2c_address)

  def command(self, c):
    """Send command byte to display."""
    self._driver.command(c)

  def begin(self, vccstate=None):
    self._driver = sh1106(self._bus)
    
  def display(self):
    """Write display buffer to physical display."""
    if self._buffer:
          self._driver.display(self._buffer)

  def image(self, image):
    """Set buffer to value of Python Imaging Library image.  The image should
    be in 1 bit mode and a size equal to the display size.
    """
    self._buffer = image

  def clear(self):
    self._driver.clear()


class SH1106_128_64(SH1106Base):
  def __init__(self, busnum=1, i2c_address=SH1106_I2C_ADDRESS):
    # Call base class constructor.
    super(SH1106_128_64, self).__init__(128, 64, i2c_address, busnum)
