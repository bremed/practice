from sense_hat import SenseHat
import time

sense = SenseHat()
#colours
B = (0,0,255)
G = (0,255,0)
O = (0,0,0)
#Letter B

def b():
    logo = [
    O,O,B,B,B,O,O,O,
    O,O,B,O,O,B,O,O,
    O,O,B,O,O,B,O,O,
    O,O,B,B,B,O,O,O,
    O,O,B,B,B,O,O,O,
    O,O,B,O,O,B,O,O,
    O,O,B,O,O,B,O,O,
    O,O,B,B,B,O,O,O
    ]
    return logo
#Letter M

def m():
    
    logo = [
    O,G,O,O,O,O,G,O,
    O,G,G,O,O,G,G,O,
    O,G,O,G,G,O,G,O,
    O,G,O,O,O,O,G,O,
    O,G,O,O,O,O,G,O,
    O,G,O,O,O,O,G,O,
    O,G,O,O,O,O,G,O,
    O,G,O,O,O,O,G,O
    ]
    return logo

letters = [b,m]
count = 0
while True:
    events = sense.stick.get_events()
    if events:
        for event in events:
            if event.action != 'pressed':
                continue
            if event.direction == 'left':
                sense.set_pixels(letters[count % len(letters)]())
                count += 1
            elif event.direction == 'right':
                sense.set_pixels(letters[count % len(letters)]())
                count += 1
            elif event.direction == 'up':
                sense.set_pixels(letters[count % len(letters)]())
                count += 1
            elif event.direction == 'down':
                sense.set_pixels(letters[count % len(letters)]())
                count += 1
    
    
                                            