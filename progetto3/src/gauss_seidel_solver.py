"""
This module contains the GussSeidelSolver class, which is a subclass of the AbstractIterativeSolver class and simply
overrides the method for updating the x solution based on the Gauss-Seidel update strategy
"""

from scipy.sparse import tril
from scipy.sparse.linalg import spsolve_triangular
from abstract_iterative_solver import AbstractIterativeSolver

class GaussSeidelSolver(AbstractIterativeSolver):

    # Constructor: additionally to the information stored by the superclass, it also stores the "P" matrix, which is the
    # lower triangular matrix of the factorization of the "A" matrix. It is used inside the update() method for
    # computing the next x vector solution
    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.P = tril(self.A, format="csr")

    # This method simply computes the next vector solution x
    def update(self):
        return self.x + spsolve_triangular(self.P, self.residual)