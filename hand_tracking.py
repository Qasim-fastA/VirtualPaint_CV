"""
Wraps MediaPipe Hands for hand detection and landmark extraction.

Responsibilities:
- Initialize and configure the MediaPipe Hands model.
- Given a frame, return detected hand landmarks (converted to usable pixel
  coordinates) and handedness (left/right), if any hand is present.

Should NOT contain: gesture interpretation, drawing logic, or UI code.
This module only answers "where is the hand and what are its landmarks?" —
it has no concept of "drawing" or "modes."
"""

import mediapipe as mp
import cv2



class HandsDetector():
    def __init__(self,mode=False , maxHands = 2 , detectionCon = 0.5 , trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )  # parameters : static image mode true means the whole time it detects and not track so keep it false                         # max hands , min detection and tracking confidence (50 percent ) ,skipping for now as default are set
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self,img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # print(results.multi_hand_landmarks) # to check there is something in results

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw :
                   self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img



    def findPosition(self,img, handNo=0, draw=True):

            lmlist = []
            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    # print(id,lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    #print(id, cx, cy)  # will give for all 21 values  so write id also
                    lmlist.append([id, cx, cy])
                    #if id == 0:
                    if draw:
                        cv2.circle(img, (cx, cy), 3, (255, 0, 0),
                                   cv2.FILLED)  # will show a circle at the particular id
            self.lmlist = lmlist
            return lmlist

    def fingers(self):
        fingers = [] # will hold 5 boolean-like values: [thumb, index, middle, ring, pinky]
        if len(self.lmlist) != 0:

            if self.lmlist[4][1] < self.lmlist[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            if self.lmlist[8][2] < self.lmlist[6][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            if self.lmlist[12][2] < self.lmlist[10][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            if self.lmlist[16][2] < self.lmlist[14][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            if self.lmlist[20][2] < self.lmlist[18][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers