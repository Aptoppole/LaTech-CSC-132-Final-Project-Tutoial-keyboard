from Tkinter import *

class App(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.currentscreen = "title"
    self.img = None
  
  def setBackground(self):
    #this function should put the images in the proper places
    if self.currentscreen == "title":
      self.img = PhotoImage(file="Title.gif")
  
  def createButtons(self):
    #this function should create the buttons for doing various things
    #like the "play" and various lesson buttons
    pass

  def setUpGUI(self):
    #this function compiles the GUI
    self.pack(fill=BOTH, expand=1)
    if self.currentscreen = "title":
      self.display = Label(self, text = "", anchor = E, bg = "white", height = 2, font=("TexGyreAdventor", 50))
  
  def process(self):
    #this should make the buttons do things
    pass
