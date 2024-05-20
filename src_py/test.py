import os
import sys
import solver
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, "../bindings")
sys.path.append(target_dir)

def norm (matrix):
        return np.sum(matrix * np.conjugate(matrix)).real

def normalize (matrix):
        return matrix / np.sqrt(norm(matrix))


psi =   np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.0, 0.1, 0.2], [0.3, 0.4, 0.5, 0.6]], dtype=np.complex128, order='F') \
    +1j*np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.0, 0.1, 0.2], [0.3, 0.4, 0.5, 0.6]], dtype=np.complex128, order='F') \

V = np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.0, 0.1, 0.2], [0.3, 0.4, 0.5, 0.6]], dtype=np.complex128, order='F')

dx = 0.1
dy = 0.1
dt = 0.000025
m = 1.0

sol = solver.Solver(normalize(psi), V, dx, dy, dt, m)

tmax = 10
for i in range (int(tmax/dt)):
        if (i%100000 == 0):
                print("\nPsi n°",i,"avec FTCS: ")
                print(sol.psi)
                print("De norme: ")
                print(norm(sol.psi))

        sol.generateNextStep_FTCS()


dt = 0.0005
sol = solver.Solver(normalize(psi), V, dx, dy, dt, m)

tmax = 10
for i in range (int(tmax/dt)):
        if (i%10000 == 0):
                print("\nPsi n°",i," avec BTCS: ")
                print(sol.psi)
                print("De norme: ")
                print(norm(sol.psi))
        sol.generateNextStep_BTCS()

dt = 0.005
sol = solver.Solver(normalize(psi), V, dx, dy, dt, m)

tmax = 100
for i in range (int(tmax/dt)):
        if (i%1000 == 0):
                print("\nPsi n°",i,"avec CTCS: ")
                print(sol.psi)
                print("De norme: ")
                print(norm(sol.psi))
        sol.generateNextStep_CTCS()
























