#!/home/chestnut/venv-piFarm/bin/python3

import RPi.GPIO as GPIO

gpio_outs = (22,18,16,15)
gpio_ins = (11,12)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#LED on pin 11
#switch on 12 as input
#Relay 1-4 = GPIO 22, 18, 16, 15 in that order
GPIO.setup(gpio_outs, GPIO.OUT)
GPIO.setup(gpio_ins, GPIO.IN)

def offAll():
    relays=[True, True, True, True]
    GPIO.output(gpio_outs[0],relays[0])
    GPIO.output(gpio_outs[1],relays[1])
    GPIO.output(gpio_outs[2],relays[2])
    GPIO.output(gpio_outs[3],relays[3])
def onAll():
    relays=[False, False, False, False]
    GPIO.output(gpio_outs[0],relays[0])
    GPIO.output(gpio_outs[1],relays[1])
    GPIO.output(gpio_outs[2],relays[2])
    GPIO.output(gpio_outs[3],relays[3])
def psuPower(state):
    #the relay board has pullup resistors in line so True = off
    if state == True:
        state = False
    else:
        state = True
    GPIO.output(gpio_outs[0], state)

def lightPower(state):
    #the relay board has pullup resistors in line so True = off
    if state == True:
        state = False
    else:
        state = True
    GPIO.output(gpio_outs[1], state)

def fanPower(state):
    #the relay board has pullup resistors in line so True = off
    if state == True:
        state = False
    else:
        state = True
    GPIO.output(gpio_outs[2], state)

def pumpPower(state):
    #the relay board has pullup resistors in line so True = off
    if state == True:
        state = False
    else:
        state = True
    GPIO.output(gpio_outs[3], state)



