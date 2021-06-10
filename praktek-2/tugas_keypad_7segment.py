from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0]
]
num = {' ':(1,1,1,1,1,1,1),
    '0':(0,0,0,0,0,0,1),
    '1':(1,0,0,1,1,1,1),
    '2':(0,0,1,0,0,1,0),
    '3':(0,0,0,0,1,1,0),
    '4':(1,0,0,1,1,0,0),
    '5':(0,1,0,0,1,0,0),
    '6':(0,1,0,0,0,0,0),
    '7':(0,0,0,1,1,1,1),
    '8':(0,0,0,0,0,0,0),
    '9':(0,0,0,0,1,0,0)}

ROW_PINS = [5, 6, 13, 19] # BCM numbering
COL_PINS = [21, 20, 16,12] # BCM numbering
# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)
 
# GPIO ports for the digit 0-3 pins 
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)
factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

char=[' ',' ',' ',' ']
def store_key(key):
      global char
      if key == "*" :
          char=[' ',' ',' ',' ']
      else :
          char[0]=char[1]
          char[1]=char[2]
          char[2]=char[3]
          char[3]=key
    

keypad.registerKeyPressHandler(store_key)

try :
  while True :
    for digit in range(4):
        listToStr = ''.join(map(str, char))
        for loop in range(0,7):
            GPIO.output(segments[loop], num[listToStr[digit]][loop])
        GPIO.output(digits[digit], 1)
        time.sleep(0.001)
        GPIO.output(digits[digit], 0)
finally:
    GPIO.cleanup()