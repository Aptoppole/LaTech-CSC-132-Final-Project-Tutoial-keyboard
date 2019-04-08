#####################################################################################
#the various libraries we've imported for this project
from Tkinter import *
import RPi.GPIO as GPIO
import pygame as pg
from sys import exit
from time import sleep
#####################################################################################
#various setup things for GPIO etc.
gpio.setmode(gpio.BCM)
gpio.setup(switches, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(leds, gpio.OUT)

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
          while gpio.input(self.switch) == True:
            val = i
            pressed = True
            sounds[val].play()
            gpio.output(leds[val], True)
    
    except KeyboardInterrupt:
      GPIO.cleanup()
      exit(0) 
      
