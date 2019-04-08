######################################################################################
# This file is for creating the lesson GUI. These be the libraries we used.
from Tkinter import *

######################################################################################
#the main part of the program
class Lesson(Frame):
  def __init__(self, master, activity, instructions):
    Frame.__init__(self, master)
    self.activity = activiity
    self.instrucitons = instructions
  
  def setUpGUI(self):
    #this function will display an activity and verify that it is done correctly
    #Alex and Jonah, I thought this function simplified our original design--Eddie
    self.instructions.grid(row=0, column=0, sticky=N+E+W)
    self.activity.grid(row=1, column=0, sticky=E+W+S)
  
######################################################################################
#main part of the gui program
length=800
width=800

A = Key("A", )
B = Key("B", )
C = Key("C", )
D = Key("D", )
E = Key("E", )
F = Key("F", )
G = Key("G", )
A2 = Key("A2", )

window = Tk()
window.title("Piano Teacher--Final Project for CSC 132")
window.geometry("{}X{}".format(length, width))
window.mainloop()
