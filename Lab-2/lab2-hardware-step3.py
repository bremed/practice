#This code will make use of the temperature sensor and the LEDS
from sense_hat import SenseHat
import time
from time import asctime

sense = SenseHat()

while True:
    temp = round(sense.get_temperature()*1.8+32)
    message = ' T=% dF ' %(temp)
    sense.show_message(message, scroll_speed=(0.08),text_colour=[100,200,150])
    time.sleep(4)