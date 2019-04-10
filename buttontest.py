######################################################################################
# a test for our circuit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.wPi)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

leds = [2, 3, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]
switches = [14, 13, 12, 10, 11, 4, 5, 6, 12, 13, 16, 17]

def play():
  pressed = False
  while True:
    for i in range(len(switches)):
      while GPIO.input(switches[i]):
        val = i
        pressed = True
        GPIO.OUT(leds[i])
      print("Yay")
