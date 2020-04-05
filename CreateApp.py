import FileFunctions
import UserInterface
from Matrix import Matrix

matrix = []


def run_functions(c_loc, m_loc, f_loc):
    # reads the file and creates the desired matrices based on the parameters given
    matrix = FileFunctions.read_covariance_matrix(c_loc)
    model = FileFunctions.read_model(m_loc)
    fiducial = FileFunctions.read_fiducial(f_loc)

    matrices = []
    for m in model:
        temp = Matrix(m[0], m[1], matrix, fiducial)
        temp.print_covariance_matrix()
        temp.print_fisher_matrix()
        matrices.append(temp)

    return matrices


# inputs for the file locations of the various parameters
covariance_location = input("Enter the file location of the covarience matrix\n")
model_location = input("Enter the file location of the model parameters\n")
fiducial_location = input("Enter the file location of the fiducial values\n")


matrices = run_functions(covariance_location, model_location, fiducial_location)  # calls the function to create the matrices
# matrices = run_functions("", "", "")
UserInterface.createGUI(matrices)  # calls the function to create the GUI
