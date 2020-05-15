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
from time import time


class IterativeSolverComparator:

    # This is a helper method for the start_comparison() method: it simply prints the results achieved by a solver to
    # the console
    def print_results(self, solver, x_es):
        time_start = time()
        x_app, num_iter = solver.solve()
        time_end = time()
        exec_time = "{:.32e}".format(time_end - time_start)
        rel_error = "{:.32e}".format(norm(x_es - x_app) / norm(x_es))
        formatted_tol = "{:.0e}".format(solver.tol)
        solver_name = type(solver).__name__
        print("\n%s results with tolerance = %s:" % (solver_name, formatted_tol))
        print("Relative error = %s" % rel_error)
        print("Number of iterations = %d" % num_iter)
        print("Execution time = %s\n" % exec_time)

    # This method simply solves the linear systems with the four different solver to the varying of the tolerance and
    # shows the achieved results on the console
    def start_comparison(self, A, tols, x_es=None):
        if x_es is None:
            x_es = ones(A.shape[0])
        b = A.dot(x_es)
        for tol in tols:
            self.print_results(JacobiSolver(A, b, tol), x_es)
            self.print_results(GaussSeidelSolver(A, b, tol), x_es)
            self.print_results(GradientSolver(A, b, tol), x_es)
            self.print_results(ConjugateGradientSolver(A, b, tol), x_es)
