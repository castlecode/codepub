import random
import radio
from microbit import button_a, Image, display, sleep

# Create an array with the three prepicked images to 
# use instead of stone, rock, scissor. By terminology we call these "tools"
tools = (Image.HEART, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'foo'
tool = 0

while True:
    if button_a.was_pressed():
        tool = random.randrange(3)
        display.clear()
        sleep(1000)
        # Show the randomly chosen tool on the Micro:bit
        display.show(tools[tool])
    
    sleep(10)