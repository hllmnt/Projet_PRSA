import numpy as np
from PIL import Image

'''
Functions to generate potential
'''

def from_img(path, min, max):
    img = np.asarray(Image.open(path).convert('L'), dtype=np.complex128, order='F')
    v = img*(max-min)/255 + min
    return v

def from_formula(x, y, k, nx, ny):
    x = np.array(np.tile(x, (len(y), 1)).T, dtype=np.complex128, order='F')
    y = np.array(np.tile(y, (len(x[0]), 1)), dtype=np.complex128, order='F')
    return k*(np.power(x, nx)+np.power(y, ny))
