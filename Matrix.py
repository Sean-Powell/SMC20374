import numpy as np
import math

# a class that holds all the functions to do with the matrices


class Matrix:
    label_1 = ""
    label_2 = ""
    covariance_matrix = []
    fisher_matrix = []
    mean_values = {}

    def __init__(self, label_1, label_2, original_matrix, mean_values):
        self.label_1 = label_1
        self.label_2 = label_2
        self.covariance_matrix, self.fisher_matrix = self.create_matrices(original_matrix)
        self.mean_values = mean_values

    def create_matrices(self, matrix_in):  # creates the covariance and fisher matrix of the parameters
        temp_matrix = matrix_in
        labels = temp_matrix[0]

        label_1_pos = -1
        label_2_pos = -1
        pos = -1

        for label in labels:
            if label == self.label_1:
                label_1_pos = pos
            if label == self.label_2:
                label_2_pos = pos
            pos += 1

        a = temp_matrix[label_1_pos + 1][label_1_pos]
        b = temp_matrix[label_1_pos + 1][label_2_pos]
        c = temp_matrix[label_2_pos + 1][label_1_pos]
        d = temp_matrix[label_2_pos + 1][label_2_pos]

        c_out = [[a, b], [c, d]]

        try:
            fisher_matrix = np.linalg.inv(np.array(c_out))
            f_out = [[fisher_matrix[0][0], fisher_matrix[0][1]], [fisher_matrix[1][0], fisher_matrix[1][1]]]
        except np.linalg.LinAlgError:
            print("There was an error when calculating the inverse of the covariance matrix")
            f_out = []

        return c_out, f_out

    def print_covariance_matrix(self):  # prints out the covariance matrix to the console
        s1_length = len(self.label_1)
        s2_length = len(self.label_2)

        a_length = len(str(self.covariance_matrix[0][0]))
        c_length = len(str(self.covariance_matrix[0][1]))

        p2 = max(s1_length, s2_length)
        p1 = max(s1_length, a_length, c_length)

        print("--Covariance Matrix--")
        print(p2 * " ", self.label_1 + (p1 - s1_length) * " ", self.label_2)
        print(self.label_1 + (p2 - s1_length) * " ", str(self.covariance_matrix[0][0]) + (p1 - a_length) * " ",
              self.covariance_matrix[0][1])
        print(self.label_2 + (p2 - s2_length) * " ", str(self.covariance_matrix[1][0]) + (p1 - c_length) * " ",
              self.covariance_matrix[1][1])
        print("-" * 21)

    def print_fisher_matrix(self):  # prints the fisher matrix to the console
        s1_length = len(self.label_1)
        s2_length = len(self.label_2)

        a_length = len(str(self.fisher_matrix[0][0]))
        c_length = len(str(self.fisher_matrix[0][1]))

        p2 = max(s1_length, s2_length)
        p1 = max(s1_length, a_length, c_length)

        print("----Fisher Matrix----")
        print(p2 * " ", self.label_1 + (p1 - s1_length) * " ", self.label_2)
        print(self.label_1 + (p2 - s1_length) * " ", str(self.fisher_matrix[0][0]) + (p1 - a_length) * " ", self.fisher_matrix[0][1])
        print(self.label_2 + (p2 - s2_length) * " ", str(self.fisher_matrix[1][0]) + (p1 - c_length) * " ", self.fisher_matrix[1][1])
        print("-" * 21)

    def get_fisher_matrix(self):  # returns the fisher matrix
        return self.fisher_matrix

    def get_covariance_matrix(self):  # returns the covariance matrix
        return self.covariance_matrix

    # @staticmethod
    # def get_mean_value(s1):
    #     if s1 == "omegabh2":
    #         return 0.022
    #     if s1 == "omegach2":
    #         return 0.12
    #     if s1 == "w":
    #         return -1
    #     if s1 == "logA":
    #         return -19.94
    #     if s1 == "ns":
    #         return 0.96
    #     if s1 == "tau":
    #         return 0.09

    def get_mean_value(self, s1):
        return self.mean_values[s1]

    def get_center(self):  # returns the center of the ellipse based on the labels given
        return [self.get_mean_value(self.label_1), self.get_mean_value(self.label_2)]

    def get_labels(self):  # returns the labels
        return [self.label_1, self.label_2]

    def get_ellipse_params(self):
        # calculates the a b and theta values and returns the center, a, b, -theta and the labels
        sigma_x2 = self.covariance_matrix[0][0]
        sigma_y2 = self.covariance_matrix[1][1]
        sigma_xy2 = self.covariance_matrix[1][0]

        sub_fract = (sigma_x2 + sigma_y2) / 2
        sub_sqrt = math.sqrt((math.pow(sigma_x2 - sigma_y2, 2) / 4) + math.pow(sigma_xy2, 2))
        a = math.sqrt(sub_fract + sub_sqrt)
        b = math.sqrt(sub_fract - sub_sqrt)
        theta = np.arctan((2 * sigma_xy2) / (sigma_x2 - sigma_y2)) / 2

        return self.get_center(), a, b, -theta, self.get_labels()
        # returns -theta cause otherwise the inclination was inverted.
