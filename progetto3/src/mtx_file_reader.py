"""
This module implements the MTXFileReader class, which is the class responsible for loading from the .mtx file the matrix
specified in input to the program
"""

from numpy import zeros
from scipy.sparse import lil_matrix

class MTXFileReader:

    # Constructor: it opens the .mtx file from the filesystem
    def __init__(self, filepath):
        self.mtx_file = open(filepath, "r")

    # This function retrieves and reads the matrix from the filesystem and
    # returns a matrix in output.
    def load_matrix(self, sparse=True):
        # read the header of the .mtx file
        header = self.mtx_file.readline().split("  ")

        # get the matrix dimension from the header
        dim = int(header[0])

        if sparse:
            A = lil_matrix((dim, dim))
        else:
            A = zeros((dim, dim))

        # fill the matrix with the coefficients
        for line_in_file in self.mtx_file:
            split_line = line_in_file.split("  ")
            row_index = int(split_line[0])
            col_index = int(split_line[1])
            coefficient = float(split_line[2].strip())
            A[row_index - 1, col_index - 1] = coefficient

        return A
