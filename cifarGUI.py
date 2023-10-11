#Importing Necessary Libraries

import tkinter as tk
from tkinter import filedialog # 
from tkinter import * 
from PIL import ImageTk, Image # helpful in image manipulation
import numpy # for dealing with pixel values in images

from keras.models import load_model # import model from keras library

model = load_model('cifar_model_Saved.h5')

#dictionary to label all the CIFAR-10 dataset classes.
# because our neural network only gives the output in numbers, 
# But we want the output in string format therefore we create a dictionary
classes = { 
    0:'Aeroplane',
    1:'Automobile',
    2:'Bird',
    3:'Cat',
    4:'Deer',
    5:'Dog',
    6:'Frog',
    7:'Horse',
    8:'Ship',
    9:'Truck' 
}

def upload_image():
    file_path = filedialog.askopenfilename() # show popup to choose what image to upload
    uploaded = Image.open(file_path) # store the chosen image in filepath
    uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25))) #convert image into thumbnail using function .thumbnail in PIL library
    im = ImageTk.PhotoImage(uploaded) # for creating image from the thumbnail
    sign_image.configure(image=im) # configure sign image object
    sign_image.image = im
    label.configure(text=' ')
    show_classify_button(file_path) # after image is uploaded show a classify button
    
def show_classify_button(file_path): # pass the path of the image as a parameter 
    classify_btn = Button(top, text="Classify Image", command= lambda: classify(file_path), padx=10,pady=5) #create an object of button class
    classify_btn.configure(background='#364156', foreground='white', font=('arial',10,'bold'))
    classify_btn.place(relx=0.79,rely=0.46)

def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((32,32)) # resize because in cipher 10 every image is of 32x32 dimensions
    image = numpy.expand_dims(image, axis =0) # expand the dimensions of the image which is an array of pixel values
    # expand the view of the image with respect to axis = 0
    image = numpy.array(image) # convert the image to an array value
    pred = model.predict_classes([image])[0]
    sign = classes[pred] # convert the int values to string using dictionary
    print(sign)
    label.configure(foreground='#011638', text=sign)


#intialise GUI
top = tk.Tk() #call the constructor/ create the object of tk class
top.geometry('800x600') #set height and width/ parameters of GUI application using geometry method
top.title("Image Classification CIFAR10") 
# We have to configure every single object in tkinkter
top.configure(background = "#CDCDCD")
#background color is grey

#set Heading

heading = Label(top, text  = "Image Classification CIFAR10", pady=20, font=('arial', 20, 'bold')) # create an object of label class
heading.configure(background = '#CDCDCD', foreground = '#364156')
heading.pack() # packed this heading atop objects

# create an object of button class
upload = Button(top, text = "Upload an image", command = upload_image, padx=10, pady=5)
upload.configure(background = "#364156", foreground='white',
    font =('arial',10, 'bold'))
upload.pack(side = BOTTOM, pady=50)

#uploaded image
sign_image = Label(top) #create a object of label class
sign_image.pack(side = BOTTOM,expand = True) 

#predicted class
label = Label(top, background = '#CDCDCD', font = ('arial', 15, 'bold'))
label.pack(side=BOTTOM, expand=True)


top.mainloop()