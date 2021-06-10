import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(18, GPIO.OUT)  #LED to GPIO24

try :
    while True:
        button_state = GPIO.input(17)
        if button_state == False:
            GPIO.output(18, True)
            print('Button Pressed...')
            time.sleep(0.2)
        else:
            GPIO.output(18, False)
except KeyboardInterrupt:
    print ("Berhenti dengan Ctrl+C")
finally :
    GPIO.cleanup()
