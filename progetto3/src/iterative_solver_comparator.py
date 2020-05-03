"""
This module contains the IterativeSolverComparator class, which implements the logic for comparing the following four
solvers with respect to their performances on the matrix given as input to the program:
- Jacobi
- Gauss-Seidel
- Gradient
- Conjugate Gradient
"""

from numpy import ones
from numpy.linalg import norm
from jacobi_solver import JacobiSolver
from gauss_seidel_solver import GaussSeidelSolver
from gradient_solver import GradientSolver
from conjugate_gradient_solver import ConjugateGradientSolver
import time


class IterativeSolverComparator:

    # Constructor: it stores the A matrix; it builds an exact solution x; it builds the b vector using the A matrix and
    # the exact solution x; it initializes the tolerance vector
    def __init__(self, A):
        self.A = A
        self.x_es = ones(A.shape[0])
        self.b = A.dot(self.x_es)
        self.tol = [1e-4, 1e-6, 1e-8, 1e-10]

    # This is a helper method for the start_comparison() method: it simply prints the results achieved by a solver to
    # the console
    def print_results(self, solver):
        time_start = time.time()
        x_app, num_iter = solver.solve()
        time_end = time.time()
        exec_time = time_end - time_start
        rel_error = norm(self.x_es - x_app) / norm(self.x_es)
        print("Relative error = " + "{:.32e}".format(rel_error))
        print("Number of iterations = %d" % num_iter)
        print("Execution time = " + "{:.32e}".format(exec_time))
        print("")

    # This method simply solves the linear systems with the four different solver to the varying of the tolerance and
    # shows the achieved results on the console
    def start_comparison(self):
        for tolerance in self.tol:
            print("\nJacobi solver results with tolerance = " + "{:.0e}".format(tolerance) + ":")
            jacobi = JacobiSolver(self.A, self.b, tolerance)
            self.print_results(jacobi)
            print("\nGauss-Seidel solver results with tolerance = " + "{:.0e}".format(tolerance) + ":")
            gauss = GaussSeidelSolver(self.A, self.b, tolerance)
            self.print_results(gauss)
            print("\nGradient solver results with tolerance = " + "{:.0e}".format(tolerance) + ":")
            gradient = GradientSolver(self.A, self.b, tolerance)
            self.print_results(gradient)
            print("\nConjugate Gradient solver results with tolerance = " + "{:.0e}".format(tolerance) + ":")
            conjugate_gradient = ConjugateGradientSolver(self.A, self.b, tolerance)
            self.print_results(conjugate_gradient)
