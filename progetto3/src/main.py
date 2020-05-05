"""
This module implements the entry point of the program and controls the execution flow
"""

import sys
from mtx_file_reader import MTXFileReader
from iterative_solver_comparator import IterativeSolverComparator
from input_parser import InputParser

def main(argv):
    # input validation
    mtx_file = InputParser(argv).parse()

    # matrix extraction from the .mtx file
    A = MTXFileReader(mtx_file).load_matrix()

    # launch comparison
    tols = [1e-4, 1e-6, 1e-8, 1e-10]
    IterativeSolverComparator(A, tols).start_comparison()


if __name__ == '__main__':
    main(sys.argv)
