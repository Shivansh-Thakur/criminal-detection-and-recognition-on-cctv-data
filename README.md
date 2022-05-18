Many times, criminals are spotted in the recordings of the surveillance systems but because of lack of technical advancement and lack of manpower, authorities don’t get to know that their surveillance systems spotted any wanted criminal.
Because of this many wanted criminals are free and are left unpunished.

To solve this Problem, our system provide these key features:

1. Identification of a criminal (person) in a video recording corresponding to the uploaded picture of criminal (person).
2. Identification of a criminal (person) in a video recording corresponding to "N" number of small video clip/gif that are to be investigated for the presence of criminal (person) in the uploaded clips.
3. Identification of criminal (person) in a list of known criminals available in our database. 
This can be used to Identify their gangs.
(terrorist groups, etc. in which he/she belongs).

Technology used:

• Python
• Deepface (Python package that contains popular face recognition models)
• Open CV

Future Extension:

• Later on we will try to identify criminals corresponding to their partial face.
• We will be using LSTM to predict the region where crime is going to happen.

Objective: 

1. Identification
1.1. Identification of a person in a video recording using a picture. (Positive/negative outlook both)
1.2. Identification of a person in a video recording using a small video clip/gif. (Positive/negative
outlook both)
1.3. Identification in a list of known criminals.
1.3.1. Identification of criminals and their gang if possible, (terrorist groups, etc. in which
he/she belongs).
2. Live Recognition
3. Automation for routine identification.

Date Set used in the Project:

Currently, we have created our dataset by ourselves so that we can test our platform, later we wish
to take a dataset from a cyber-cell so as to practically implement our project and solve this real-world
problem. The data-set will consist of footage from cameras installed in the society (town). Our footage
are pixelated due to the use of low resolution cameras.

Results : 

Based on experiments, these models are over performing models: 
FaceNet, VGG-Face, ArcFace and Dlib.
Following are the accuracies of these models on other datasets [Dataset used are: Labeled Faces in
the Wild (LFW) and YouTube Faces in the Wild (YTF)] which are declared by its creators. This is
the concept of transfer learning, in which an already existing model is used for a new application.
