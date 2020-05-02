# This module contains the functions used to validate the user input

import os


# This function parses the arguments in "argv" to check whether the user input is correct and returns the parsed
# input to the caller method
def parse_arguments(argv):

    # syntax checking
    if len(argv) != 6 or argv[0] != "-f" or not argv[1].isdigit() or \
            argv[2] != "-d" or not argv[3].isdigit() or argv[4] != "-path":
        throw_error_msg()

    # extract the values of "F" and "d"
    f = int(argv[1])
    d = int(argv[3])

    # check whether the value of "d" is contained in the [0, 2 * F - 2] interval
    if d < 0 or d > (2 * f - 2):
        throw_error_msg()

    # extract the file path of the image to process
    path_to_img = argv[5]

    # check whether the image file exists
    if not os.path.isfile(path_to_img):
        print("[ERROR] File \"%s\" does not exist" % argv[5])
        exit(1)

    return f, d, path_to_img


def throw_error_msg():
    print("\n[ERROR] Syntax error\n")
    print("You have to specify the following options: \n")
    print("-f <integer value>  it is the width of the Minimum Coded Unit (MCU)"
          " on which the DCT2 will be executed;\n\n")
    print("-d <integer value>  it is the cutoff threshold of the frequencies and it must range"
          " from 0 to (2f - 2);\n\n")
    print("EXAMPLE: python main.py -f 8 -d 10 -path my_image.bmp")
    exit(1)
