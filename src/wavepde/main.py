import numpy as np

from wavepde.Plot import Wave2DAnim
from wavepde.Wave import Wave2D

def main():
    a = 1
    h = 2 * a / 50
    c = 1
    dt = h / (c * 5)

    f = lambda x, y: np.exp(-10 * (x**2 + y**2))
    g = lambda x, y: np.zeros_like(x)
    
    w = Wave2D(f, g, a, h, c, dt)
    p = Wave2DAnim(w)
    p.animate()

if __name__ == "__main__":
    main()
