#import libraries and other scripts
import tkinter as tk
import pygame
import time
import cv2
import numpy as np
from webcam import *
from scripts import *
import random

#initialize pygame
pygame.init()

#set up application to have all files
class StartApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #set logo, title, and screen size
        self.title("ASLearning")
        self.iconbitmap('Logo.ico')
        self.geometry("1440x1024")

        #create a virtual grid to hold all app pages for use at different times
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #Initialize each frame using a blank dictionary and for loop to add it to the grid
        #the frame on the top of the grid will be the one that is visible to the user
        self.frames = {}
        for frameGrid in (Menu, Module1, Module2, Module3):
            page_name = frameGrid.__name__
            frame = frameGrid(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #show the menu page to let users choose modules
        self.show("Menu")

    #function that changes which frame is visible by raising the previous one
    def show(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

#Menu page
class Menu(tk.Frame):

    #music!
    pygame.mixer.music.load("UI/8BitSpaceGroove.mp3")
    pygame.mixer.music.play()

    #initialization step of menu
    def __init__(self, parent, controller):
        #initialize canvas to store all ui options
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame1 = (self)
        self.frame1.place(relheight=1, relwidth=1)

        #place background image
        self.bgImage = tk.PhotoImage(file="UI/bg.png")
        self.background = tk.Label(self.frame1, image=self.bgImage)
        self.background.place(relwidth=1, relheight=1)

        title = tk.Label(self.frame1, bg="#65AEA6", text="Welcome to ASLearning!")
        title.config(font=("Curlz MT",64))
        title.place(relx=0.28,rely=0.04)

        #Module 1 button
        self.lettersImage = tk.PhotoImage(file="UI/mod1.png")
        self.letters = tk.Button(self.frame1, image=self.lettersImage, bg="#65AEA6", border="0", command=lambda: controller.show("Module1"))
        self.letters.place(relx=0.5,rely=0.3,anchor="n")

        #Module 2 Button
        self.wordsImage = tk.PhotoImage(file="UI/mod2.png")
        self.words = tk.Button(self.frame1, image=self.wordsImage, bg="#65AEA6", border="0", command=lambda: controller.show("Module2"))
        self.words.place(relx=0.5,rely=0.5,anchor="n")

        #Module 3 Button
        self.sentencesImage = tk.PhotoImage(file="UI/mod3.png")
        self.sentences = tk.Button(self.frame1, image=self.sentencesImage, bg="#65AEA6", border="0", command=lambda: controller.show("Module3"))
        self.sentences.place(relx=0.5,rely=0.7,anchor="n")

#Module1:Letters page
class Module1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame2 = tk.Frame(self, bg="#FFFFFF", border="0")
        self.frame2.place(relheight=1, relwidth=1)

        self.bgImage2 = tk.PhotoImage(file="UI/chalkboard.png")
        self.background2 = tk.Label(self.frame2, image=self.bgImage2)
        self.background2.place(relwidth=1,relheight=1)

        webcam = Webcam(self.frame2)

        self.gameStartImage1 = tk.PhotoImage(file="UI/startgame.png")
        self.gameStart = tk.Button(self,text="start game", image=self.gameStartImage1, bg="#497959", border="0", command=lambda: lettergame(self.frame2,self.gameStart))
        self.gameStart.place(relx=0.45,rely=0.1)

        self.exit1Image = tk.PhotoImage(file="UI/exit.png")
        self.exit1 = tk.Button(self,text="exit", image=self.exit1Image, bg="#497959", border="0", command=lambda: controller.show("Menu"))
        self.exit1.place(relx=0.05,rely=0.3,relwidth=0.1,relheight=0.1)

#Module2:Letters page
class Module2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame3 = tk.Frame(self, bg="#FFFFFF", border="0")
        self.frame3.place(relheight=1, relwidth=1)
        self.gameStart = tk.Button(self,text="start game", border="0")
        self.gameStart.place(relx=0.5,rely=0.5,relwidth=0.3,relheight=0.3)
        self.exit2 = tk.Button(self,text="exit", border="0", command=lambda: controller.show("Menu"))
        self.exit2.place(relx=0,rely=0.5,relwidth=0.3,relheight=0.3)

class Module3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame4 = tk.Frame(self, bg="#FFFFFF", border="0")
        self.frame4.place(relheight=1, relwidth=1)
        self.gameStart = tk.Button(self,text="start game", border="0")
        self.gameStart.place(relx=0.5,rely=0.5,relwidth=0.3,relheight=0.3)
        self.exit3 = tk.Button(self,text="exit", border="0", command=lambda: controller.show("Menu"))
        self.exit3.place(relx=0,rely=0.5,relwidth=0.3,relheight=0.3)

#loop so that the app stays open
if __name__ == "__main__":
    app = StartApp()
    app.mainloop()
