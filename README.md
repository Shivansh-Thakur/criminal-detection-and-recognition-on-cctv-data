# Face-Recognition
Face detection and Recognition using OpenCV-python

A console based application 

OpenCV based face recognition system that can detect and recognize multiple faces in an image. 

There are 2 parts in a face recognition system.

1. Face Detection - To detect faces in images.

2. Face Recognition - To recognize face of persons in the images.

## 1.Face Detection 

Face detection is acheived in this project using Haar Cascade classifier. It could be used for object detection. Here we are using it for detecting faces and store the data as array in a .yml file. 

## 2. Face Recognition

We are using LBPH (Local Binary Patterns Histograms ) classifier to recognize the faces from the images. It compares neighboring pixels of a pixel and creates a histogram out of it for comparing faces. We could also use algorithms such as, EigenFaces Face Recognizer and FisherFaces Face Recognizer.

## Requirements
- [Python3](https://www.python.org/downloads/)

- [OpenCV2](https://opencv.org/releases/)

- [PIL](https://pypi.org/project/Pillow/)

- [Cascade Classifier](https://github.com/opencv/opencv/tree/master/data/haarcascades)

- [gspread](https://gspread.readthedocs.io/en/latest/)

- [JSON](https://www.json.org/json-en.html)

## How to run??

1. Run create.py file to create a dataset by providing name and id, it will capture 20 images and store in dataset and convert into array, store in trainner.yml file.

2. Run detector.py to detect the face. If any face stored in dataset, the name of the person will be displayed.

3. The detected person's data will be added to the google form.
