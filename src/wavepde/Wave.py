from typing import Callable

import numpy as np


class Wave1D:
    """
    1D wave object.
    """

    def __init__(
        self,
        f: Callable,
        g: Callable,
        a: float,
        dx: float,
        c: float,
        dt: float,
        bndry: list = [0, 0],
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
        self.f = f
        self.g = g
        self.a = a
        self.dx = dx
        self.c = c
        if dt > dx / (c * 2**0.5):
            raise ValueError("Time step must be smaller than h/(c*sqrt(2))")
        self.dt = dt
        self.bndry = bndry
        self.init_cond()

    def init_cond(self):
        """
        Initialize the wave.
        x = meshgrid of the domain.
        u0 = initial condition.
        u = wave at time t.
        """
        self.x = np.arange(-self.a-self.dx, self.a + 2*self.dx, self.dx)
        self.u0 = self.f(self.x)
        self.u = self.u0 + self.dt * self.g(self.x)
        self.bndry_cond(self.bndry)

    def bndry_cond(self, bndry: list):
        """
        Apply boundary conditions.
        """
        # Free boundary conditions
        self.u[0] = self.u[2]
        self.u[-1] = self.u[-3]
        return
        # Fixed boundary conditions
        self.u[0] = bndry[0]
        self.u[-1] = bndry[1]

    def laplacian(self):
        """
        Compute the Laplacian of the wave:
        Laplacian(u) = u_xx
        using the 3-point stencil:
        u_xx = (u_{i+1} + u_{i-1} - 2u_{i})/dx^2
        """
        return (np.roll(self.u, 1) + np.roll(self.u, -1) - 2 * self.u) / self.dx**2

    def update(self):
        """
        Update the wave:
        u_tt = c^2 * (u_xx + u_yy)
        using the finite difference method:
        u(x, y, t + dt) = 2u(x, y, t) - u(x, y, t - dt) + c^2 * dt^2 * (u_xx + u_yy)
        """
        self.u0, self.u = (
            self.u,
            2 * self.u - self.u0 + self.c**2 * self.dt**2 * self.laplacian(),
        )
        self.bndry_cond(self.bndry)


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
        self.f = f
        self.g = g
        self.a = a
        self.h = h
        self.c = c
        if dt > h / (c * 2**0.5):
            raise ValueError("Time step must be smaller than h/(c*sqrt(2))")
        self.dt = dt
        self.init_cond()

    def init_cond(self):
        """
        Initialize the wave.
        X, Y = meshgrid of the domain.
        u0 = initial condition.
        u = wave at time t.
        """
        self.x, self.y = np.meshgrid(
            np.arange(-self.a, self.a + self.h, self.h),
            np.arange(-self.a, self.a + self.h, self.h),
        )
        self.u0 = self.f(self.x, self.y)
        self.u = self.u0 + self.dt * self.g(self.x, self.y)

    def laplacian(self):
        """
        Compute the Laplacian of the wave:
        Laplacian(u) = u_xx + u_yy
        using the 5-point stencil:
        u_xx = (u_{i+1, j} + u_{i-1, j} + u_{i, j+1} + u_{i, j-1} - 4u_{i, j})/h^2
        """
        return (
            np.roll(self.u, 1, axis=0)
            + np.roll(self.u, -1, axis=0)
            + np.roll(self.u, 1, axis=1)
            + np.roll(self.u, -1, axis=1)
            - 4 * self.u
        ) / self.h**2

    def update(self):
        """
        Update the wave:
        u_tt = c^2 * (u_xx + u_yy)
        using the finite difference method:
        u(x, y, t + dt) = 2u(x, y, t) - u(x, y, t - dt) + c^2 * dt^2 * (u_xx + u_yy)
        """
        self.u0, self.u = (
            self.u,
            2 * self.u - self.u0 + self.c**2 * self.dt**2 * self.laplacian(),
        )
