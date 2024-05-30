import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize


class Wave2DAnim:
    def __init__(self, wave, frames=480, interval=1):
        self.wave = wave
        self.frames = frames
        self.interval = interval

        self.x, self.y, self.u = self.wave.get()
        self.xmin, self.xmax = self.x.min(), self.x.max()
        self.ymin, self.ymax = self.y.min(), self.y.max()
        self.umin, self.umax = self.u.min(), self.u.max()

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)
        self.ax.set_zlim(self.umin, self.umax)

        self.norm = Normalize(vmin=self.umin, vmax=self.umax)
        self.colormap = cm.viridis
        self.surf = self.ax.plot_surface(
            self.x, self.y, self.u, cmap=self.colormap, norm=self.norm
        )
        self.fig.colorbar(
            cm.ScalarMappable(norm=self.norm, cmap=self.colormap),
            ax=self.ax,
            shrink=0.5,
            aspect=5,
        )

    def update(self, i):
        self.wave.update()
        self.u = self.wave.get_wave()
        self.ax.clear()
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)
        self.ax.set_zlim(self.umin, self.umax)
        self.surf = self.ax.plot_surface(
            self.x, self.y, self.u, cmap=self.colormap, norm=self.norm
        )
        self.ax.set_title("Wave Equation Free-Boundary", fontsize=16)
        # self.ax.text2D(0.05, 0.95, f"Time: {i*self.dt:.2f}", transform=self.ax.transAxes)

    def animate(self):
        anim = FuncAnimation(
            self.fig, self.update, frames=self.frames, interval=self.interval
        )
        plt.show()
        # To save the animation, uncomment the following line:
        # anim.save('wave_animation.mp4', fps=15, extra_args=['-vcodec', 'libx264'])
