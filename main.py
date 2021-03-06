#   To check address: sudo i2cdetect -y 1

import smbus
import time

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

  def display(button):
    self.joystick

class Joystick:

  def __init__(button,chn):
    button.chn = PCF8591(chn)

  def getX(button):
   return button.chn.read(1)

  def getY(button):
    return button.chn.read(0)
  


while True:
  myJoystick = Joystick(0X48)
  print(myJoystick.getX(), " , ", myJoystick.getY())
  time.sleep(0.1)
