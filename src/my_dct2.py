# This module contains my dct2 implementation

import numpy as np
from math import cos, sqrt

# This function applies the dct1 function over all the rows of the "mat" matrix in input
def my_dct(mat):
    nrows = mat.shape[0]
    ncols = mat.shape[1]
    c = np.zeros((nrows, ncols)) # matrix containing the result to return
    for row in range(0, nrows):
        for k in range(0, ncols):
            total_sum = 0
            for i in range(1, ncols + 1):
                total_sum += cos(np.pi * k * (2 * i - 1) / (2 * ncols)) * mat[row][i - 1]
            alpha_k = ncols if k == 0 else ncols * 0.5
            c[row][k] = total_sum / sqrt(alpha_k)
    return c


# This function implements the dct2 over a matrix
def my_dct2(m):
    return my_dct(my_dct(m).transpose()).transpose()
