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
                matrix_line.append(float(entry))
            matrix.append(matrix_line)

    return matrix