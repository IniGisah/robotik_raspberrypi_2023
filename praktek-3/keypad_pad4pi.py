#install dulu librarynya pip install pad4pi
from pad4pi import rpi_gpio
KEYPAD = [
    [1, 2, 3,"A"],
    [4, 5, 6,"B" ],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

ROW_PINS = [5, 6, 13, 19] # BCM numbering
COL_PINS = [21, 20, 16,12] # BCM numbering

def print_key(key):
    print(key)

try:
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_4_by_3_keypad() # makes assumptions about keypad layout and GPIO pin numbers

    keypad.registerKeyPressHandler(print_key)

    print("Press buttons on your keypad. Ctrl+C to exit.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Goodbye")
finally:
    keypad.cleanup()
