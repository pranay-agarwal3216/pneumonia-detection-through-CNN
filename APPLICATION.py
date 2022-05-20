import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

app = tk.Tk()


def camp_table():
    app.destroy()
    os.system("python Welcome_Table.py")


s = ttk.Style()
s.configure('my.TButton',
            font=('Helvetica', 15),
            foreground='black',
            background="#0A4438")

# setting up image address
image = Image.open("pic1.jpg")
image2 = Image.open("pic2.jpg")
image = image.resize((180, 200))
image2 = image2.resize((190,200))
photo = ImageTk.PhotoImage(image)
photo2 = ImageTk.PhotoImage(image2)

pic = tk.Label(image= photo)
pic.pack()
pic.place(relx=0.04, rely = 0.6, anchor="w")

pic1 = tk.Label(image= photo2)
pic1.pack()
pic1.place(relx= 0.67, rely = 0.6, anchor="w")

label = ttk.Label(app, text= "Pneumonia Detection",
                  foreground="Black",
                  font=("Ariell Rounded MT Bold",38)).grid(row=0,
                                                           column= 0,
                                                           padx = 100)

tk.b1 = ttk.Button(app, text="Welcome", command=None,
                   style='my.TButton').grid(row=1,column=0,pady=40)

def upload_page():
    app.destroy()
    os.system("python Upload_Page.py")

b6 = ttk.Button(app, text="Upload", command= upload_page,style='my.TButton').grid(row=6, column =0, pady=10)


def center_window(width, height):

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # calculating pos of x and y

    x= (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    app.geometry('%dx%d+%d+%d' % (width,height, x, y))

center_window(700,300)

app.resizable(False,False)
app.configure(bg='#0A4438')
app.config(highlightbackground="#053128",
           highlightthickness=10,
           highlightcolor="#053128")
app.mainloop()



