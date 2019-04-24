from Tkinter import *

class App(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.master = master
    self.currentscreen = "title"
    self.img = None
    self.setBackground()
  
  def setBackground(self):
    #this function should put the images in the proper places
    self.pack(fill=BOTH, expand=1)
    if self.currentscreen == "title":
      global creditButton, startButton, image
      self.img = PhotoImage(file="Title.gif")
      creditButton = Button(self, bg="lightgray", text="Credits", command = lambda: self.process("Credits"))
      startButton = Button(self, bg="lightgray", text="Start", command = lambda: self.process("Start"))
      creditButton.pack(side=BOTTOM, fill=X)
      startButton.pack(side=BOTTOM, fill=X)

      image = Label(self, bg="white", width=WIDTH, height=HEIGHT, image=self.img)
      image.pack(side=TOP, fill=BOTH)
      
    elif self.currentscreen == "credit":
      global backButton, text, text_frame
      self.img = None
      
      text_frame = Frame(self, width=WIDTH)

      text = Text(text_frame, bg="lightgrey")
      text.pack(fill=BOTH, expand=1)
      text_frame.pack(side=TOP, fill=BOTH)
      text.insert(END, "Contributors: \n\n Jonah Fitzgerald, \n\n Alex Petty, \n\n Eddie Redmann")
      backButton = Button(self, bg="lightgrey", text="Back", command = lambda: self.process("Back"))
      backButton.pack(side=BOTTOM, fill=X)

      text.config(state=DISABLED)
  def process(self, prompt):
    #this should make the buttons do things
    if prompt == "Credits":
      global creditButton, startButton, image
      self.currentscreen = "credit"
      creditButton.pack_forget()
      startButton.pack_forget()
      image.pack_forget()
    elif prompt == "Start":
      self.currentscreen = "start"
    elif prompt == "Back":
      global backButton, text, text_frame
      self.currentscreen = "title"
      backButton.pack_forget()
      text.pack_forget()
      text_frame.pack_forget()
    else:
      print "You piece of shit. What did you do?"
    self.setBackground()

WIDTH = 800
HEIGHT = 480
window = Tk()
window.title("Piano Lessons")
window.geometry("{}x{}".format(WIDTH, HEIGHT))
app = App(window)
window.mainloop()

