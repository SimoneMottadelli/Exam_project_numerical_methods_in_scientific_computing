"""
This module contains the GussSeidelSolver class, which is a subclass of the AbstractIterativeSolver class and simply
overrides the method for updating the x solution based on the Gauss-Seidel update strategy
"""

import numpy as np
import scipy.sparse as sp
from abstract_iterative_solver import AbstractIterativeSolver
from forward_substitution_solver import ForwardSubstitutionSolver


class GaussSeidelSolver(AbstractIterativeSolver):

    # Constructor: additionally to the information stored by the superclass, it also stores the "P" matrix, which is the
    # lower triangular matrix of the factorization of the "A" matrix. It is used inside the update() method for
    # computing the next x vector solution
    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        if sp.issparse(A):
            self.P = sp.tril(self.A, format="lil")
        else:
            self.P = np.tril(self.A)

    # This method simply computes the next vector solution x
    def update(self):
        return self.x + ForwardSubstitutionSolver(self.P, self.residual).solve()
