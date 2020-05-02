# This module is the main module from which the whole computation starts

import sys
from results import display_images
from image_processing import process_image
from input_parser import parse_arguments
import numpy as np
from PIL import Image


def main(argv):
    f, d, path_to_img = parse_arguments(argv)
    img_before = np.array(Image.open(path_to_img).convert("L"))
    img_after = process_image(img_before, f, d)
    img_after = Image.fromarray(np.uint8(img_after))
    display_images(img_before, img_after)


if __name__ == '__main__':
    main(sys.argv[1:])