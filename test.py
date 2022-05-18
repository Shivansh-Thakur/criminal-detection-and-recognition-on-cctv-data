from deepface import DeepFace
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import time

#cv2.imshow("Capture Image",frame)
# k=cv2.waitKey(1)
# if k%256 ==27:
#     print ("Escape pressed ..")
#     break

#img_name = "{}.jpg".format(img_counter)
#cv2.imwrite('Sanyam/User.1.'+img_name, frame)

#image = cv2.imread('Sanyam/User.1.'+img_name)
#cv2.waitKey(0)
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('Sanyam/User.1.'+img_name,gray_image)
#cv2.waitKey(0)

#print("{} written!".format(img_name))
#img_counter += 1
# cam.release()
# cv2.destroyAllWindows()

img1_path = 'dataset/images/shivansh_thakur/1.png'
img2_path = 'dataset/images/shivansh_thakur/45.png'
img3_path = 'dataset/images/sanyam_saxena/1.png'
img4_path = 'dataset/images/jpg/1.jpg'
# img4_path= frame
#test_path = 'test1.png'

img1 = DeepFace.detectFace(img1_path)
img2 = DeepFace.detectFace(img2_path)
img3 = DeepFace.detectFace(img3_path)
img4 = DeepFace.detectFace(img4_path,enforce_detection=False)
#test1 = DeepFace.detectFace(test_path)
#img4 = DeepFace.detectFace(img4_path)
# plt.imshow(img1)
# plt.imshow(img2)


# analyzing images
print('*****analyzing images******')
obj = DeepFace.analyze(img_path = img4_path)
print(obj)

# finding images in dataset
print('------Finding images in dataset :-----')
df = DeepFace.find(img_path = img4_path, db_path = 'dataset/images/jpg', enforce_detection=False)
print(df)

# models
model_name = 'Facenet512'
resp1 = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name= model_name,enforce_detection=False)
print(resp1)

model_name = 'Dlib'
resp2 = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name= model_name,enforce_detection=False)
print(resp2)

model_name = 'OpenFace'
resp3 = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name= model_name,enforce_detection=False)
print(resp3)

print('!!!!!!!For different images :!!!!!!!')
# plt.imshow(img1)
# plt.imshow(img3)

model_name = 'DeepFace'
resp3 = DeepFace.verify(img1_path = img1_path, img2_path = img3_path, model_name= model_name,enforce_detection=False)
print(resp3)

model_name = 'DeepID'
resp3 = DeepFace.verify(img1_path = img1_path, img2_path = img3_path, model_name= model_name,enforce_detection=False)
print(resp3)

# face verification 
print('#######face verification-metric#######')
metrics = ["cosine", "euclidean", "euclidean_l2"]

result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, distance_metric = metrics[0])
print(result)
result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, distance_metric = metrics[1])
print(result)
result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, distance_metric = metrics[2])
print(result)
