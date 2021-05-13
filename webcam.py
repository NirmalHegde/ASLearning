import tkinter as tk
import PIL.Image, PIL.ImageTk
import cv2
import numpy as np

def Webcam(root):
    videoFrame = tk.Frame(root, bg="black")
    videoFrame.grid()

    videoFeed = tk.Label(videoFrame)
    videoFeed.grid()

    captureFeed = cv2.VideoCapture(0)
    captureFeed.set(3, 300)
    captureFeed.set(4, 300)

    def placement(value):
        pass
    
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, placement)
    cv2.createTrackbar("Hue Max", "TrackBars", 15, 179, placement)
    cv2.createTrackbar("Sat Min", "TrackBars", 44, 255, placement)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, placement)
    cv2.createTrackbar("Val Min", "TrackBars", 0, 255, placement)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, placement)

    def stream():
        working, image = captureFeed.read()
        inverted_image = cv2.flip(image, 1)
        image_HSV = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

        upper = np.array([h_max, s_max, v_max])
        lower = np.array([h_min, s_min, v_min])
        mask = cv2.inRange(image_HSV, lower, upper)
        hand_detector_raw = cv2.bitwise_and(inverted_image, inverted_image, mask=mask)
        hand_detector_gray = cv2.cvtColor(hand_detector_raw, cv2.COLOR_BGR2GRAY)
        thresh, hand_detector_BlackAndWhite = cv2.threshold(hand_detector_gray, 55, 255, cv2.THRESH_BINARY)
        hand_detector_cropped = hand_detector_BlackAndWhite[71:315, 16:240]
        cv2.rectangle(inverted_image, (315, 16), (71, 240), (0, 0, 255), 3)

        frame = cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB)
        photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        videoFeed.photo = photo
        videoFeed.configure(image=photo)
        videoFeed.after(1, stream)

    stream()
 
