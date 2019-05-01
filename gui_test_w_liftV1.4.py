from Tkinter import *

class Page(Frame):
    def __init__(self, bg="white"):
        Frame.__init__(self)

    def show(self):
        self.lift()

class Titlescreen(Page):
    def __init__(self):
        Page.__init__(self)
        img = PhotoImage(file="Title.gif")
        self.image = Label(self, bg="white", image=img)
        self.image.image = img
        self.image.pack(side="top", fill="both", expand=True)

class Credit(Page):
    def __init__(self):
        Page.__init__(self)
        label = Label(self, text="Contributors: \n\n Jonah Fitzgerald, \n\n Alex Petty, \n\n Eddie Redmann")
        label.pack(side="top", fill="both", expand=True)

class Lessons(Page):
    def __init__(self):
        Page.__init__(self)
        for row in range(5):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(5):
            Grid.columnconfigure(self, col, weight=1)
        self.button1 = Button(self, bg = "lightgrey", text = "Lesson 1: Mary Had a Little Lamb")
        self.button1.grid(row = 1, column = 1, sticky = N+E+W+S)
        self.button2 = Button(self, bg = "lightgrey", text = "Lesson 2: Ode to Joy")
        self.button2.grid(row = 1, column = 3, sticky = N+E+W+S)
        self.button3 = Button(self, bg = "lightgrey", text = "Lesson 3: Freeplay")
        self.button3.grid(row = 3, column = 1, sticky = N+E+W+S)
        self.button4 = Button(self, bg = "lightgrey", text = "PLACEHOLDER")
        self.button4.grid(row = 3, column = 3, sticky = N+E+W+S)


class LessonOne(Page):
    def __init__(self):
        Page.__init__(self)
        
        
class PageCompiler(Frame):
    def __init__(self, master, bg = "white"):
        Frame.__init__(self, master)

        ts = Titlescreen()
        cs = Credit()
        ls =Lessons()

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        ts.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        cs.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ls.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
        bsb = Button(buttonframe, text="title", command=ts.lift)
        csb = Button(buttonframe, text="credits", command=cs.lift)
        lsb = Button(buttonframe, text="lessons", command=ls.lift)

        csb.pack(side="top")
        bsb.pack(side="left")
        lsb.pack(side="right")

        
    
        ts.show()

if __name__ == "__main__":
    window = Tk()
    window.title("Piano Lesson")
    program = PageCompiler(window)
    program.pack(side="top", fill="both", expand=True)
    window.wm_geometry("800x480")
    window.mainloop()
