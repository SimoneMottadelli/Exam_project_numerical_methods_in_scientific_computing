"""
This module implements the entry point of the program
"""

import sys
import os
from mtx_file_reader import MTXFileReader
from iterative_solver_comparator import IterativeSolverComparator


def main(argv):
    # input validation
    if len(argv) <= 1:
        print("\n[ERROR] a filepath must be specified in input! Example: python main.py myfile.mtx\n")
        sys.exit(1)
    elif not os.path.isfile(argv[1]):
        print("\n[ERROR] file \"%s\" does not exist in the filesystem!\n" % argv[1])
        sys.exit(1)

    # matrix extraction from the .mtx file
    file_reader = MTXFileReader(argv[1])
    A = file_reader.load_matrix()

    # launch comparison
    comparator = IterativeSolverComparator(A)
    comparator.start_comparison()


if __name__ == '__main__':
    main(sys.argv)
