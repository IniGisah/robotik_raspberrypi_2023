 #!/usr/bin/python
from time import sleep
from matrix_keypad import RPi_GPIO
from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)
# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
GPIO.setup(segments, GPIO.OUT, initial=1)
 
# GPIO ports for the digit 0-3 pins 
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
GPIO.setup(digits, GPIO.OUT, initial=0)
 
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


def seg():
    for digit in range(4):
        GPIO.output(segments, (num[display_string[digit]]))
        GPIO.output(digits[digit], 1)
        time.sleep(0.001)
        GPIO.output(digits[digit], 0)
try:
    n = 99
    g = '123 '
    while n >= 0:
        display_string = str(n).rjust(4)
        if n == 0:
            display_string = g
        seg()
        n -= 1
    n = 1000
    while n >= 0:
        if n <= 500:
            display_string = '5678'
        seg()
        n -= 1
finally:
    GPIO.cleanup()

kp = RPi_GPIO.keypad(columnCount = 3)
def digit():
    r = None
    while r == None:
        r = kp.getKey()
    return r 
 
print ("Please enter a 4 digit code: ")
d1 = digit()
print (d1)
sleep(1)
 
d2 = digit()
print (d2)
sleep(1)
 
d3 = digit()
print (d3)
sleep(1)
 
d4 = digit()
print (d4)
print ("You Entered %s%s%s%s "%(d1,d2,d3,d4))

 