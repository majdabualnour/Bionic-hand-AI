import cv2
import mediapipe as mp
import pyfirmata

comport='COM5'  

b=pyfirmata.Arduino(comport)
it = pyfirmata.util.Iterator(b)
it.start()
s1=b.get_pin('d:2:s')
s2=b.get_pin('d:3:s')
s3=b.get_pin('d:4:s')
#led_3=b.get_pin('d:4:o')
s4= b.get_pin('d:5:s')
s5=b.get_pin('d:6:s')
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
tipIds = [4, 8, 12, 16, 20]
def thes(array):
   v = 0
   for a in array:
      if a == 1 : array[v]= 90
      else: a = 0
      v +=1

   s1.write(array[0])
   s2.write(array[1])
   s3.write(array[2])
   s4.write(array[3])
   s5.write(array[4])
while True:
   success, img = cap.read()
   img = cv2.flip(img, 1)

   imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

   results = hands.process(imgRGB)

   lmList = []

   if results.multi_hand_landmarks:
      for handLms in results.multi_hand_landmarks:
         for id, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            

            if id == 8:
               cv2.circle(img, (cx, cy), 20, (0, 255, 0), cv2.FILLED)

            if len(lmList) == 21:
               fingers = []

               if lmList[tipIds[0]][1] < lmList[tipIds[0] - 2][1]:
                  fingers.append(1)
               else:
                  fingers.append(0)

               for tip in range(1, 5):
                  if lmList[tipIds[tip]][2] < lmList[tipIds[tip] - 2][2]:
                     fingers.append(1)
                  else:
                     fingers.append(0)

              
               
               #cv2.putText(img, f'{totalFingers}', (40, 80), cv2.FONT_HERSHEY_SIMPLEX,
               #3, (0, 0, 255), 6)
   else:fingers = [0, 0, 0, 0, 0]
   thes(fingers)
   print(fingers)

   cv2.imshow('Hand Tracker', img)
   k=cv2.waitKey(5)
   if k==ord('q'):break
                
