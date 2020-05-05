"""
This module contains the JacobiSolver class, which is a subclass of the AbstractIterativeSolver class and simply
overrides the method for updating the x solution based on the Jacobi update strategy
"""

from abstract_iterative_solver import AbstractIterativeSolver
from scipy.sparse import identity, csr_matrix


class JacobiSolver(AbstractIterativeSolver):

    # Constructor: additionally to the information stored by the superclass, it also stores the inverse of the P matrix
    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.P_inv = csr_matrix(identity(A.shape[0]) / A.diagonal())

    # This function implements the update strategy of the Jacobi method
    def update(self):
        return self.x + self.P_inv.dot(self.residual)
