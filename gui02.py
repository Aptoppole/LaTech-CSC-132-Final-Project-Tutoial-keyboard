from Tkinter import *

class Window(Frame):
  def __init__(self, master):
    Frame.__init__(self, master, bg="white")
    self.currentscreen = "startMenu"
    self.setUpGrid()
  
  def setUpGrid(self):
    for row in range(6):
      Grid.rowconfigure(self, row, weight=1)
    for col in range(2):
      Grid.columnconfigure(self, col, weight=1)
  
  def screensetup(self):
    if self.currentscreen == "startMenu":
      button1 = Button(self, bg = "lightgrey", text = "Lesson 1: Mary Had a Little Lamb", command = lambda: self.process("marylamb"))
      button1.grid(row = 1, column = 1, sticky = N+E+W+S)
      button2 = Button(self, bg = "lightgrey", text = "Lesson 2: Ode to Joy", command = lambda: self.process("odetojoy"))
      button2.grid(row = 3, column = 1, sticky = N+E+W+S)
      button3 = Button(self, bg = "lightgrey", text = "Lesson 3: The Third One", command = lambda: self.process("thethirdone"))
      button3.grid(row = 5, column = 1, sticky = N+E+W+S)
      
window = Tk()
WIDTH = 800
HEIGHT = 480
window.geometry("{}x{}".format(WIDTH, HEIGHT))
app = Window(window)
window.mainloop()
