######################################################################################
# a test for our circuit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

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
