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
  def __init__(self, master, activity, quiz, instructions):
    Frame.__init__(self, master)
    self.activity = activiity
    self.quiz = quiz
    self.instrucitons = instructions
    
  def update(self):
    #this function will blank the screen
    pass 
  
  def setUpGUI(self):
    #this function will display an activity and verify that it is done correctly
    self.instructions.grid(row=0, column=0, sticky=N+E+W)
    self.activity.grid(row=1, column=0, sticky=E+W+S)
    pass
  
  def showQuiz(self):
    #this function will display the 
    pass

  
######################################################################################
#main part of the gui program
length=800
width=800

window = Tk()
window.title("Piano Teacher--Final Project for CSC 132")
window.geometry("{}X{}".format(length, width))
window.mainloop()
