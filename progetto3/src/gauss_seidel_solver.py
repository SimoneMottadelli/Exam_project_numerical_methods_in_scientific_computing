from numpy import tril
from abstract_iterative_solver import AbstractIterativeSolver
from forward_substitution_solver import ForwardSubstitutionSolver


class GaussSeidelSolver(AbstractIterativeSolver):

    def __init__(self, A, b, tol):
        super().__init__(A, b, tol)
        self.P = tril(self.A)

    def update(self):
        return self.x + ForwardSubstitutionSolver(self.P, self.residual).solve()
