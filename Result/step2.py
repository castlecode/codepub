import random
import radio
from microbit import button_a, Image, display, sleep

# Create an array with the three prepicked images to 
# use instead of stone, rock, scissor. By terminology we call these "tools"
tools = (Image.HEART, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'foo'
tool = 0

radio.on()

while True:
    if button_a.was_pressed():
        tool = random.randrange(3)
        display.clear()
        sleep(1000)
        # Show the randomly chosen tool on the Micro:bit
        display.show(tools[tool])
    
    # Broadcast your id and tool number (1, 2 or 3) 
    # as a string in a radio message, e.g. '10 1'
    radio.send('%s %s' % (my_id, tool))

    sleep(10)