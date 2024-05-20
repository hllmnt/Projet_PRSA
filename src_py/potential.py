import numpy as np
from PIL import Image

def from_img(path, min, max):
    img = np.asarray(Image.open(path).convert('L'), dtype=np.float64)
    v = img*(max-min)/255 + min
    return v

def from_formula(x, y, k, nx, ny):
    x = np.tile(x, (len(y), 1)).T
    y = np.tile(y, (len(x[0]), 1))
    return k*(np.power(x, nx)+np.power(y, ny))
