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
    def __init__(self, l1, l2, l3, l4):
        Page.__init__(self)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        
        for row in range(5):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(5):
            Grid.columnconfigure(self, col, weight=1)
        self.button1 = Button(self, bg = "lightgrey", text = "Lesson 1: Mary Had a Little Lamb", command=self.l1.lift)
        self.button1.grid(row = 1, column = 1, sticky = N+E+W+S)
        self.button2 = Button(self, bg = "lightgrey", text = "Lesson 2: Ode to Joy", command=self.l2.lift)
        self.button2.grid(row = 1, column = 3, sticky = N+E+W+S)
        self.button3 = Button(self, bg = "lightgrey", text = "Lesson 3: Freeplay", command=self.l3.lift)
        self.button3.grid(row = 3, column = 1, sticky = N+E+W+S)
        self.button4 = Button(self, bg = "lightgrey", text = "Lesson 4: PLACEHOLDER", command=self.l4.lift)
        self.button4.grid(row = 3, column = 3, sticky = N+E+W+S)


class LessonOne(Page):
    def __init__(self):
        Page.__init__(self)
        label = Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)
############################ BUGED NEED FIX ###################################################
##        self.button1 = Button(self, bg="lightgrey", text = "next page", command=self.nextPage())
##        self.button1.grid(row=1, column=2, sticky = N+E+W+S)
##        
##        
##    def nextPage(self):
##        self.pack_forget()
##        self.pageNum += 1
##        self.pageUpdate()
##
##    def backPage(self):
##        if (self.pageNum == 1):
##            pass
##        else:
##            self.pack_forget()
##            self.pageNum -= 1
##            self.pageUpdate()
##
##    def exitLesson(self):
##        self.pack_forget()
##
##    def pageUpdate(self):
##        if (self.pageNum==1):
##            print ("1")
##            self.label = Label(self, text="This is page 1.1")
##            self.label.pack(side="top", fill="both", expand=True)
##        elif (self.pageNum==2):
##            print ("2")
##            self.label = Label(self, text="This is page 1.2")
##            self.label.pack(side="top", fill="both", expand=True)
##        elif (self.pageNum==3):
##            print ("3")
##            self.label = Label(self, text="This is page 1.3")
##            self.label.pack(side="top", fill="both", expand=True)
##        else:
##            pass


class LessonTwo(Page):
    def __init__(self):
        Page.__init__(self)
        label = Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)

class LessonThree(Page):
    def __init__(self):
        Page.__init__(self)
        label = Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)

class LessonFour(Page):
    def __init__(self):
        Page.__init__(self)
        label = Label(self, text="This is page 4")
        label.pack(side="top", fill="both", expand=True)
        
class PageCompiler(Frame):
    def __init__(self, master, bg = "white"):
        Frame.__init__(self, master)

        ts = Titlescreen()
        cs = Credit()
        l1 = LessonOne()
        l2 = LessonTwo()
        l3 = LessonThree()
        l4 = LessonFour()
        ls =Lessons(l1,l2,l3,l4)
        

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        ts.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        cs.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ls.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        l1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        l2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        l3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        l4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
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

