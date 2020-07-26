import random
import radio
from microbit import accelerometer, Image, display, sleep, button_a

tools = (Image.HEART, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'thommy'
tool = 0
peers = set()
receives = 0
toggle = 0

radio.on()
radio.config(channel=9)

while True:
    if button_a.was_pressed():
        tool = random.randrange(3)
    
    sleep_time = random.randint(200, 500)
    print('sleep time: %s' % sleep_time)
    
    if receives >= 10:
        print('sending: %s %s' % (my_id, tool))
        radio.send('%s %s' % (my_id, tool))
        receives = 0
        
        if toggle:
            display.show('%s' % len(peers))
        else:
            display.show(tools[tool])
            
        toggle = not toggle

    incoming = radio.receive()
    receives += 1
    
    print(incoming)
    
    if incoming:
        (their_id, their_tool) = incoming.split()
        
        if int(their_tool) == tool:
            peers.add(their_id)
        else:
            peers.discard(their_id)

    print(peers)

    print('sleeping...')
    sleep(sleep_time)