import tkinter as tk
from PIL import Image
from PIL import ImageTk
import ctypes

width = 940
height = 600
img_height = 600
img_width = 720

omega = chr(937)
tau = chr(0x03C4)
superscript_two = chr(0x00B2)

# calculates the center position for the window on the monitor
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
x = screensize[0] / 2 - width / 2
y = screensize[1] / 2 - height / 2


def switch_img_1():  # function for switching the image to image 1
    image_canvas.create_image(2, 2, image=tk_img, anchor=tk.NW)
    image_canvas.pack()


def switch_img_2():  # function for switching the image to image 2
    image_canvas.create_image(2, 2, image=tk_img_2, anchor=tk.NW)
    image_canvas.pack()


def switch_img_3():  # function for switching the image to image 3
    image_canvas.create_image(2, 2, image=tk_img_3, anchor=tk.NW)
    image_canvas.pack()


def switch_img_4():  # function for switching the image to image 4
    image_canvas.create_image(2, 2, image=tk_img_4, anchor=tk.NW)
    image_canvas.pack()


# creates the window
gui = tk.Tk()
gui.title("SMC20374 - Programming for Prototyping")
# sets the window to the size specified while also adding the offsets so the window opens in the center
gui.geometry(str(width) + "x" + str(height) + "+" + str(int(x)) + "+" + str(int(y)))
gui.resizable(width=False, height=False)

# creates the button frame for the button panel to be placed in
button_frame = tk.Frame(gui)
image_canvas = tk.Canvas(gui, width=img_width, height=img_height)
button_frame.pack(side='right')


img = Image.open("omegabh2_vs_omegach2.png")
img = img.resize((img_width, img_height), Image.ANTIALIAS)
tk_img = ImageTk.PhotoImage(img)

img_2 = Image.open("omegach2_vs_w.png")
img_2 = img_2.resize((img_width, img_height), Image.ANTIALIAS)
tk_img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open("tau_vs_w.png")
img_3 = img_3.resize((img_width, img_height), Image.ANTIALIAS)
tk_img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open("logA_vs_ns.png")
img_4 = img_4.resize((img_width, img_height), Image.ANTIALIAS)
tk_img_4 = ImageTk.PhotoImage(img_4)

button_1 = tk.Button(button_frame, text=omega + "bh" + superscript_two + " vs " + omega + "ch" + superscript_two,
                     width=30, height=10, command=switch_img_1)
button_1.pack(side='top')
button_2 = tk.Button(button_frame, text=omega + "ch" + superscript_two + " vs W", width=30, height=10, command=switch_img_2)
button_2.pack(side='top')
button_3 = tk.Button(button_frame, text=tau + " vs W", width=30, height=10, command=switch_img_3)
button_3.pack(side='top')
button_4 = tk.Button(button_frame, text="log(A) vs ns", width=30, height=10, command=switch_img_4)
button_4.pack(side='top')
image_canvas.create_image(2, 2, image=tk_img, anchor=tk.NW)
image_canvas.pack()

gui.mainloop()
