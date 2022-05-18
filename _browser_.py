from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

def func():
   global Browse 
   Browse = Tk()
   Browse.geometry("360x144+600+250")
   Browse.title('Browser')
   # Add a Label widget
   label = Label(Browse, text = "Click The Button To Browse The Files", font = ('Aerial 14'))
   label.pack(pady = 10)
   # Create a Button
   ttk.Button(Browse, text = "Browse", command = open_file).pack(pady = 20)
   Browse.mainloop()
   return filepath
    
def open_file():
   file = filedialog.askopenfile()
   if file:
      global filepath
      filepath = os.path.abspath(file.name)
      #Label(Browse, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()
