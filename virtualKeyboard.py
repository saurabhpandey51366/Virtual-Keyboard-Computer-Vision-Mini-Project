from cvzone.HandTrackingModule import HandDetector
import cv2
import cvzone
import numpy as np
from time import sleep
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", '"'],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", ":"]]

functional_keys = [[ "Space", "Clear", "Enter"]]

finalText = ""

keyboard = Controller()

def drawAll(img, buttonList, functionalKeysList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[0]),20 ,rt=0, colorC= (0, 0, 0))
        cv2.rectangle(img, button.pos, (int(x + w), int(y + h)), (238, 130, 238), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        ## Draw Functional keys
    for functionalKey in functionalKeysList:
        x, y =  functionalKey.pos
        w, h = functionalKey.size

        cvzone.cornerRect(img, (functionalKey.pos[0], functionalKey.pos[1], functionalKey.size[0] + 100, functionalKey.size[0]),20 ,rt=0, colorC= (0, 0, 0))
        cv2.rectangle(img, functionalKey.pos, (int(x + w + 100), int(y + h)), (238, 130, 238), cv2.FILLED)
        cv2.putText(img, functionalKey.text, (x + 20, y + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    return img

def drawTransparentAll(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 10, y + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out

class Button:
    def __init__(self, pos, text, size=[70, 70]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
functionalKeysList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 150, 100 * i +80], key))

for i in range(len(functional_keys)):
    for j, key in enumerate(functional_keys[i]):
        functionalKeysList.append(Button([200 * j + 350, 100 * i + 480], key))


lastClick = time.time() 


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)
    img = drawAll(img, buttonList, functionalKeysList) 
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 landmarks points
        bbox1 = hand1["bbox"] #bounding box info x,y,w,h
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            for i in lmList1:
                if (i[0] != 0) and ((i[0] % 4) == 0):
                    if x < i[1] < x+w and y < i[2]<y+h:
                        cv2.rectangle(img, (x-3, y-3), (x + w + 3, y + h + 3), (218, 112, 214), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 15, y + 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                        l, _, _ = detector.findDistance(lmList1[8][:2], lmList1[12][:2], img, False)
                        # when clicked  
                        if l < 15 and time.time() - lastClick > 0.75:
                            print(button.text)
                            keyboard.press(button.text)
                            lastClick = time.time()

        for funcKey in functionalKeysList:
            x1, y1 = funcKey.pos
            w1, h1 = funcKey.size
            for i in lmList1:
                if (i[0] != 0) and ((i[0] % 4) == 0):
                    if x1 < i[1] < x1+w1+100 and y1 < i[2]<y1+h1:
                        cv2.rectangle(img, (x1-3, y1-3), (x1 + w1 + 110, y1 + h1 + 3), (218, 112, 214), cv2.FILLED)
                        cv2.putText(img, funcKey.text, (x1 + 10, y1 + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                        a, _, _ = detector.findDistance(lmList1[4][:2], lmList1[8][:2], img, False)
                        # # when clicked  
                        if a < 15 and time.time() - lastClick > 0.75:
                            if funcKey.text == 'Space':
                                keyboard.press(" ")
                            if funcKey.text == 'Clear':
                                keyboard.press('\b')
                            if funcKey.text == 'Enter':
                                keyboard.press("\r")
                                lastClick = time.time()

                    
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"] #list of 21 landmarks points
            bbox2 = hand2["bbox"] #bounding box info x,y,w,h
            for button in buttonList:
                x, y = button.pos
                w, h = button.size
                for i, j in zip(lmList1, lmList2):
                    if (i[0] != 0) and ((i[0] % 4) == 0):
                        if (x < i[1] < x+w and y < i[2]<y+h) or (x < j[1] < x+w and y < j[2]<y+h):
                            cv2.rectangle(img, (x-3, y-3), (x + w + 3, y + h + 3), (218, 112, 214), cv2.FILLED)
                            cv2.putText(img, button.text, (x + 15, y + 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                            l1, _, _ = detector.findDistance(lmList1[8][:2], lmList1[12][:2], img, False)
                            l2, _, _ = detector.findDistance(lmList2[8][:2], lmList2[12][:2], img, False)
                            l = [l1, l2]
                            for k in l:
                                if k < 15 and time.time() - lastClick > 0.75:
                                    print(button.text)
                                    keyboard.press(button.text)
                                    keyboard.release(button.text)
                                    lastClick = time.time()
                                    cv2.rectangle(img, (x-3, y-3), (x + w + 3, y + h + 3), (255, 0, 255), cv2.FILLED)
                                    cv2.putText(img, button.text, (x + 15, y + 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
            
            for funcKey in functionalKeysList:
                x1, y1 = funcKey.pos
                w1, h1 = funcKey.size
                for i in lmList1:
                    if (i[0] != 0) and ((i[0] % 4) == 0):
                        if x1 < i[1] < x1+w1+100 and y1 < i[2]<y1+h1:
                            cv2.rectangle(img, (x1-3, y1-3), (x1 + w1 + 110, y1 + h1 + 3), (218, 112, 214), cv2.FILLED)
                            cv2.putText(img, funcKey.text, (x1 + 10, y1 + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                            a, _, _ = detector.findDistance(lmList1[4][:2], lmList1[8][:2], img, False)

                            ## when clicked  
                            if a < 15 and time.time() - lastClick > 0.75:
                                if funcKey.text == 'Space':
                                    keyboard.press(" ")
                                if funcKey.text == 'Clear':
                                    keyboard.press('\b')
                                if funcKey.text == 'Enter':
                                    keyboard.press("\r")
                                    lastClick = time.time()             




    cv2.imshow("Image", img)
    cv2.waitKey(1)