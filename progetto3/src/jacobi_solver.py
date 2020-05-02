import numpy as np
from abstract_iterative_solver import AbstractIterativeSolver


class JacobiSolver(AbstractIterativeSolver):

    def update(self):
        P_inv_dot_residual = np.zeros(self.A.shape[0])
        for i in range(0, len(P_inv_dot_residual)):
            P_inv_dot_residual[i] = self.residual[i] / self.A[i, i]
        return self.x + P_inv_dot_residual
