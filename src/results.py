# This module contains the function used to display the results obtained with the image processing

import matplotlib.pyplot as plt
import os


# this function shows an interactive window containing two images side by side
def display_images(img1, img2):
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title('Image before compression')
    plt.imshow(img1, cmap=plt.get_cmap('gray'))
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(img2, cmap=plt.get_cmap('gray'))
    plt.title('Image after compression')
    plt.axis('off')
    plt.show()


# This function is used to save on a file the results of the comparison of the dct2 implementations
def save_results_on_file(my_dct2_time, lib_dct2_time, dimension_matrix, step):
    dir = "../results"
    if not os.path.isdir(dir):
        os.makedirs(dir)
    file_name = "%s/output_%d_step_%d.txt" % (dir, dimension_matrix[len(dimension_matrix) - 1], step)
    f = open(file_name, "w")

    f.write("Matrix dimensions: \n")
    f.write("[")
    for i in dimension_matrix[0 : len(dimension_matrix) - 1]:
        f.write(str(i) + ", ")
    f.write(str(dimension_matrix[len(dimension_matrix) - 1]))
    f.write("]\n\n")

    f.write("Execution time of my dct2 implementation: \n")
    f.write("[")
    for i in range(0, len(my_dct2_time) - 1):
        f.write(str(my_dct2_time[i]) + ", ")
    f.write(str(my_dct2_time[len(my_dct2_time) - 1]))
    f.write("]\n\n")

    f.write("Execution time of the dct2 of the library: \n")
    f.write("[")
    for i in range(0, len(lib_dct2_time) - 1):
        f.write(str(lib_dct2_time[i]) + ", ")
    f.write(str(lib_dct2_time[len(lib_dct2_time) - 1]))
    f.write("]")

    f.close()


# This function is used to plot the results of the comparison of the dct2 implementations
def plot_results(my_dct2_time, lib_dct2_time, dimension_matrix, step):
    plt.style.use('ggplot') # To improve visualization

    # build first line
    line_my_dct2, = plt.semilogy(dimension_matrix, my_dct2_time)
    line_my_dct2.set_label('my dct2 implementation')
    plt.setp(line_my_dct2, color="b", linestyle="--")

    # build second line
    line_lib_dct2, = plt.semilogy(dimension_matrix, lib_dct2_time)
    line_lib_dct2.set_label('dct2 of the library')
    plt.setp(line_lib_dct2, color="r")

    # add more graph info
    plt.title("Comparison between the dct2 implementations")
    plt.legend()
    plt.xlabel("Dimension of the matrix (NxN)")
    plt.ylabel("Time in seconds (log scale)")

    dir = "../results/"
    file_name = "%s/output_%d_step_%d.png" % (dir, dimension_matrix[len(dimension_matrix) - 1], step)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    plt.savefig("%s/%s" % (dir, file_name))

    # show graph
    plt.show()
