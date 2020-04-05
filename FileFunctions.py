# reads the file given to obtain the 28x28 covariance matrix


def read_covariance_matrix(file_path):
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


def read_model(file_path):
    f = open(file_path)
    model_params = []
    for line in f:
        line = line.strip()
        model = line.split(",")
        model_params.append(model)
    return model_params


def read_fiducial(file_path):
    f = open(file_path)
    fiducial_values = {}
    for line in f:
        line.strip()
        line_split = line.split(",")
        try:
            fiducial_values[line_split[0]] = float(line_split[1])
        except ValueError:
            print("There is an invalid value of", line_split[1], "for", line_split[0])
    return fiducial_values
