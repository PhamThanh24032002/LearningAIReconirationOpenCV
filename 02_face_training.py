import cv2
import numpy as np
from PIL import Image
import os


# Đường dẫn cơ sở dữ liệu ảnh khuôn mặt
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# chức năng lấy dữ liệu hình ảnh và nhãn
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # chuyển nó sang thang độ xám
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faceSamples.append(img_numpy)
        ids.append(id)
        cv2.waitKey(1)
    return ids,faceSamples

def Tranning() :
    ids,faceSamples = getImagesAndLabels(path) 
    recognizer.train(faceSamples,np.array(ids))
    recognizer.save('trainer/trainer.yml')
    
Tranning()
cv2.destroyAllWindows()
