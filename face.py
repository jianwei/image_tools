# coding=utf-8
import cv2,time

#创建新的cam对象
cap = cv2.VideoCapture(2)
# cap = cv2.VideoCapture('video.mp4')
#初始化人脸识别器（默认的人脸haar级联）
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

while True:
    t1=time.time()
    # 从摄像头读取图像
    _, image = cap.read()
    # 转换为灰度
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 检测图像中的所有人脸
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    # 为每个人脸绘制一个蓝色矩形
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    t2=time.time()
    fps = 1/(t2-t1)
    cv2.putText(image,"fps:{}".format(round(fps,3)), (0,30),0,1,(0, 0, 255),thickness=2,lineType=cv2.LINE_AA)
    cv2.imshow("image", image)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
