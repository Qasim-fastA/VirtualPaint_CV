"""
Entry point for the Virtual Paint application.

Responsibilities:
- Initialize webcam capture.
- Run the main loop: read frame -> flip -> detect hands -> interpret gesture ->
  update canvas -> blend canvas with frame -> display.
- Handle exit conditions and resource cleanup (release camera, destroy windows).

Should NOT contain: hand detection logic, drawing math, or UI rendering details.
This file orchestrates other modules; it does not implement them.
"""

import cv2
import time
import hand_tracking as ht

pTime = 0
cap = cv2.VideoCapture(0)
detector = ht.HandsDetector()

while True:

    success , img = cap.read()

    if not success :
        break

    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    fingers = detector.fingers()
    print(fingers)
    # if len(lmlist) != 0 :
    #     print(lmlist)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()