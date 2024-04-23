import numpy as np
import math


# Function to calculate the hermite polynomials
# @param n: int - the order of the hermite polynomial
# @param x: numpy array - the values at which to evaluate the hermite polynomial
# @return: numpy array - the values of the hermite polynomial at the given x keeping each order in a different row
def hermite(n, x):
    h = np.zeros((n+1, len(x)))

    h[0] = np.ones((1, len(x)))
    if n == 0:
        return h

    h[1] = 2*x
    
    for i in range(2, n+1):
        h[i] = 2*x*h[i-1] - 2*(i-1)*h[i-2]
    return h

# Function to calculate the solution to the harmonic oscillator
# @param n: int - the order of the harmonic oscillator
# @param x: numpy array - the values at which to evaluate the harmonic oscillator
# @param h: numpy array - the hermite polynomials evaluated at the given x
# @return: numpy array - the values of the harmonic oscillator at the given x
def solution1D(n, x, h, m=1, w=1, hbar=1):
    # Calculate the harmonic oscillator
    x = math.pow(m*w/(hbar*math.pi), 0.25) * np.exp(-m*w*x*x/(2*hbar)).reshape(1, len(x))
    psi = x * h[n] / math.sqrt(math.pow(2, n) * math.factorial(n))
    return psi

def solution2D(nx, ny, x, y, hx, hy, m=1, w=1, hbar=1):
    psix = np.transpose(solution1D(nx, x, hx, m, w, hbar))
    psiy = solution1D(ny, y, hy, m, w, hbar)
    return psix @ psiy

def solutionMix(deg_array_x, deg_array_y, proportion_array, x, y, m=1, w=1, hbar=1):
    psi = np.zeros((len(x), len(y)))
    hx = hermite(np.max(deg_array_x), x)
    hy = hermite(np.max(deg_array_y), y)
    for i in range(len(deg_array_x)):
        psi += proportion_array[i] * solution2D(deg_array_x[i], deg_array_y[i], x, y, hx, hy, m, w, hbar)
    return psi/np.sqrt(np.sum(proportion_array*proportion_array))


def gaussian_packet(x, x0, y, y0, kx, ky, w=1):
    resx = np.transpose(np.exp(-((x-x0)**2)/(w**2)) * np.exp(1j*(kx*x)).reshape(1, len(x)))
    resy = np.exp(-((y-y0)**2)/(w**2)) * np.exp(1j*(ky*y)).reshape(1, len(y))
    res = resx @ resy
    return np.sqrt(2) * res / (w * np.sqrt(np.pi))

