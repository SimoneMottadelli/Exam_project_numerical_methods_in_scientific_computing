import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

tol = [1e-4, 1e-6, 1e-8, 1e-10]

jacobi = np.array([2.30052471160888671875000000000000e-02, 3.49953174591064453125000000000000e-02, 4.99708652496337890625000000000000e-02, 6.29630088806152343750000000000000e-02])
gauss = np.array([7.29575157165527343750000000000000e-02, 1.19930267333984375000000000000000e-01, 1.70901536941528320312500000000000e-01, 2.19877004623413085937500000000000e-01])
gradient = np.array([5.19719123840332031250000000000000e-02, 1.27628302574157714843750000000000e+00, 2.88532352447509765625000000000000e+00, 4.64434123039245605468750000000000e+00])
conj_grad = np.array([3.50005626678466796875000000000000e-02, 9.39638614654541015625000000000000e-02, 1.29941940307617187500000000000000e-01, 1.38918876647949218750000000000000e-01])

plt.title("Comparison execution time/tolerance")
plt.semilogy(tol, jacobi, label="Jacobi")
plt.scatter(tol, jacobi, s=5)
plt.semilogy(tol, gauss, label="Gauss-Seidel")
plt.scatter(tol, gauss, s=5)
plt.semilogy(tol, gradient, label="Gradient")
plt.scatter(tol, gradient, s=5)
plt.semilogy(tol, conj_grad, label="Conjugate Gradient")
plt.scatter(tol, conj_grad, s=5)
plt.gca().invert_xaxis()
plt.xlabel("Tolerance")
plt.ylabel("Time in seconds (semi-logarithmic scale)")
plt.xticks([1e-4, 1e-10], rotation='vertical')
plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.e'))
plt.legend()
plt.show()