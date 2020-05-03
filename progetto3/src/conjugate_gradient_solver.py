"""
This module contains the ConjugateGradientSolver class, which is a subclass of the AbstractIterativeSolver class and
simply overrides the method for updating the x solution based on the Conjugate Gradient update strategy
"""

from abstract_iterative_solver import AbstractIterativeSolver


class ConjugateGradientSolver(AbstractIterativeSolver):

    # Constructor: additionally to the information stored by the superclass, it also initializes the value for the d_k
    # vector
    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.d_k = self.residual

    # This method computes the next vector solution x based on the Conjugate Gradient update strategy
    def update(self):
        y_k = self.A.dot(self.d_k)
        alpha = self.compute_alpha(y_k)
        self.x = self.x + alpha * self.d_k
        self.residual = self.compute_residual()
        beta = self.compute_beta(y_k)
        self.d_k = self.residual - beta * self.d_k
        return self.x

    # This is a helper function for the update() method and simply computes the value of "alpha"
    def compute_alpha(self, y_k):
        alpha_numerator = self.d_k.dot(self.residual)
        alpha_denominator = self.d_k.dot(y_k)
        return alpha_numerator / alpha_denominator

    # This is a helper function for the update() method and simply computes the value of "beta"
    def compute_beta(self, y_k):
        beta_numerator = self.d_k.dot(self.A.dot(self.residual))
        beta_denominator = self.d_k.dot(y_k)
        return beta_numerator / beta_denominator
