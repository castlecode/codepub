import random
import radio
from microbit import accelerometer, Image, display, sleep, button_a

# Create an array with the three prepicked images to 
# use instead of stone, rock, scissor. By terminology we call these "tools"
tools = (Image.SKULL, Image.PITCHFORK, Image.PACMAN)

random.seed(463473567345343)
my_id = 'foo'
tool = 0
# A set to store other players id number
peers = set()
# An index for how many messages you have recieved
receives = 0

radio.on()

while True:
    if button_a.was_pressed():
        tool = random.randrange(3)
        #display.clear()
        #sleep(1000)
        # Show the randomly chosen tool on the Micro:bit
        #display.show(tool)
    
    display.clear()
    # Display how many other players have the same tool as you
    display.scroll('%s' % len(peers))
    # Show the randomly chosen tool on the Micro:bit
    display.show(tools[tool])

    # Randomly pick a sleep time between 200 - 500 ms
    sleep_time = random.randint(200, 500)
    print('sleep time: %s' % sleep_time)
    
    # Only send a message after you have recieved 10 messages, i.e. alternate 
    # sending recieving with a ratio of 1 in 10 messages.
    if receives >= 10:
        # Broadcast your id and tool number (1, 2 or 3) 
        # as a string in a radio message, e.g. 'foo 1'
        print('sending: %s %s' % (my_id, tool))
        radio.send('%s %s' % (my_id, tool))
        receives = 0

    # Collect recieved messages from other "players" on the radio
    incoming = radio.receive()
    receives += 1
    
    print(incoming)
    
    if incoming:
        # Store incoming message in 2 variables, their id and their tool number
        (their_id, their_tool) = incoming.split()
        
        # If the incoming tool number equals your own tool number add their id 
        # to the peers set otherwise discard their id from the peers set
        if int(their_tool) == tool:
            peers.add(their_id)
        else:
            peers.discard(their_id)

    print(peers)
    
    print('sleeping...')
    sleep(sleep_time)