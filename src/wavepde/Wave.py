# Path: Wave.py

from typing import Callable

import numpy as np


class Wave2D:
    """
    2D wave object.
    """

    def __init__(
        self, f: Callable, g: Callable, a: float, h: float, c: float, dt: float
    ):
        """
        Parameters
        ----------
        f : Callable
            Initial condition.
        g : Callable
            Initial velocity.
        L : float
            Length of the domain.
        h : float
            Grid spacing.
        dt : float
            Time step.
        c : float
            Wave speed.
        """
        self._f = f
        self._g = g
        self.a = a
        self._h = h
        self._c = c
        if dt > h / (c * 2**0.5):
            raise ValueError("Time step must be smaller than h/(c*sqrt(2))")
        self._dt = dt
        self._init_cond()

    def _init_cond(self):
        """
        Initialize the wave.
        X, Y = meshgrid of the domain.
        u0 = initial condition.
        u = wave at time t.
        """
        self._x, self._y = np.meshgrid(
            np.arange(-self.a, self.a + self._h, self._h),
            np.arange(-self.a, self.a + self._h, self._h),
        )
        self._u0 = self._f(self._x, self._y)
        self._u = self._u0 + self._dt * self._g(self._x, self._y)

    def _laplacian(self):
        """
        Compute the Laplacian of the wave:
        Laplacian(u) = u_xx + u_yy
        using the 5-point stencil:
        u_xx = (u_{i+1, j} + u_{i-1, j} + u_{i, j+1} + u_{i, j-1} - 4u_{i, j})/h^2
        """
        return (
            np.roll(self._u, 1, axis=0)
            + np.roll(self._u, -1, axis=0)
            + np.roll(self._u, 1, axis=1)
            + np.roll(self._u, -1, axis=1)
            - 4 * self._u
        ) / self._h**2

    def update(self):
        """
        Update the wave:
        u_tt = c^2 * (u_xx + u_yy)
        using the finite difference method:
        u(x, y, t + dt) = 2u(x, y, t) - u(x, y, t - dt) + c^2 * dt^2 * (u_xx + u_yy)
        """
        self._u0, self._u = (
            self._u,
            2 * self._u - self._u0 + self._c**2 * self._dt**2 * self._laplacian(),
        )

    def get_axes(self):
        """
        Get the axis of the domain.
        Returns
        -------
        X : np.ndarray
            X-coordinates of the domain.
        Y : np.ndarray
            Y-coordinates of the domain.
        """
        return self._x, self._y

    def get_wave(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get the current wave.
        Returns
        -------
        u : np.ndarray
            Wave at time t.
        """
        return self._u

    def get(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Get the current wave and the axis of the domain.
        Returns
        -------
        X : np.ndarray
            X-coordinates of the domain.
        Y : np.ndarray
            Y-coordinates of the domain.
        u : np.ndarray
            Wave at time t.
        """
        return self._x, self._y, self._u
