import random
import radio
from microbit import accelerometer, Image, display, sleep

tools = (Image.SKULL, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'foo'
tool = 0

while True:
    if accelerometer.was_gesture('shake'):
        tool = tools[random.randrange(3)]
        display.clear()
        sleep(1000)
        display.show(tool)
    
    sleep(10)
