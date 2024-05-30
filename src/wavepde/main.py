import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize

from wavepde.Wave import Wave

# Parameters
a = 1
h = 2 * a / 50
c = 1
dt = h / (c * 5)

# Initial condition
f = lambda x, y: np.exp(-10 * (x**2 + y**2))
g = lambda x, y: np.zeros_like(x)


def main():
    w = Wave(f, g, a, h, c, dt)
    x, y, u = w.get()
    umin, umax = u.min(), u.max()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(-a, a)
    ax.set_ylim(-a, a)
    ax.set_zlim(umin, umax)

    u = w.get_wave()
    norm = Normalize(vmin=umin, vmax=umax)
    colormap = cm.viridis

    surf = ax.plot_surface(x, y, u, cmap=colormap, norm=norm)
    fig.colorbar(
        cm.ScalarMappable(norm=norm, cmap=colormap), ax=ax, shrink=0.5, aspect=5
    )

    def update(i):
        w.update()
        u = w.get_wave()
        ax.clear()
        ax.set_xlim(-a, a)
        ax.set_ylim(-a, a)
        ax.set_zlim(umin, umax)
        surf = ax.plot_surface(x, y, u, cmap=colormap, norm=norm)
        ax.set_title("Wave Equation Free-Boundary", fontsize=16)
        ax.text2D(0.05, 0.95, f"Time: {i*dt:.2f}", transform=ax.transAxes)

    anim = FuncAnimation(fig, update, frames=480, interval=1)

    # # Save the animation as a video file
    # anim.save('wave_animation.mp4', fps=15, extra_args=['-vcodec', 'libx264'])

    plt.show()


if __name__ == "__main__":
    main()
