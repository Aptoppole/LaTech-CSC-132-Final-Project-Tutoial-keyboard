#####################################################################################
#the various libraries we've imported for this project
import RPi.GPIO as GPIO
import pygame as pg
from sys import exit
from time import sleep
#####################################################################################
#various setup things for GPIO etc.
GPIO.setmode(GPIO.BCM)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

leds = []
switches = []
sounds = [pg.mixer.Sound("")]
#####################################################################################
#this is the key class that creates the various keys
class Key(object):
  def __init__(self, note, led, switch, sound):
    self.note = note
    self.pressed = False
    self.led = led
    self.switch = switch
    self.sound = sound
   
  def play(self):
    #lights up appropriate LEDs
    pressed = False
    try:
      while True:
        while not pressed:
          while GPIO.input(self.switch) == True:
            val = i
            pressed = True
            sounds[val].play()
            GPIO.output(leds[val], True)
    
    except KeyboardInterrupt:
      GPIO.cleanup()
      exit(0) 
      
