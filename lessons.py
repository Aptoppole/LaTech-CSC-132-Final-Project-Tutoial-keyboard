from Tkinter import *
import pygame as pg
import RPi.GPIO as GPIO
from array import array
from threading import Thread
from time import sleep

mixer_freq = 44100
mixer_size = -16
mixer_chans = 1
mixer_buff = 1024

GPIO.setmode(GPIO.BCM)
pg.mixer.pre_init(mixer_freq, mixer_size, mixer_chans, mixer_buff)
pg.init()

class Page(Frame):
    def __init__(self, bg="white"):
        Frame.__init__(self)

    def show(self):
        self.lift()
        
class Lesson(Page):
  def __init__(self):
    Page.__init__(self)
    self.freqs = [261.6256, 277.1826, 293.6648, 311.1270, 329.6276, 349.2282, 369.9944, 391.9954, 415.3047, 440, 466.1638, 493.8833]
    self.switches = [11, 9, 10, 8, 7, 4, 5, 6, 12, 13, 16, 17]
    self.leds = [2, 3, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18]
    self.notes = []
    self.pictures = ["c.gif", "csharp.gif", "d.gif", "dsharp.gif", "e.gif", "f.gif", "fsharp.gif", "g.gif", "gsharp.gif", "a.gif", "asharp.gif", "b.gif"]
    self.pictures2 = ["c2.gif", "csharp2.gif", "d.gif", "dsharp2.gif", "e.gif", "f.gif", "fsharp2.gif", "g.gif", "gsharp2.gif", "a2.gif", "asharp2.gif", "b.gif"]
    GPIO.setup(self.switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(self.leds, GPIO.OUT)

    for i in range(len(self.freqs)):
        self.notes.append(Note(self.freqs[i], 1))

class Note(pg.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pg.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(mixer_freq / self.frequency))
        amplitude = 2 ** (abs(mixer_size) -1) -1
        samples = array("h", [0] * period)

        for t in range(period):
            if t <= (period/4):
                samples[t] = (amplitude*4*t)/(period) 
            elif t > (period/4) and t <= (period*.75):
                samples[t] = -((amplitude*t*4)/(period))+(2*amplitude)
            else:
                samples[t] = (4*amplitude*t)/(period) - (4*amplitude)

        return samples

    def set_volume(self, vol):
        pass
    
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


class LessonOne(Lesson):
    def __init__(self):
        Lesson.__init__(self)
########################## BUGGED, NEED TO FIX ###################################################
        self.pageNum = 0
        self.button1 = Button(self, bg="lightgrey", text = "Next", command=lambda:self.nextPage())
        self.button1.pack(side="right", expand=False)

        self.button2 = Button(self, bg="lightgrey", text = "Back", command=lambda:self.backPage())
        self.button2.pack(side="left", expand=False)
        self.label = Label(self, text="Welcome to our interactive piano. In this lesson,\n"\
                           "we aim to familiarize you with the various keys on the keyboard.\n"\
                           "Press the 'Next' button at the top of your screen to start the lesson.")
        self.label.pack(side="top", fill="both", expand=True)
        self.val = 0
        
    def nextPage(self):
        self.label.pack_forget()
        self.pageNum += 1
        self.pageUpdate()

    def backPage(self):
        if (self.pageNum == 1):
            pass
        else:
            self.label.pack_forget()
            self.pageNum -= 1
            self.pageUpdate()

    def pageUpdate(self):
        t1 = Thread(target=self.check_input())
        t2 = Thread(target=self.setUpGUI())

        t1.start()
        t2.start()
        
    def setUpGUI(self):
        if (self.pageNum==1):
            self.val = self.check_input()
            if GPIO.input(self.switches[self.val]) == False:
                img = PhotoImage(file=self.pictures[self.val])
                img2 = PhotoImage(file=self.pictures2[self.val])
                self.label = Label(self, width=400, image=img)
                self.label.image = img
                self.label.pack(side="left", fill="both", expand=True)
                self.label2 = Label(self, width=400, image = img)
                self.label2.image = img2
                self.label2.pack(side="right", fill="both", expand=True)
            self.label.pack_forget()
            self.label2.pack_forget()                    
                
        elif (self.pageNum==2):
            self.label = Label(self, text="This is page 1.2")
            self.label.pack(side="top", fill="both", expand=True)
        elif (self.pageNum==3):
            self.label = Label(self, text="This is page 1.3")
            self.label.pack(side="top", fill="both", expand=True)
            self.label = Label(self, text="Congratulations. You have completed our tutorial.")
            self.label.pack(side="top", fill="both", expand=True)

    def check_input(self):
        if self.pageNum == 1:
            for i in range(len(self.switches)):
                val=i
                while GPIO.input(self.switches[val]) == False:
                    GPIO.output(self.leds[val], GPIO.HIGH)
                GPIO.output(self.leds[val], GPIO.LOW)
                while GPIO.input(self.switches[val]) == True:
                    self.notes[val].play(-1)
                self.notes[val].stop()
            return val
        else:
            pass

class LessonTwo(Lesson):
    def __init__(self):
        Lesson.__init__(self)
        label = Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)

class LessonThree(Lesson):
    def __init__(self):
        Lesson.__init__(self)
        self.label = Label(self, text="Press the 'Start Freeplay Button' to start Freeplay and"\
                           "'Ctrl' + 'C' to exit Freeplay.")
        self.label.pack(side="top", fill="both", expand=True)
        self.freeplayButton = Button(self, bg = "lightgrey", text = "Start Freeplay", command=self.freeplay)
        self.freeplayButton.pack(side="top", expand=False)

    def freeplay(self):
        try:
            self.label = Label(self, bg="white", text="Welcome to Freeplay.")
            self.label.pack(side="top", fill="both", expand=True)
            while True:
                for i in range(len(self.switches)):                  
                    if GPIO.input(self.switches[i]) == True:
                        img = PhotoImage(file=self.pictures[i])
                        self.label.configure(image=img)
                        self.label.image = img                        
                         
                        self.notes[i].play(-1)
                        GPIO.output(self.leds[i], GPIO.HIGH)
    
                    else:
                        GPIO.output(self.leds[i], GPIO.LOW)
                        self.notes[i].stop()

        except KeyboardInterrupt:
            pass
          
class LessonFour(Lesson):
    def __init__(self):
        Lesson.__init__(self)
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
