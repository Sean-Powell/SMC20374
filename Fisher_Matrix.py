import math
import matplotlib.pyplot as plt
import numpy.random as rnd
import numpy as np
from matplotlib.patches import Ellipse
from MatrixObject import Matrix


def get_covariance_matrix(file_path):
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
            line_split = line.split("  ")
            for entry in line_split:
                value = float(entry)
                if entry[0] == '-':
                    value = value * -1
                matrix_line.append(value)
            matrix.append(matrix_line)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for c in row:
            print(c, end=" ")
        print("\n", end="")
    print("-" * 10)


def science_convert(labels):
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


def plot(params):
    center = params[0]
    w_1 = params[1] * 1.52
    h_1 = params[2] * 1.52
    w_2 = params[1] * 2.48
    h_2 = params[2] * 2.48

    inclination = params[3]
    original_labels = params[4]
    labels = science_convert(params[4])
    fig, ax = plt.subplots()
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.xscale('linear')
    plt.yscale('linear')
    plt.title(labels[0] + " vs " + labels[1])

    ell_1 = Ellipse(xy=center, width=w_1, height=h_1, angle=inclination, edgecolor='b', ls='-', lw=1, facecolor='none')
    ell_2 = Ellipse(xy=center, width=w_2, height=h_2, angle=inclination, edgecolor='b', ls='--', lw=1, facecolor='none')
    plt.scatter(center[0], center[1], 4, c='r')
    ax.add_artist(ell_1)
    ax.add_artist(ell_2)

    y_lower = center[1] - h_2
    y_upper = center[1] + h_2
    x_lower = center[0] - w_2
    x_upper = center[0] + w_2
    plt.ylim(y_lower, y_upper)
    plt.xlim(x_lower, x_upper)

    ax.legend((ell_1, ell_2), (r'1 - $\alpha$', r'2 - $\alpha$'), loc='upper right')

    random_points_w = rnd.normal(center[0], w_2 / 4, 500)
    random_points_h = rnd.normal(center[1], h_2 / 4, 500)
    for i in range(500):
        p_w = random_points_w[i]
        p_h = random_points_h[i]
        plt.scatter(p_w, p_h, 1, c='black')
    plt.savefig(original_labels[0] + " vs " + original_labels[1] + ".png", bbox_inches="tight", pad_inches=0)
    plt.show()


matrix = get_covariance_matrix("base_w_plikHM_TTTEEE_lowl_lowE_BAO_Riess18_Pantheon.covmat")

bh2_ch2_obj = Matrix("omegabh2", "omegach2", matrix)
ch2_w_obj = Matrix("omegach2", "w", matrix)
logA_ns_obj = Matrix("logA", "ns", matrix)
tau_w_obj = Matrix("tau", "w", matrix)

bh2_ch2_obj.print_covariance_matrix()
bh2_ch2_obj.print_fisher_matrix()
ch2_w_obj.print_covariance_matrix()
ch2_w_obj.print_fisher_matrix()
logA_ns_obj.print_covariance_matrix()
logA_ns_obj.print_fisher_matrix()
tau_w_obj.print_covariance_matrix()
tau_w_obj.print_fisher_matrix()

plot(tau_w_obj.get_ellipse_params())
print("done")
