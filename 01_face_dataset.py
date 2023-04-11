
import cv2
import sys
import connect_db
face_id = input('\n enter student code : ')
face_name = input('\n Enter student name:')
face_class = input('\n Enter student class: ')

sv = connect_db.sinhvien(face_id, face_name, face_class)
# names = sv.getAllSinhvien()
# print(names)
sv.insertOrUpdate()
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

# print("\n [INFO] Initializing face capture. Look the camera and wait ...")

# Khởi tạo số lượng khuôn mặt lấy mẫu riêng lẻ
count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.COVAR_SCALE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

#     cv2.imshow('image', img)

#     k = cv2.waitKey(100) & 0xff # Nhấn 'ESC' để thoát video
#     if k == 27:
#         break
#     elif count >= 50: # chụp 50 ảnh và và dừng video
#         break 
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    k = cv2.waitKey(100) & 0xff # Nhấn 'ESC' để thoát video
    if k == 27:
        break
    elif count >= 100: # chụp 50 ảnh và và dừng video
       break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()