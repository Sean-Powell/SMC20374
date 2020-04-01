from FinalRewrite import FileFunctions, PlottingFunctions, UserInterface
from FinalRewrite.Matrix import Matrix

matrix = []


def plot_matrix(matrix):
    center, width, height, inclination, labels = matrix.get_ellipse_params()
    PlottingFunctions.plot_graph(center, width, height, inclination, labels)


def run_functions():
    matrix = FileFunctions.get_covariance_matrix("../base_w_plikHM_TTTEEE_lowl_lowE_BAO_Riess18_Pantheon.covmat")
    total = 0.0
    for i in range(1, len(matrix)):
        total += float(matrix[i][0])
        print(matrix[i][0])

    print(total / (len(matrix) - 1))

    bh2_ch2_obj = Matrix("omegabh2", "omegach2", matrix)
    bh2_ch2_obj.print_covariance_matrix()
    bh2_ch2_obj.print_fisher_matrix()
    # plot_matrix(bh2_ch2_obj)

    ch2_w_obj = Matrix("omegach2", "w", matrix)
    ch2_w_obj.print_covariance_matrix()
    ch2_w_obj.print_fisher_matrix()
    # plot_matrix(ch2_w_obj)

    logA_ns_obj = Matrix("logA", "ns", matrix)
    logA_ns_obj.print_covariance_matrix()
    logA_ns_obj.print_fisher_matrix()
    # plot_matrix(ch2_w_obj)

    tau_w_obj = Matrix("tau", "w", matrix)
    tau_w_obj.print_covariance_matrix()
    tau_w_obj.print_fisher_matrix()
    # plot_matrix(tau_w_obj)

    matrices = [bh2_ch2_obj, ch2_w_obj, logA_ns_obj, tau_w_obj]
    return matrices


matrices = run_functions()
UserInterface.createGUI(matrices)
