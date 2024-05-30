import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize


class Wave2DAnim:
    def __init__(self, wave, frames=480, interval=1):
        self._wave = wave
        self._frames = frames
        self._interval = interval

        self._x, self._y, self._u = self._wave.get_wave()
        _, _, self._a, _, _, self._dt = self._wave.get_params()
        self._xmin, self._xmax = -self._a, self._a
        self._ymin, self._ymax = -self._a, self._a
        self._umin, self._umax = self._u.min(), self._u.max()

        self._fig = plt.figure()
        self._ax = self._fig.add_subplot(111, projection="3d")
        self._ax.set_xlim(self._xmin, self._xmax)
        self._ax.set_ylim(self._ymin, self._ymax)
        self._ax.set_zlim(self._umin, self._umax)

        self._norm = Normalize(vmin=self._umin, vmax=self._umax)
        self._colormap = cm.viridis
        self._surf = self._ax.plot_surface(
            self._x, self._y, self._u, cmap=self._colormap, norm=self._norm
        )
        self._fig.colorbar(
            cm.ScalarMappable(norm=self._norm, cmap=self._colormap),
            ax=self._ax,
            shrink=0.5,
            aspect=5,
        )

    def update(self, i):
        self._wave.update()
        _, _, self._u = self._wave.get_wave()
        self._ax.clear()
        self._ax.set_xlim(self._xmin, self._xmax)
        self._ax.set_ylim(self._ymin, self._ymax)
        self._ax.set_zlim(self._umin, self._umax)
        self._surf = self._ax.plot_surface(
            self._x, self._y, self._u, cmap=self._colormap, norm=self._norm
        )
        self._ax.set_title("Wave Equation Free-Boundary", fontsize=16)
        self._ax.text2D(
            0.05, 0.95, f"Time: {i*self._dt:.2f}", transform=self._ax.transAxes
        )

    def animate(self):
        anim = FuncAnimation(
            self._fig, self.update, frames=self._frames, interval=self._interval
        )
        plt.show()
        # To save the animation, uncomment the following line:
        # anim.save('wave_animation.mp4', fps=15, extra_args=['-vcodec', 'libx264'])
