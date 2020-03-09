import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse
from MatrixObject import Matrix
import math

def get_covariance_matrix(file_path):
    # reads the file specified in the file path parameter, then converts it into a 29x28 matrix.
    # with the labels in the first row at the top of the matrix and this matrix is returned from this function
    f = open(file_path)
    matrix = []

    for line in f:
        matrix_line = []
        line = line.strip()
        line_split = line.split(" ")
        if line_split[0] == "#":
            line_split.remove(line_split[0])
            matrix.append(line_split)
        else:
            line_split = line.split("  ")  # splits the line with 2 spaces as some have another space or a negative sign
            for entry in line_split:
                value = float(entry)
                matrix_line.append(value)
            matrix.append(matrix_line)

    return matrix


def science_convert(labels):
    # this function converts the plaintext labels into a TeX format for use in labeling the graph plots
    new_labels = []
    for label in labels:
        label = label.replace("omega", "\\Omega_")
        label = label.replace("2", "^2")
        label = label.replace("log", "log(")
        label = label.replace("A", "A)")
        label = label.replace("ns", "n_s")
        label = label.replace("tau", "\\tau")
        new_labels.append("$" + label + "$")
    return new_labels


def transformation(origin_x, origin_y, point_x, point_y, theta):
    s = math.sin(theta)
    c = math.cos(theta)

    point_x -= origin_x
    point_y -= origin_y

    x_new = (point_x * c) - (point_y * s)
    y_new = (point_x * s) + (point_y * c)

    x_prime = x_new + origin_x
    y_prime = y_new + origin_y

    return x_prime, y_prime




def plot(params):
    # this function takes in the parameter list and plots the ellipsis and and performs the Gaussian realization for
    # the selection of the 500 points
    # parameter 0 is a list containing the center x and y values, with x being first
    # parameter 1 is the width of the ellipsis
    # parameter 2 is the height of the ellipsis
    # parameter 3 is the inclination of the ellipsis
    # parameter 4 is a list containing the x and y axis labels, with x being first

    center = params[0]

    # width and height for both 1 - alpha values are found
    w_1 = params[1] * 1.52
    h_1 = params[2] * 1.52
    w_2 = params[1] * 2.48
    h_2 = params[2] * 2.48
    inclination = params[3]
    original_labels = params[4]
    labels = science_convert(params[4])

    # the plot basis is set out where the labels, scales and title is set
    fig, ax = plt.subplots()
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.xscale('linear')
    plt.yscale('linear')
    plt.title(labels[0] + " vs " + labels[1])

    # the ellipses and center are plotted onto the graph
    ell_1 = Ellipse(xy=center, width=w_1, height=h_1, angle=math.degrees(inclination), edgecolor='b', ls='-', lw=1, facecolor='none')
    ell_2 = Ellipse(xy=center, width=w_2, height=h_2, angle=math.degrees(inclination), edgecolor='b', ls='--', lw=1, facecolor='none')
    plt.scatter(center[0], center[1], 4, c='r')
    ax.add_artist(ell_1)
    ax.add_artist(ell_2)

    # the graph limits are calculated and set
    y_lower = center[1] - h_2
    y_upper = center[1] + h_2
    x_lower = center[0] - w_2
    x_upper = center[0] + w_2
    plt.ylim(y_lower, y_upper)
    plt.xlim(x_lower, x_upper)

    # the graph legend is created and set in the upper right position
    ax.legend((ell_1, ell_2), (r'1 - $\alpha$', r'2 - $\alpha$'), loc='upper right')

    # the 500 points are created by gaussian realization and plotted on the graph
    random_points_w = rnd.normal(center[0], w_2 / 4, 500)
    random_points_h = rnd.normal(center[1], h_2 / 4, 500)
    for i in range(500):
        p_w = random_points_w[i]
        p_h = random_points_h[i]
        p_w, p_h = transformation(center[0], center[1], p_w, p_h, inclination)
        plt.scatter(p_w, p_h, 1, c='black')

    # the graph is saved and show to the user
    plt.subplots_adjust(left=0.15, right=0.95, top=0.85, bottom=0.2)
    plt.savefig(original_labels[0] + "_vs_" + original_labels[1] + ".png")
    plt.show()


matrix = get_covariance_matrix("base_w_plikHM_TTTEEE_lowl_lowE_BAO_Riess18_Pantheon.covmat") # the file is read

# the specified matrices are created
bh2_ch2_obj = Matrix("omegabh2", "omegach2", matrix)
bh2_ch2_obj.print_covariance_matrix()
bh2_ch2_obj.print_fisher_matrix()
plot(bh2_ch2_obj.ellipse_params())


ch2_w_obj = Matrix("omegach2", "w", matrix)
ch2_w_obj.print_covariance_matrix()
ch2_w_obj.print_fisher_matrix()
plot(ch2_w_obj.ellipse_params())

logA_ns_obj = Matrix("logA", "ns", matrix)
logA_ns_obj.print_covariance_matrix()
logA_ns_obj.print_fisher_matrix()
plot(logA_ns_obj.ellipse_params())

tau_w_obj = Matrix("tau", "w", matrix)
tau_w_obj.print_covariance_matrix()
tau_w_obj.print_fisher_matrix()
plot(tau_w_obj.ellipse_params())
