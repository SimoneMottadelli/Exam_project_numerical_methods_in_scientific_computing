"""
This module contains the GradientSolver class, which is a subclass of the AbstractIterativeSolver class and simply
overrides the method for updating the x solution based on the Gradient update strategy
"""

from abstract_iterative_solver import AbstractIterativeSolver


class GradientSolver(AbstractIterativeSolver):

    # This method computes the next x vector solution using the Gradient update strategy
    def update(self):
        alpha = self.compute_alpha()
        return self.x + alpha * self.residual

    # This is a helper function for the update() method and simply computes the value of "alpha"
    def compute_alpha(self):
        alpha_numerator = self.residual.dot(self.residual)
        alpha_denominator = self.residual.dot(self.A.dot(self.residual))
        return alpha_numerator / alpha_denominator
