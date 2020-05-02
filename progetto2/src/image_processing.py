# This module contains the logic for processing the image in input

from tqdm import tqdm
from scipy import fft


# This function is used to cutoff the frequencies of the Minimum Coded Unit (MCU), that is to set
# the c_(k,l) coefficients to zero when (k + l) >= d
def cutoff_frequencies(mcu, d):
    for k in range(0, mcu.shape[0]):
        for l in range(0, mcu.shape[1]):
            if k + l >= d:
                mcu[k, l] = 0
    return mcu


# This function is used to round the coefficients of the Minimum Coded Unit (MCU) to the nearest integer value.
# In addition, this function also adjusts the coefficients of the MCU in such a way that their values is contained
# in the [0, 255] interval
def adjust_coefficients(mcu):
    for i in range(0, mcu.shape[0]):
        for j in range(0, mcu.shape[1]):
            mcu[i, j] = max(0, min(round(mcu[i, j]), 255))
    return mcu


# This method implements the core function of this module. It receives the image to process, the F value and the d
# value in input and it applies the compression algorithm
def process_image(img_to_process, f, d):

    # copy the image in input and work on the copied image from now on,
    # so that the function won't destroy the image in input
    img = img_to_process.copy()

    nrows = img.shape[0]
    ncols = img.shape[1]

    for start_mcu_row in tqdm(range(0, nrows, f)):
        for start_mcu_col in range(0, ncols, f):

            # compute the indices to identify a Minimum Coded Unit (MCU)
            end_mcu_row = start_mcu_row + f
            end_mcu_col = start_mcu_col + f

            # extract the mcu from the image to process
            mcu = img[start_mcu_row:end_mcu_row, start_mcu_col:end_mcu_col]

            # if the mcu is a FxF square matrix, then compress the mcu
            if mcu.shape[0] == f and mcu.shape[1] == f:
                mcu = fft.dctn(mcu, type=2, norm="ortho")
                mcu = cutoff_frequencies(mcu, d)
                mcu = fft.idctn(mcu, type=2, norm="ortho")
                mcu = adjust_coefficients(mcu)

            # save the processed mcu in its original position inside the matrix representing the image being processed
            img[start_mcu_row:end_mcu_row, start_mcu_col:end_mcu_col] = mcu

    return img
