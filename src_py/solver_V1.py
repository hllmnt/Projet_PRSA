import sys
sys.path.append("~/Documents/PRSA/projet/bindings")

import solver
import numpy as np

psi = np.array([[0.1, 0.2], [0.3, 0.4]], dtype = np.complex128, order = 'F') \
        + 1j * np.array([[0.1, 0.2], [0.3, 0.4]], dtype = np.complex128, order = 'F')
V = np.array([[0.1, 0.2], [0.3, 0.4]], dtype = np.complex128, order = 'F')
dx = 0.1
dy = 0.1
dt = 0.01
m = 1.0

sol = solver.Solver(psi, V, dx, dy, dt, m)

for i in range 100:
    sol.generateNextStep_FTCS()
    matplotlib(sol.psi)

