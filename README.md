# Rock, paper, scissor
This is a 4-step workshop for learning how to program with a Micro:bit,
the steps we will go through are:

* Part 1: create images (SKULL, PITCHFORK, PACMAN) and display one of 
them randomly each time you press button A.
* Part 2: send out an unique id and image number (0, 1 or 2) in a radio 
message.
* Part 3: add so you can also receive others message and identify if their 
image is the same as yours. count all players that have same image as you 
and alternate between displaying the image and this number on the board.
* Part 4: General improvements

## Compile and load binary image
Write code in your choice of editor or directly in the live editor
[editor](http://python.microbit.org/v/1). When ready to compile load script 
into the live editor and press *Download* this will produce a .hex file.
Connect Micro:bit to computer. Drag and drop the .hex file to the Micro:bit 
drive, the program you just wrote will now be flashed into the device. 

## Debug
Plug in Micro:bit, check which port the Micro:bit is connected to in a terminal
```
ls /dev
```
Then debug in screen (if you have a Mac or Linux computer) by running 

```
screen /dev/<name of port> 115200
```
in an open terminal. If you have a Windows computer follow [these](https://www.microbit.co.uk/td/serial-library) instructions.

### Useful screen commands
```
Kill terminal   *ctrl+a k*
Detach terminal	*ctrl+a d*
Attach terminal	*ctrl+a a*
```
