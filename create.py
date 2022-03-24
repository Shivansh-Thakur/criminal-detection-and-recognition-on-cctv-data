import cv2
from trainner import trainner
import json

camera = cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change
#cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

name = input('Enter Name: ')
Id = int(input('Enter Id: '))
itr = 1

while 1:

    ret, image = camera.read()

    grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(grayImage,scaleFactor = 1.5,minNeighbors = 5,minSize= (30,30))

    for (x,y,w,h) in face:
        
        cv2.rectangle(image, (x,y), (x+w,y+h), (100,100,0), 2)

        cv2.imwrite('dataset/' + str(Id) + '.' + str(itr) + '.jpg', grayImage[y:y+h+5, x:x+w+5])
    itr += 1

    if itr == 21:
        break
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    cv2.imshow('Frame',image)
camera.release()
cv2.destroyAllWindows()

with open('C:/Users/shiva/Desktop/projects/Criminal_identification/git_fr/Face-Recognition/users.json') as json_file:
    data = json.load(json_file)

username = {
            'name':name
           }
data[Id] = username

with open("users.json", "w") as file:  
    json.dump(data, file,indent = 4)
    
trainner()
