from Tkinter import *

class App(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.master = master
    self.currentscreen = "title"
    self.img = None
    self.setBackground()
    self.creditButton = Button(self, bg="lightgray", text="Credits", command = lambda: self.process("Credits"))
    self.startButton = Button(self, bg="lightgray", text="Start", command = lambda: self.process("Start"))
    self.backButton = Button(self, bg="lightgrey", text="Back", command = lambda: self.process("Back"))
  
  def setBackground(self):
    #this function should put the images in the proper places
    self.pack(fill=BOTH, expand=1)
    if self.currentscreen == "title":
      self.img = PhotoImage(file="Title.gif")
      self.creditButton = Button(self, bg="lightgray", text="Credits", command = lambda: self.process("Credits"))
      self.startButton = Button(self, bg="lightgray", text="Start", command = lambda: self.process("Start"))
      self.creditButton.pack(side=BOTTOM, fill=X)
      self.startButton.pack(side=BOTTOM, fill=X)

      image = Label(self, bg="white", width=WIDTH, height=HEIGHT, image=self.img)
      image.pack(side=TOP, fill=BOTH)
      
    elif self.currentscreen == "credit":
      self.img = None
      
      text_frame = Frame(self, width=WIDTH)

      text = Text(text_frame, bg="lightgrey")
      text.pack(fill=BOTH, expand=1)
      text_frame.pack(side=TOP, fill=BOTH)
      text.insert(END, "Contributors: \n\n Jonah Fitzgerald, \n\n Alex Petty, \n\n Eddie Redmann")
      self.backButton.pack(side=BOTTOM, fill=X)

      text.config(state=DISABLED)
    elif self.currentscreen == "start":
      for row in range(9):
        Grid.rowconfigure(self, row, weight=1)
      for col in range(3):
        Grid.columnconfigure(self, col, weight=1)
      button1 = Button(self, bg = "lightgrey", text = "Lesson 1: Mary Had a Little Lamb", command = lambda: self.process("marylamb"))
      button1.grid(row = 1, column = 1, sticky = N+E+W+S)
      button2 = Button(self, bg = "lightgrey", text = "Lesson 2: Ode to Joy", command = lambda: self.process("odetojoy"))
      button2.grid(row = 3, column = 1, sticky = N+E+W+S)
      button3 = Button(self, bg = "lightgrey", text = "Lesson 3: The Third One", command = lambda: self.process("thethirdone"))
      button3.grid(row = 5, column = 1, sticky = N+E+W+S)
      self.backButton.grid(row=7, column=1, sticky = N+E+W+S)
      
  def process(self, prompt):
    #this should make the buttons do things
    if prompt == "Credits":
      global image
      self.currentscreen = "credit"
      self.creditButton.pack_forget()
      self.startButton.pack_forget()
      image.pack_forget()
    elif prompt == "Start":
      global creditButton, startButton, image
      self.currentscreen = "start"
      self.creditButton.pack_forget()
      startButton.pack_forget()
      self.image.pack_forget()
    elif prompt == "Back":
      global text, text_frame
      if self.currentscreen == "credit":
        self.backButton.pack_forget()
        text.pack_forget()
        text_frame.pack_forget()
        self.currentscreen = "title"
      elif self.currentscreen == "title":
        pass
      elif self.currentscreen == "start":
        pass
      self.currentscreen = "title"
    elif prompt == "marylamb":
      pass
    elif prompt == "odetojoy":
      pass
    elif prompt == "thethirdone":
      pass
    else:
      print "You piece of shit. What did you do?"
    self.setBackground()
class Lesson(object):
    def __init__(self, seq):
        self.seq = seq
        self.notes = [261.6256, 277.1826, 293.6648, 311.1270, 329.6276, 349.2282, 369.9944, 391.9954, 415.3047, 440, 466.1638, 493.8833, 523.2511]
        self.switches = []
        self.leds = []
        self.pictures = ["c.gif", "d.gif", "e.gif", "f.gif", "g.gif", "a.gif", "b.gif", "c2.gif"]
        
WIDTH = 800
HEIGHT = 480
window = Tk()
window.title("Piano Lessons")
window.geometry("{}x{}".format(WIDTH, HEIGHT))
app = App(window)
window.mainloop()
