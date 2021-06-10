#Menggunakan BOARD
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT, initial=GPIO.LOW)
try :
    while True :
       print ("LED on")
       GPIO.output(12,GPIO.HIGH)
       time.sleep(1)#satuannya detik
       print ("LED off")
       GPIO.output(12,GPIO.LOW)
       time.sleep(1)
finally :
    GPIO.cleanup()



