import cv2
from deepface import DeepFace
#path where data is stored.
#use 'q' to exit the new window
path = "dataset/images/combined"
DeepFace.stream(db_path = path)