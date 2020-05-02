from numpy import zeros, triu, random, ones
from numpy.linalg import cond, norm


class ForwardSubstitutionSolver:

    def __init__(self, A, b):
        self.A = A
        self.b = b

    def solve(self):
        n = self.A.shape[0]
        x = zeros(n)
        x[0] = self.b[0] / self.A[0, 0]
        for i in range(1, n):
            x[i] = (self.b[i] - self.A[i,].dot(x)) / self.A[i, i]
        return x


if __name__ == '__main__':
    A = random.triangular((100, 100))
    A = triu(A)
    print(cond(A))
    x = ones(A.shape[0])
    b = A.dot(x)
    xapp = ForwardSubstitutionSolver(A, b).solve()
    print(norm(xapp - x) / norm(x))

