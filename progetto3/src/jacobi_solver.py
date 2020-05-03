from numpy import zeros
from abstract_iterative_solver import AbstractIterativeSolver


class JacobiSolver(AbstractIterativeSolver):

    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.P_inv_dot_residual = zeros(len(A))

    def update(self):
        for i in range(0, len(self.P_inv_dot_residual)):
            self.P_inv_dot_residual[i] = self.residual[i] / self.A[i, i]
        return self.x + self.P_inv_dot_residual
