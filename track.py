# pip3 install opencv-python==4.4.0.46
# pip3 install opencv-contrib-python==4.4.0.46
# pip3 install opencv-contrib-python-headless==4.4.0.46

import cv2
print(cv2.__version__)

tracker = cv2.legacy.TrackerCSRT_create()
cap = cv2.VideoCapture("2.mp4") 
# cap = cv2.VideoCapture(0)
ret,frame = cap.read()
bbox = cv2.selectROI("Frame",frame,fromCenter=False,showCrosshair=True)
print("bbox:",bbox)
tracker.init(frame,bbox)
while (True):
    ret,frame = cap.read()
    ok,box = tracker.update(frame)
    if(ok):
        (x,y,w,h) = [int(v) for v in box]
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=2)
    cv2.imshow("Frame",frame)
    if(cv2.waitKey(50)==ord("q")):
        break
cap.release()
cv2.destroyAllWindows()


    
