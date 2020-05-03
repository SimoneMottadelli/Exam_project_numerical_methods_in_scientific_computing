"""
This module contains the JacobiSolver class, which is a subclass of the AbstractIterativeSolver class and simply
overrides the method for updating the x solution based on the Jacobi update strategy
"""

from numpy import zeros
from abstract_iterative_solver import AbstractIterativeSolver


class JacobiSolver(AbstractIterativeSolver):

    # Constructor: additionally to the information stored by the superclass, it also stores the "P_inv_dot_residual"
    # vector which represents the result of the dot product between the inverse of the "P" lower diagonal matrix and the
    # residual vector. It is used inside the update() method for computing the next x vector solution
    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.P_inv_dot_residual = zeros(len(A))

    # This function implements the update strategy of the Jacobi method
    def update(self):
        for i in range(0, len(self.P_inv_dot_residual)):
            self.P_inv_dot_residual[i] = self.residual[i] / self.A[i, i]
        return self.x + self.P_inv_dot_residual
