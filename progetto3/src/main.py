"""
This module implements the entry point of the program and controls the execution flow
"""

import sys
from mtx_file_reader import MTXFileReader
from iterative_solver_comparator import IterativeSolverComparator
from input_parser import InputParser

def main(argv):
    # input validation
    mtx_file, sparse = InputParser(argv).parse()

    # matrix extraction from the .mtx file
    file_reader = MTXFileReader(mtx_file)
    A = file_reader.load_matrix(sparse=sparse)

    # launch comparison
    comparator = IterativeSolverComparator(A)
    comparator.start_comparison()


if __name__ == '__main__':
    main(sys.argv)
