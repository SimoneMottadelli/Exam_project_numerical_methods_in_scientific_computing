from abstract_iterative_solver import AbstractIterativeSolver
from numpy import zeros


class ConjugateGradientSolver(AbstractIterativeSolver):

    def __init__(self, A, b, tol):
        self.A = A
        self.b = b
        self.x = zeros(self.A.shape[0])
        self.d_k = self.compute_residual()
        super(ConjugateGradientSolver, self).__init__(A, b, tol)

    def update(self):
        alpha_numerator = self.d_k.dot(self.residual)
        alpha_denominator = self.d_k.dot(self.A.dot(self.d_k))
        alpha = alpha_numerator / alpha_denominator
        self.x = self.x + alpha * self.d_k
        self.residual = self.compute_residual()
        beta_numerator = self.d_k.dot(self.A.dot(self.residual))
        beta_denominator = self.d_k.dot(self.A.dot(self.d_k))
        beta = beta_numerator / beta_denominator
        self.d_k = self.residual - beta * self.d_k
        return self.x
