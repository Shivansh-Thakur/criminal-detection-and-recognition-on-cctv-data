from deepface import DeepFace
import numpy as np
import _browser_
import padding_size
import cv2
import os
import time

flag = 0
input_video_path = _browser_.func()
input_video = cv2.VideoCapture(input_video_path)
successful, input_frame = input_video.read()
count = 0
successful = True
input_frames = []
while successful:
    input_frames.append(input_frame)
    successful, input_frame = input_video.read()
    count += 1
input_frames = np.array(input_frames)
input_frames.nbytes

start_time = time.time()
for video in os.listdir('dataset/videos'):
    if flag == 1:
        break
    video_path = f"dataset/videos/{video}"
    source_video = cv2.VideoCapture(video_path)
    success, frame = source_video.read()
    count = 0
    success = True
    frames = []

    while success:
        frames.append(frame)
        success,frame = source_video.read()
        count += 1

    print(count, "Frames extracted")
    frames = np.array(frames)
    print("Data shape =\t", frames.shape)
    frames.nbytes

    for frame_num in range(0,len(frames)):
        if flag == 1:
            break    
        detected_face = DeepFace.detectFace(img_path = frames[frame_num], target_size = (160,160), enforce_detection = False)

        for input_video_frame in input_frames:
            result = DeepFace.verify(img1_path = input_video_frame, img2_path = detected_face, model_name = 'Facenet512', enforce_detection = False)

            if result['verified'] == True:
                flag = 1
                print(result, '\nInput image matched with the Frame number :', frame_num, 'of the video :', video)
                end_time = time.time()
                print(f'Time taken to detect and match the face : {end_time - start_time}')
                
                img = frames[frame_num]
                cv2.namedWindow("Uploaded") 
                cv2.moveWindow('Uploaded', 400, 200)
                input_image_original=padding_size.padding(input_video_frame)
                cv2.imshow('Uploaded', input_image_original)
                face=padding_size.padding(frames[frame_num])
                cv2.namedWindow("Matched in Video") 
                cv2.moveWindow('Matched in Video', 750, 200)
                cv2.imshow('Matched in Video', face)
                cv2.waitKey(0)
                cv2. destroyAllWindows()
                break

    print(f'Video : ', video, 'Scanned') 