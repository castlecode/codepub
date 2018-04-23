import random
import radio
from microbit import accelerometer, Image, display, sleep, button_a

tools = (Image.SKULL, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'foo'
tool = 0
peers = set()

radio.on()

while True:
    #if accelerometer.was_gesture('shake'):
    if button_a.was_pressed():
        tool = random.randrange(3)
        #display.clear()
        #sleep(1000)
        #display.show(tool)
    
    display.clear()
    display.show(tools[tool])

    sleep_time = random.randint(200, 500)
    print('sleep time: %s' % sleep_time)
    
    print('sending: %s %s' % (my_id, tool))
    radio.send('%s %s' % (my_id, tool))

    incoming = radio.receive()
    
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

    display.clear()
    display.scroll('%s' % len(peers))
    
    print('sleeping...')
    sleep(sleep_time)
