"""
This module implements the Parser class, which is responsible of the user input validation
"""

from os.path import isfile
from sys import exit

class InputParser:

    # Constructor: get the user input from the argv parameter
    def __init__(self, argv):
        self.argv = argv

    # Method that parses the user input and shows errors to the user if it is not valid
    def parse(self):
        if len(self.argv) <= 1:
            print("\n[ERROR] a filepath must be specified in input! Example: python main.py myfile.mtx\n")
            exit(1)
        elif not isfile(self.argv[1]):
            print("\n[ERROR] file \"%s\" does not exist in the filesystem!\n" % self.argv[1])
            exit(2)

        sparse = True
        if len(self.argv) == 3 and self.argv[2] == "-dense":
            print("\n[INFO] matrix format selected: dense.\n")
            sparse = False
        else:
            print("\n[INFO] matrix format selected: sparse. Use \"-dense\" option to change it. Example: "
                  "python main.py myfile.mtx -dense\n")

        return self.argv[1], sparse
