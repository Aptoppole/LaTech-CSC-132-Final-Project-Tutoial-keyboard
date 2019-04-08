######################################################################################
# a test for our circuit
import RPi.GPIO as GPIO

gpio.setmode(gpio.BCM)
gpio.setup(switches, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(leds, gpio.OUT)

leds = []
switches = []

def play():
  pressed = False
  while True:
    for i in range(len(switches)):
      while GPIO.input(switches[i]):
        val = i
        pressed = True
        print("Yay")
