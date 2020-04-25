# This module is used to wrap the scify library and implement the dct2 and idct2 using its implementation of the dct1
# and idct1 functions

from scipy import fft


# This method wraps the dct2 function of the scipy library
def lib_dct2(m):
    return fft.dct(fft.dct(m, norm="ortho", axis=0), norm="ortho", axis=1)


# This method wraps the idct2 function of the scipy library
def lib_idct2(m):
    return fft.idct(fft.idct(m, axis=0, norm="ortho"), norm="ortho", axis=1)