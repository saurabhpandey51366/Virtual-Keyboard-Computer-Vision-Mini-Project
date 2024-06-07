import cv2
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)



cTime = 0
pTime = 0
while True:
    success, img = cap.read()

    hands, img = detector.findHands(img) #with draw
    #hands, img = detector.findHands(img, draw=False) #No Draw
    if hands:
        #Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 landmarks points
        bbox1 = hand1["bbox"] #bounding box info x,y,w,h
        centerPoint1 = hand1["center"] #center of the hand cx, cy
        handType1 = hand1["type"] #hand type left or right
        fingers1 = detector.fingersUp(hand1)
        length, info, img = detector.findDistance(lmList1[8][:2], lmList1[7][:2], img)


        

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"] #list of 21 landmarks points
            bbox2 = hand2["bbox"] #bounding box info x,y,w,h
            centerPoint2 = hand2["center"] #center of the hand cx, cy
            handType2 = hand2["type"] #hand type left or right
            fingers2 = detector.fingersUp(hand2)

            length, info, img = detector.findDistance(lmList1[8][:2], lmList1[8][:2], img)
            #length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
            #print(fingers1, fingers2)

            
    

    

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)