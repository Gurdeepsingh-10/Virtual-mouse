import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True:
    success , image  = cap.read()

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm  in enumerate(handLms.landmark):
                # print(id , lm)
                h, w, c = image.shape
                cx,cy  = int(lm.x*w) , int(lm.y*h)
                print(id , cx , cy)

                if id == 4:
                    cv2.circle(image,(cx,cy), 10 , (240,140,0), cv2.FILLED)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.putText(image,str(int(fps)), (10, 70) , cv2.FONT_HERSHEY_COMPLEX, 1 , (240,120,200) , 2)





    cv2.imshow('Image',image)
    cv2.waitKey(1)

