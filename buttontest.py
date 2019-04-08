######################################################################################
# a test for our circuit
import Rpi.GPIO as GPIO

gpio.setmode(gpio.BCM)
gpio.setup(switches, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(leds, gpio.OUT)

leds = []
switches = []
sounds = [pg.mixer.Sound("")]

def play():
  pressed = False
  while True:
    
