import tkinter as tk
import PlottingFunctions
from PIL import Image
from PIL import ImageTk
import ctypes

# dimensions of items in the GUI
width = 900
height = 585
img_height = 600
img_width = 720

# unicode symbols for the mathematical symbols used
omega_sym = chr(937)
tau_sym = chr(0x03C4)
superscript_two_sym = chr(0x00B2)


def calculate_center_pos(w, h):  # finds the screen size of the operating system and calculates the center of the screen
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    x = screensize[0] / 2 - w / 2
    y = screensize[1] / 2 - h / 2
    return x, y


def get_image():  # gets the last plot that was made and resize the plot to fit the GUI
    img = Image.open("current_plot.png")
    img = img.resize((img_width, img_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


def switch_img(matrix, image_canvas):
    # calls the function to plot a graph based on the matrix given and adds it to the given image canvas
    center, m_width, m_height, inclination, labels = matrix.get_ellipse_params()
    PlottingFunctions.plot_graph(center, m_width, m_height, inclination, labels)
    img = get_image()
    image_canvas.create_image(2, 2, image=img, anchor=tk.NW)
    image_canvas.pack()


def createGUI(m):
    # gets the matrices that were passed to the GUI
    matrices = m

    # sets up the window and opens it in the center of the screen
    gui = tk.Tk()
    gui.title("SMC20374 - Programming for Prototyping")
    x, y = calculate_center_pos(width, height)
    gui.geometry(str(width) + "x" + str(height) + "+" + str(int(x)) + "+" + str(int(y)))
    gui.resizable(0, 0)

    # creates the buttons for choosing which plot to display
    button_frame = tk.Frame(gui)
    image_canvas = tk.Canvas(gui, width=img_width, height=img_height)
    button_frame.pack(side='right')

    # lambda expression to pass the matrix to the plotting function so the plot can be created and displayed
    # the lambda expression was used so as we are able to pass parameters to the function that is called.
    for i in range(len(matrices)):
        label = matrices[i].get_labels()
        b = tk.Button(button_frame, text=label[0] + " vs " + label[1], width=20, height=3,
                      command=lambda i=i: switch_img(matrices[i], image_canvas))
        b.pack(side='top', pady=10, padx=25)
    # button_1 = tk.Button(button_frame, text=omega_sym + "bh" + superscript_two_sym + " vs " + omega_sym + "ch" +
    #                      superscript_two_sym, width=15, height=3,
    #                      command=lambda: switch_img(matrices[0], image_canvas))
    #
    # button_1.pack(side='top', pady=10)  # padding so the buttons are not touching each other directly
    #
    # button_2 = tk.Button(button_frame, text=omega_sym + "ch" + superscript_two_sym + " vs W", width=15, height=3,
    #                      command=lambda: switch_img(matrices[1], image_canvas))
    # button_2.pack(side='top', pady=10)
    #
    # button_3 = tk.Button(button_frame, text=tau_sym + " vs W", width=15, height=3,
    #                      command=lambda: switch_img(matrices[2], image_canvas))
    # button_3.pack(side='top', pady=10)
    #
    # button_4 = tk.Button(button_frame, text="log(A) vs ns", width=15, height=3,
    #                      command=lambda: switch_img(matrices[3], image_canvas))
    # button_4.pack(side='top', pady=10, padx=40)
    # image_canvas.create_image(2, 2, image=tk_img, anchor=tk.NW)
    image_canvas.pack()

    gui.mainloop()
