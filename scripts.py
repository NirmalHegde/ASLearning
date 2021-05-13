#import libraries and other scripts
import tkinter as tk
import pygame
import time
import cv2
import numpy as np
from webcam import *
import random

def lettergame(root,delete):
    delete.place_forget()
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","10"]
    broadcast = tk.Label(root, text=random.choice(letters))
    broadcast.config(font=("Arial Rounded MT Bold",500),background="#497959", foreground="#FFFFFF")
    broadcast.place(relx=0.5,rely=0.03)