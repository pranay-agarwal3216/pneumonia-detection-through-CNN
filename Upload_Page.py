import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
from tkinter import messagebox


import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

app = tk.Tk()
app.title('Uploading Page')
my_font1=('times', 18, 'bold')
label = ttk.Label(app, text="Add Photo", foreground="Black", font=("Arial Rounded MT Bold", 38)).grid(row=0,column=0,padx=200,pady=20)

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 15), foreground='black', background="#0A4438")

b1 = ttk.Button(app, text='Upload File',width=20,command = lambda:upload_file(),style='my.TButton')
b1.grid(row=2,column=0)
result =""
def upload_file():
    global img
    f_types = [('Jpeg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)

    model = load_model('model_vgg16.h5')

    img = Image.open(filename)
    img = img.resize((244,244))
    img = ImageTk.PhotoImage(img)
    img2 = image.load_img(filename, target_size=(224,224))

    x = image.img_to_array(img2)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    print(classes)
    l = classes.astype(int)
    print(l)
    y = l[0]
    print(y[0])
    if y[0] == 1:
        result = "NORMAL"
        messagebox.showinfo("showinfo", "YOU ARE NORMAL. CONGO!")
    else:
        result = "PNEUMONIA"
        messagebox.showinfo("showinfo", "YOU MIGHT BE SUFFERING FORM PNEUMONIA. CONSULT A DOCTOR")

    b2 =tk.Button(app,image=img)
    b2.grid(row=3,column=0)

frame1 = Frame(app)
frame1.grid(row=4, column=0,pady=10)


def center_window(width, height):
    # get screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))


center_window(700, 500)


app.configure(bg='#0A4438')
app.config(highlightbackground="#053128", highlightthickness=10, highlightcolor="#053128")
app.mainloop()

