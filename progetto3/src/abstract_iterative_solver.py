from numpy.linalg import norm
from numpy import zeros

class AbstractIterativeSolver:

    def __init__(self, A, b, tol):
        self.A = A
        self.b = b
        self.tol = tol
        self.x = zeros(A.shape[0])
        self.max_iter = 20000
        self.current_iter = 1
        self.residual = self.compute_residual()

    def compute_residual(self):
        return self.b - self.A.dot(self.x)

    def must_continue(self):
        if self.current_iter >= self.max_iter:
            print("[WARNING] max number of iterations reached: solver failed to achieve convergence!")
            return False
        elif norm(self.residual) / norm(self.b) < self.tol:
            return False
        else:
            return True

    def solve(self):
        while self.must_continue():
            self.x = self.update()
            self.residual = self.compute_residual()
            self.current_iter += 1
        return self.x, self.current_iter

    def update(self):
        raise NotImplementedError("This method has not been implemented yet")
