"""
This module contains the ForwardSubstitutionSolver class, which implements the strategy for solving linear systems of
equations where "A" is a triangular matrix. It is a helper class for the GaussSeidelSolver.
"""

from numpy import zeros


class ForwardSubstitutionSolver:

    # Constructor that saves the "A" matrix and the "b" vector
    def __init__(self, L, b):
        self.L = L
        self.b = b

    # It solves the linear system of equations based on the forward substitution direct method
    def solve(self):
        n = self.L.shape[0]
        x = zeros(n)
        x[0] = self.b[0] / self.L[0, 0]
        for i in range(1, n):
            x[i] = (self.b[i] - self.L[i,].dot(x)) / self.L[i, i]
        return x
