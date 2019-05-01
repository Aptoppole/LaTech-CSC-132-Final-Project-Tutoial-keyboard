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
        self.image.pack(side="top", fill="both")

class PageCompiler(Frame):
    def __init__(self, master, bg = "white"):
        Frame.__init__(self, master)

        ts = Titlescreen()

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="bottom", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        ts.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
        tsb = Button(buttonframe, text="Title", command=ts.lift)

        tsb.pack(side="bottom")
    
        ts.show()

height = 480
width = 800
window = Tk()
window.title("Piano Lesson")
window.geometry("{}x{}".format(width, height))
program = PageCompiler(window)
program.pack(side=TOP, fill=BOTH)
window.mainloop()
        
