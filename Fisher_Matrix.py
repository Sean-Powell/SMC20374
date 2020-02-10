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


def plot(params):
    center = params[0]
    w_1 = params[1] * 1.52
    h_1 = params[2] * 1.52
    w_2 = params[1] * 2.48
    h_2 = params[2] * 2.48

    inclination = params[3]
    labels = params[4]
    fig, ax = plt.subplots()
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.xscale('linear')
    plt.yscale('linear')
    plt.title(labels[0] + " vs " + labels[1])

    ell_1 = Ellipse(xy=center, width=w_1, height=h_1, angle=inclination, edgecolor='b', ls='-', lw=1, facecolor='none')
    ell_2 = Ellipse(xy=center, width=w_2, height=h_2, angle=inclination, edgecolor='b', ls='--', lw=1, facecolor='none')
    plt.scatter(center[0], center[1], 2, c='r')
    ax.add_artist(ell_1)
    ax.add_artist(ell_2)
    # plt.ylim(center[1] - w_2 / 2, center[1] + w_2 / 2)
    # plt.xlim(center[0] - h_1 / 2, center[0] + h_2 / 2)
    ax.margins(-0.03, -0.43)

    ax.legend((ell_1, ell_2), (r'1 - $\alpha$', r'2 - $\alpha$'))
    plt.savefig(labels[0] + " vs " + labels[1] + ".png", bbox_inches="tight", pad_inches=0)

    random_points_w = rnd.normal(center[0], params[1], 500)
    random_points_h = rnd.normal(center[1], params[2], 500)
    for i in range(500):
        p_w = random_points_w[i]
        p_h = random_points_h[i]
        plt.scatter(p_w, p_h, 2, c='black')
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

plot(bh2_ch2_obj.get_ellipse_params())
print("done")
