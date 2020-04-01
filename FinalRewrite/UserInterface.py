import tkinter as tk
from FinalRewrite import PlottingFunctions
from PIL import Image
from PIL import ImageTk
import ctypes

width = 940
height = 585
img_height = 600
img_width = 720

omega_sym = chr(937)
tau_sym = chr(0x03C4)
superscript_two_sym = chr(0x00B2)


def calculate_center_pos(w, h):
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    x = screensize[0] / 2 - w / 2
    y = screensize[1] / 2 - h / 2
    return x, y


def get_image():
    img = Image.open("current_plot.png")
    img = img.resize((img_width, img_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def switch_img_1(matrix, image_canvas):
    center, m_width, m_height, inclination, labels = matrix.get_ellipse_params()
    PlottingFunctions.plot_graph(center, m_width, m_height, inclination, labels)
    img = get_image()
    image_canvas.create_image(2, 2, image=img, anchor=tk.NW)
    image_canvas.pack()


def switch_img_2(matrix, image_canvas):
    center, m_width, m_height, inclination, labels = matrix.get_ellipse_params()
    PlottingFunctions.plot_graph(center, m_width, m_height, inclination, labels)
    img = get_image()
    image_canvas.create_image(2, 2, image=img, anchor=tk.NW)
    image_canvas.pack()


def switch_img_3(matrix, image_canvas):
    center, m_width, m_height, inclination, labels = matrix.get_ellipse_params()
    PlottingFunctions.plot_graph(center, m_width, m_height, inclination, labels)
    img = get_image()
    image_canvas.create_image(2, 2, image=img, anchor=tk.NW)
    image_canvas.pack()


def switch_img_4(matrix, image_canvas):
    center, m_width, m_height, inclination, labels = matrix.get_ellipse_params()
    PlottingFunctions.plot_graph(center, m_width, m_height, inclination, labels)
    img = get_image()
    image_canvas.create_image(2, 2, image=img, anchor=tk.NW)
    image_canvas.pack()


def createGUI(m):
    matrices = m
    gui = tk.Tk()
    gui.title("SMC20374 - Programming for Prototyping")
    x, y = calculate_center_pos(width, height)
    gui.geometry(str(width) + "x" + str(height) + "+" + str(int(x)) + "+" + str(int(y)))
    gui.resizable(0, 0)

    button_frame = tk.Frame(gui)
    image_canvas = tk.Canvas(gui, width=img_width, height=img_height)
    button_frame.pack(side='right')

    button_1 = tk.Button(button_frame, text=omega_sym + "bh" + superscript_two_sym + " vs " + omega_sym + "ch" +
                         superscript_two_sym, width=15, height=3,
                         command=lambda: switch_img_1(matrices[0], image_canvas))
    button_1.pack(side='top', pady=10)

    button_2 = tk.Button(button_frame, text=omega_sym + "ch" + superscript_two_sym + " vs W", width=15, height=3,
                         command=lambda: switch_img_2(matrices[1], image_canvas))
    button_2.pack(side='top', pady=10)

    button_3 = tk.Button(button_frame, text=tau_sym + " vs W", width=15, height=3,
                         command=lambda: switch_img_3(matrices[2], image_canvas))
    button_3.pack(side='top', pady=10)

    button_4 = tk.Button(button_frame, text="log(A) vs ns", width=15, height=3,
                         command=lambda: switch_img_4(matrices[3], image_canvas))
    button_4.pack(side='top', pady=10, padx=40)
    # image_canvas.create_image(2, 2, image=tk_img, anchor=tk.NW)
    image_canvas.pack()

    gui.mainloop()
