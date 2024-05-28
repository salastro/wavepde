"""FDM solver for the wave equation."""

import numpy as np


def laplacian(u: np.ndarray, h: float) -> np.ndarray:
    """
    Compute the Laplacian of u using FDM.
    Args:
    u: 2D numpy array of the function u(x, y).
    h: float, grid spacing.
    Returns:
    2D numpy array, Laplacian of u.
    """
    return (
        np.roll(u, 1, axis=0)
        + np.roll(u, -1, axis=0)
        + np.roll(u, 1, axis=1)
        + np.roll(u, -1, axis=1)
        - 4 * u
    ) / h**2
