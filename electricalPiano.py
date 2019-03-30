#####################################################################################
#the various libraries we've imported for this project
from Tkinter import *
import RPi.GPIO as GPIO

#####################################################################################
#this is the key class that creates the various keys
class key(object):
  def __init__(self, note):
    self.note = note
    self.pressed = False
    self.leds = []
  
  def make_noise(self):
    #plays the various notes on the keyboard
    pass
  
  def light_up(self):
    #lights up appropriate LEDs
    pass

class lesson(Frame):
  def __init__(self, master, activity, instructions):
    Frame.__init__(self, master)
    self.activity = activiity
    self.instrucitons = instructions
  
  def setUpGUI(self):
    #this function will display an activity and verify that it is done correctly
    #Alex and Jonah, I thought this function simplified our original design--Eddie
    self.instructions.grid(row=0, column=0, sticky=N+E+W)
    self.activity.grid(row=1, column=0, sticky=E+W+S)
    pass
  
  def compileLesson(self):
    #this function should light up the leds that need to be pressed
    pass

######################################################################################
#the main function of the program that compiles most of the program
def main_function(array):
  for i in range(len(array)):
    #play the sounds and light up the LEDs
  pass
  
######################################################################################
#main part of the gui program
length=800
width=800

window = Tk()
window.title("Piano Teacher--Final Project for CSC 132")
window.geometry("{}X{}".format(length, width))
window.mainloop()
