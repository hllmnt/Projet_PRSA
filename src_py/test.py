import sys
sys.path.append("~/Documents/PRSA/projet/bindings")

import solver
import numpy as np

def norm (matrix):
        return np.sum(matrix * np.conjugate(matrix)).real

def normalize (matrix):
        return matrix / np.sqrt(norm(matrix))
               


psi = np.array([[0.1, 0.2], [0.3, 0.4]], dtype = np.complex128, order = 'F') \
        + 1j * np.array([[0.1, 0.2], [0.3, 0.4]], dtype = np.complex128, order = 'F')

psi = normalize(psi)

V = np.array([[0., 0.], [0., 0.]], dtype = np.complex128, order = 'F')
dx = 0.1
dy = 0.1
dt = 0.01
m = 1.0

sol = solver.Solver(psi, V, dx, dy, dt, m)

for i in range (10):
        print("\nPsi n°",i,": ")
        print(sol.psi)
        print("De norme: ")
        print(norm(sol.psi))
        sol.generateNextStep_FTCS()
























# psi = np.array([[0.1, 0.2, 0.3, 0.4], 
#                 [0.5, 0.6, 0.7, 0.8], 
#                 [0.9, 1.0, 1.1, 1.2], 
#                 [1.3, 1.4, 1.5, 1.6]], 
#                 dtype=np.complex128, order='F') \
#                                                 \
#       + 1j * np.array([[0.1, 0.2, 0.3, 0.4], 
#                        [0.5, 0.6, 0.7, 0.8], 
#                        [0.9, 1.0, 1.1, 1.2], 
#                        [1.3, 1.4, 1.5, 1.6]], 
#                        dtype=np.complex128, order='F')

# V = np.array([[0.1, 0.2, 0.3, 0.4], 
#               [0.5, 0.6, 0.7, 0.8], 
#               [0.9, 1.0, 1.1, 1.2], 
#               [1.3, 1.4, 1.5, 1.6]], 
#               dtype=np.complex128, order='F')