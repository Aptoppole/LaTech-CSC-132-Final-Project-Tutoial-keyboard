from Tkinter import *

class App(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.currentscreen = "title"
    self.img = None
    self.dostuff()
  
  def setBackground(self):
    #this function should put the images in the proper places
    if self.currentscreen == "title":
      self.img = PhotoImage(file="Title.gif")
      creditButton = Button(self, bg="lightgray", text="Credits", width="50", height="25", self.process("Credits"))
      startButton = Button(self, bg="lightgray", text="Start", self.process("Start"))
      creditButton.pack(side=BOTTOM)
      startButton.pack(side=BOTTOM)
      
  def createButtons(self):
    #this function should create the buttons for doing various things
    #like the "play" and various lesson buttons
    pass

  def setUpGUI(self):
    #this function compiles the GUI
    self.pack(fill=BOTH, expand=1)
    App.image = Label(self, bg="white", width=WIDTH, height=HEIGHT, image=self.img)
    App.image.pack(side=TOP, fill=BOTH)
    App.image.pack_propagate(False)
      
  def process(self, thingy):
    #this should make the buttons do things
    if thingy == "Credits":
        pass
    elif thingy == "Start":
        pass
    else
        print "You piece of shit. What did you do?"
  
  def dostuff(self):
    self.setBackground()
    self.setUpGUI()

WIDTH = 800
HEIGHT = 480
window = Tk()
window.title("Piano Lessons")
window.geometry("{}x{}".format(WIDTH, HEIGHT))
app = App(window)
window.mainloop()

