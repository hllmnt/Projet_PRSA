import numpy as np
import math
from scipy import special

# Function to calculate the solution to the harmonic oscillator
# @param n: int - the order of the harmonic oscillator
# @param x: numpy array - the values at which to evaluate the harmonic oscillator
# @param h: numpy array - the hermite polynomials evaluated at the given x
# @return: numpy array - the values of the harmonic oscillator at the given x
def solution1D(n, x, h, m=1, w=1, hbar=1):
    # Calculate the harmonic oscillator
    x = math.pow(m*w/(hbar*math.pi), 0.25) * np.exp(-m*w*x*x/(2*hbar), dtype=np.complex128, order='F').reshape(1, len(x))
    psi = x * h / math.sqrt(math.pow(2, n) * math.factorial(n))
    return psi

# Function to calculate the solution to the harmonic oscillator in 2D
# @param nx: int - the order of the harmonic oscillator in the x direction
# @param ny: int - the order of the harmonic oscillator in the y direction
# @param x: numpy array - the values at which to evaluate the harmonic oscillator in the x direction
# @param y: numpy array - the values at which to evaluate the harmonic oscillator in the y direction
# @param hx: numpy array - the hermite polynomials evaluated at the given x
# @param hy: numpy array - the hermite polynomials evaluated at the given y
# @return: numpy array - the values of the harmonic oscillator at the given x and y
def solution2D(nx, ny, x, y, hx, hy, m=1, w=1, hbar=1):
    psix = np.transpose(solution1D(nx, x, hx, m, w, hbar))
    psiy = solution1D(ny, y, hy, m, w, hbar)
    return psix @ psiy

# Function to calculate the solution to the harmonic oscillator as a linear combination of different orders
# @param deg_array_x: numpy array - the orders of the harmonic oscillator in the x direction
# @param deg_array_y: numpy array - the orders of the harmonic oscillator in the y direction
# @param proportion_array: numpy array - the proportions of each order
# @param x: numpy array - the values at which to evaluate the harmonic oscillator in the x direction
# @param y: numpy array - the values at which to evaluate the harmonic oscillator in the y direction
# @return: numpy array - the values of the harmonic oscillator at the given x and y
def solutionMix(deg_array_x, deg_array_y, proportion_array, x, y, m=1, w=1, hbar=1):
    psi = np.zeros((x.size, y.size), dtype=np.complex128, order='F')
    for i in range(deg_array_x.size):
        hx = special.hermite(deg_array_x[i])(x)
        hy = special.hermite(deg_array_y[i])(y)
        psi += proportion_array[i] * solution2D(deg_array_x[i], deg_array_y[i], x, y, hx, hy, m, w, hbar)
    return psi/np.sqrt(np.sum(proportion_array*proportion_array))

# Function to calculate a gaussian packet
# @param x: numpy array - the values at which to evaluate the gaussian packet in the x direction
# @param x0: float - the center of the gaussian packet in the x direction
# @param y: numpy array - the values at which to evaluate the gaussian packet in the y direction
# @param y0: float - the center of the gaussian packet in the y direction
# @param kx: float - the wave number in the x direction
# @param ky: float - the wave number in the y direction
# @param w: float - the width of the gaussian packet
# @return: numpy array - the values of the gaussian packet at the given x and y
def gaussian_packet(x, x0, y, y0, kx, ky, w=1):
    resx = np.transpose(np.exp(-((x-x0)**2)/(w**2), dtype=np.complex128, order='F') * np.exp(1j*(kx*x), dtype=np.complex128, order='F').reshape(1, len(x)))
    resy = np.exp(-((y-y0)**2)/(w**2), dtype=np.complex128, order='F') * np.exp(1j*(ky*y), dtype=np.complex128, order='F').reshape(1, len(y))
    res = resx @ resy
    return np.sqrt(2) * res / (w * np.sqrt(np.pi))

