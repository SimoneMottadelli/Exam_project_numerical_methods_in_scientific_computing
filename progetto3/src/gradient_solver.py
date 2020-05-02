from abstract_iterative_solver import AbstractIterativeSolver


class GradientSolver(AbstractIterativeSolver):

    def update(self):
        alpha_numerator = self.residual.dot(self.residual)
        alpha_denominator = self.residual.dot(self.A.dot(self.residual))
        alpha = alpha_numerator / alpha_denominator
        return self.x + alpha * self.residual
