from abstract_iterative_solver import AbstractIterativeSolver


class ConjugateGradientSolver(AbstractIterativeSolver):

    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.d_k = self.residual

    def update(self):
        y_k = self.A.dot(self.d_k)
        alpha = self.compute_alpha(y_k)
        self.x = self.x + alpha * self.d_k
        self.residual = self.compute_residual()
        beta = self.compute_beta(y_k)
        self.d_k = self.residual - beta * self.d_k
        return self.x

    def compute_alpha(self, y_k):
        alpha_numerator = self.d_k.dot(self.residual)
        alpha_denominator = self.d_k.dot(y_k)
        return alpha_numerator / alpha_denominator

    def compute_beta(self, y_k):
        beta_numerator = self.d_k.dot(self.A.dot(self.residual))
        beta_denominator = self.d_k.dot(y_k)
        return beta_numerator / beta_denominator
