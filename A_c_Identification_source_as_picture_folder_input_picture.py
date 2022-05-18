from deepface import DeepFace
import _browser_
import padding_size
import cv2

d_path =  "dataset/images"

img_path = _browser_.func()
input_image_original = cv2.imread(img_path)
df = DeepFace.find(img_path = img_path, db_path = d_path,enforce_detection=False)
if df.empty:
    print("No match!!!")
else:
    img = cv2.imread(df["identity"][0])
    cv2.namedWindow("Uploaded") 
    cv2.moveWindow('Uploaded',400,200)
    input_image_original=padding_size.padding(input_image_original)
    cv2.imshow('Uploaded', input_image_original)
    face=padding_size.padding(img)
    cv2.namedWindow("In Database") 
    cv2.moveWindow('In Database', 750, 200)
    cv2.imshow('In Database', face)
    cv2.waitKey(0)
    cv2. destroyAllWindows() 