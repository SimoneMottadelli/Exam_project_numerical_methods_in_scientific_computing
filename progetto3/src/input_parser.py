"""
This module implements the Parser class, which is responsible of the user input validation
"""

from os.path import isfile
from sys import exit


class InputParser:

    # Method that parses the user input and shows errors to the user if it is not valid
    def parse(self, argv):
        if len(argv) <= 1:
            print("\n[ERROR] a filepath must be specified in input! Example: python main.py myfile.mtx\n")
            exit(1)
        elif not isfile(argv[1]):
            print("\n[ERROR] file \"%s\" does not exist in the filesystem!\n" % argv[1])
            exit(2)

        return argv[1]
