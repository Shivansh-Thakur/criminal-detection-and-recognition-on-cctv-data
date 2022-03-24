import cv2
import json
#from spreadsheet import *

cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change
#cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


camera = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainner.yml')

with open('users.json') as jsonFile:
    users = json.load(jsonFile)
    
userList = []

while 1:
    ret, image = camera.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (30,30))

    for (x,y,w,h) in face:
        cv2.rectangle(image, (x,y), (x+w, y+h), (100,0,100), 2)

        faceId, percentage = recognizer.predict(gray[y:y+h, x:x+w])

        if percentage < 50:
            userList.append(faceId)
            faceId = users[str(faceId)]['name']+' '+str(round(100-percentage,2))+'%'
            

        else:
             faceId = 'Unknown'

        cv2.putText(image, faceId, (x,y+h),cv2.FONT_HERSHEY_SIMPLEX, 1, (50,255,),2)

    cv2.imshow('Image',image)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
#userList = list(set(userList))
#if userList:
#    addToSpreadsheet(users,userList)
