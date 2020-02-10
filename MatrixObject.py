import numpy as np
import math


class Matrix:
    label_1 = ""
    label_2 = ""
    covariance_matrix = []
    fisher_matrix = []

    def __init__(self, s1, s2, original_matrix):
        self.label_1 = s1
        self.label_2 = s2
        self.covariance_matrix, self.fisher_matrix = self.create_matrices(self.label_1, self.label_2, original_matrix)

    @staticmethod
    def create_matrices(s1, s2, covariance_matrix_in):
        temp_matrix = covariance_matrix_in
        labels = temp_matrix[0]

        s1_pos = -1
        s2_pos = -1
        pos = -1

        for label in labels:
            if label == s1:
                s1_pos = pos
            if label == s2:
                s2_pos = pos
            pos = pos + 1

        a = temp_matrix[s1_pos + 1][s1_pos]
        b = temp_matrix[s1_pos + 1][s2_pos]
        c = temp_matrix[s2_pos + 1][s1_pos]
        d = temp_matrix[s2_pos + 1][s2_pos]

        covariance_matrix_out = [[a, b],
                                 [c, d]]

        try:
            fisher_matrix = np.linalg.inv(np.array([[a, b], [c, d]]))

            fisher_matrix = [[fisher_matrix[0][0], fisher_matrix[0][1]],
                             [fisher_matrix[1][0], fisher_matrix[1][1]]]
        except np.linalg.LinAlgError:
            fisher_matrix = []

        return covariance_matrix_out, fisher_matrix

    def print_covariance_matrix(self):
        s1_length = len(self.label_1)
        s2_length = len(self.label_2)

        a_length = len(str(self.covariance_matrix[0][0]))
        c_length = len(str(self.covariance_matrix[0][1]))

        p2 = max(s1_length, s2_length)
        p1 = max(s1_length, a_length, c_length)

        print("--Covariance Matrix--")
        print(p2 * " ", self.label_1 + (p1 - s1_length) * " ", self.label_2)
        print(self.label_1 + (p2 - s1_length) * " ", str(self.covariance_matrix[0][0]) + (p1 - a_length) * " ", self.covariance_matrix[0][1])
        print(self.label_2 + (p2 - s2_length) * " ", str(self.covariance_matrix[1][0]) + (p1 - c_length) * " ", self.covariance_matrix[1][1])
        print("-" * 21)

    def print_fisher_matrix(self):
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

    def get_fisher_matrix(self):
        return self.fisher_matrix

    def get_covariance_matrix(self):
        return self.covariance_matrix

    def get_mean_value(self, s1):
        if s1 == "omegabh2":
            return 0.022
        if s1 == "omegach2":
            return 0.12
        if s1 == "w":
            return -1
        if s1 == "logA":
            return -19.94
        if s1 == "ns":
            return 0.96
        if s1 == "tau":
            return 0.09

    def get_center(self):
        return [self.get_mean_value(self.label_1), self.get_mean_value(self.label_2)]

    def get_labels(self):
        return [self.label_1, self.label_2]

    def get_ellipse_params(self):
        sigma_x2 = self.covariance_matrix[0][0]
        sigma_y2 = self.covariance_matrix[1][1]
        sigma_xy2 = math.pow(self.covariance_matrix[1][0], 2)

        sub_a = (sigma_x2 + sigma_y2) / 2
        sub_sqrt = math.sqrt((math.pow(sigma_x2 - sigma_y2, 2) / 4) + sigma_xy2)
        a = np.sqrt(sub_a + sub_sqrt)
        b = np.sqrt(sub_a - sub_sqrt)
        theta = math.degrees(np.arctan((2 * self.covariance_matrix[1][0]) / (sigma_x2 - sigma_y2)) / 2)

        return [self.get_center(), a, b, theta, self.get_labels()]
