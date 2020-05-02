from numpy import ones
from numpy.linalg import norm
from jacobi_solver import JacobiSolver
from gauss_seidel_solver import GaussSeidelSolver
from gradient_solver import GradientSolver
from conjugate_gradient_solver import ConjugateGradientSolver
import time


class IterativeSolverComparator:

    def __init__(self, A):
        self.A = A
        self.x_es = ones(A.shape[0])
        self.b = A.dot(self.x_es)
        self.tol = [1e-4, 1e-6, 1e-8, 1e-10]

    def print_results(self, solver):
        time_start = time.time()
        x_app, num_iter = solver.solve()
        time_end = time.time()
        exec_time = time_end - time_start
        rel_error = norm(self.x_es - x_app) / norm(self.x_es)
        print("Relative error = " + "{:.32e}".format(rel_error))
        print("Number of iterations = %d" % num_iter)
        print("Execution time = " + "{:.32e}".format(exec_time))
        print("\n\n")

    def start_comparison(self):
        for tolerance in self.tol:
            #print("\nJacobi solver results with tolerance = " + "{:.0e}".format(tolerance) + ":\n")
            #jacobi = JacobiSolver(self.A, self.b, tolerance)
            #self.print_results(jacobi)
            #print("\nGauss-Seidel solver results with tolerance = " + "{:.0e}".format(tolerance) + ":\n")
            #gauss = GaussSeidelSolver(self.A, self.b, tolerance)
            #self.print_results(gauss)
            #print("\nGradient solver results with tolerance = " + "{:.0e}".format(tolerance) + ":\n")
            #gradient = GradientSolver(self.A, self.b, tolerance)
            #self.print_results(gradient)
            print("\nConjugate Gradient solver results with tolerance = " + "{:.0e}".format(tolerance) + ":\n")
            conjugate_gradient = ConjugateGradientSolver(self.A, self.b, tolerance)
            self.print_results(conjugate_gradient)
