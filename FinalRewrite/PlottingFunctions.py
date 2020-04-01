import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse
import math


def convert_labels(labels):
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


def transform(origin_x, origin_y, point_x, point_y, theta):
    sin = math.sin(theta)
    cos = math.cos(theta)

    point_x -= origin_x
    point_y -= origin_y

    x_new = (point_x * cos) - (point_y * sin)
    y_new = (point_x * sin) + (point_y * cos)

    x_prime = x_new + origin_x
    y_prime = y_new + origin_y

    return x_prime, y_prime


def calculate_limits(center, offset):
    return center - offset, center + offset


def scatter_random_points(center, w_2, h_2, inclination, number_of_points):
    random_w = rnd.normal(center[0], w_2 / 4, number_of_points)
    random_h = rnd.normal(center[1], h_2 / 4, number_of_points)

    for i in range(number_of_points):
        x_new, y_new = transform(center[0], center[1], random_w[i], random_h[i], inclination)
        plt.scatter(x_new, y_new, 1, c='black')


def plot_graph(center, width, height, inclination, labels):
    w_1 = width * 1.52
    h_1 = height * 1.52
    w_2 = width * 2.48
    h_2 = height * 2.48
    science_labels = convert_labels(labels)

    fig, ax = plt.subplots()
    plt.xlabel(science_labels[0])
    plt.ylabel(science_labels[1])
    plt.xscale('linear')
    plt.ylabel('linear')
    plt.title(science_labels[0] + " vs " + science_labels[1])

    ellipsis_1 = Ellipse(xy=center, width=w_1, height=h_1, angle=math.degrees(inclination), edgecolor='b', ls='-', lw=1,
                         facecolor='none')
    ellipsis_2 = Ellipse(xy=center, width=w_2, height=h_2, angle=math.degrees(inclination), edgecolor='b', ls='--', lw=1,
                         facecolor='none')
    ax.add_artist(ellipsis_1)
    ax.add_artist(ellipsis_2)

    plt.ylim(calculate_limits(center[1], h_2))
    plt.xlim(calculate_limits(center[0], w_2))

    ax.legend((ellipsis_1, ellipsis_2), (r'1 - $\alpha$', r'2 - $\alpha$'), loc='upper right')
    scatter_random_points(center, w_2, h_2, inclination, 500)
    plt.scatter(center[0], center[1], 4, c='r')

    plt.subplots_adjust(left=0.15, right=0.95, top=0.85, bottom=0.2)
    plt.savefig("current_plot.png")
    # plt.show()



