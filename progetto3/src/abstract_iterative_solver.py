"""
This module contains the implementation of the AbstractIterativeSolver class, which is a general class that can be
extended to implement different variants of an iterative method for solving linear systems of equations.
In particular, it implements the general template for an iterative method. Classes that extend the
AbstractIterativeSolver have to override the update() method only.
"""

from numpy.linalg import norm
from numpy import zeros


class AbstractIterativeSolver:

    # Constructor: it stores the information of the linear system of equations to be solved and the data of the
    # current iteration
    def __init__(self, A, b, tol):
        self.A = A
        self.b = b
        self.tol = tol
        self.x = zeros(len(A))
        self.max_iter = 20000
        self.current_iter = 1
        self.residual = self.compute_residual()

    # Helper method to compute the residual, which is used by the stopping criterion
    def compute_residual(self):
        return self.b - self.A.dot(self.x)

    # Helper method that returns TRUE if the solver must continue to iterate, FALSE otherwise. In particular, the solver
    # must stop to iterate (then it returns FALSE) when the maximum number of iterations is reached or the residual
    # error is less than the tolerance
    def must_continue(self):
        if self.current_iter >= self.max_iter:
            print("[WARNING] max number of iterations reached: solver failed to achieve convergence!")
            return False
        elif norm(self.residual) / norm(self.b) < self.tol:
            return False
        else:
            return True

    # Template method for a classical iterative method
    def solve(self):
        while self.must_continue():
            self.x = self.update()
            self.residual = self.compute_residual()
            self.current_iter += 1
        return self.x, self.current_iter

    # Method that must be overridden by the subclasses. It must implement the strategy to update the next x solution
    def update(self):
        raise NotImplementedError("This method has not been implemented yet")
