# This module implements the comparison between my implementation of the dct2 function and the one provided by the
# scipy library

from scipy import fft
from my_dct2 import my_dct2
from results import plot_results, save_results_on_file
from numpy.random import randint
from tqdm import tqdm
import time
import sys


# This function is used to compare the execution time of my_dct2 implementation and
# the one of the scipy library. In particular, a semi log graph is
# plotted, where the x-axis represents the dimension of the square matrix
# processed by the two functions, while the y-axis represents the time in
# milliseconds in log scale.
# "max_dim" is the maximum dimension of the matrices that will be processed
# "step" is used to generate the dimensions of the matrices that will be processed
def compare(max_dim, step):
    # "my_time" contains the execution time of my dct2 at the varying
    # of the matrix dimension
    my_time = []

    # lib_time contains the execution time of the dct2 of the library
    # at the varying of the matrix dimension
    lib_time = []

    # "dim_matrix" contains the dimensions of the matrices that will be
    # processed by the dct2 functions
    dim_matrix = list(range(2, max_dim, step))
    if max_dim not in dim_matrix:
        dim_matrix.append(max_dim)

    # start computing the dct2 functions on the matrices at the varying of their dimensions
    for n in tqdm(dim_matrix):
        # generate a random matrix of dimension NxN
        m = randint(0, 255, size=(n, n))

        # execute my dct2 implementation on the generated matrix and compute the execution time
        start_execution_time = time.time()
        my_dct2(m)
        end_execution_time = time.time()
        my_time.append(end_execution_time - start_execution_time)

        # execute the dct2 of the library on the generated matrix and compute the execution time
        start_execution_time = time.time()
        fft.dctn(m, type=2, norm="ortho")
        end_execution_time = time.time()
        lib_time.append(end_execution_time - start_execution_time)

    return my_time, lib_time, dim_matrix


def main(argv):
    max_dim = int(argv[1])
    step = int(argv[2])
    my_time, lib_time, dim_matrix = compare(max_dim, step)
    plot_results(my_time, lib_time, dim_matrix)
    save_results_on_file(my_time, lib_time, dim_matrix, step)


if __name__ == '__main__':
    main(sys.argv)