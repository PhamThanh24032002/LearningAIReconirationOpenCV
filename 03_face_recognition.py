import cv2
import numpy as np
import os 
import connect_db
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# khởi tạo bộ đếm id
id = 0

# tên liên quan đến id: ví dụ ==> Marcelo: id=1, v.v.
# names = ['None', 'tien', 'toan', 'thanh']

# Khởi tạo và bắt đầu quay video thời gian thực
cam = cv2.VideoCapture(0)
cam.set(3, 1800) # đặt chiều rộng camera
cam.set(4, 720) # đặt chiều ngang camera

# Xác định kích thước cửa sổ tối thiểu để được nhận dạng là khuôn mặt
minW = 0.2*cam.get(3)
minH = 0.2*cam.get(4)

while True:

    ret, img =cam.read()
    # img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (203,23,252)
    
    # Line thickness of 2 px
    thickness = 2
    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if(confidence < 40): 
       # Kiểm tra xem giống không ==> "0" là khớp hoàn hảo
            id,conf=recognizer.predict(gray[y:y+h,x:x+w])
            profile=connect_db.sinhvien.getProfile(id)
         #set text to window
            if(profile!=None):
              confidence = " {0}% ".format(round(100 - confidence))
                
            #cv2.PutText(cv2.fromarray(img),str(id),(x+y+h),font,(0,0,255),2);
              cv2.putText(img, "Name: " + str(profile[1]), (x,y+h+30), fontface, fontscale, fontcolor ,2)
              cv2.putText(img, "Lop: " + str(profile[3]), (x,y+h+60), fontface, fontscale, fontcolor ,2)
              cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1) 
             
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # nhấn ESC để thoát
    if k == 27:
      break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
