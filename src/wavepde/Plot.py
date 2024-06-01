import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize


class Wave1DAnim:
    def __init__(self, wave, frames: int, video: str = ""):
        """
        Parameters
        ----------
        wave : Wave1D
            Wave object.
        frames : int
            Number of frames for the animation.
        video : str
            Filename to save the animation as a video. If empty, the animation will be shown.
        """
        self.wave = wave
        self.frames = frames
        self.video = video

        self.umin, self.umax = self.wave.u.min(), self.wave.u.max()

        self.fig, self.ax = plt.subplots()
        (self.line,) = self.ax.plot(self.wave.x, self.wave.u)

        self.ax.set_xlim(-self.wave.a, self.wave.a)
        self.ax.set_ylim(-self.umax, self.umax)
        self.ax.set_title("Wave Equation", fontsize=18)
        self.time_text = self.ax.text(0.05, 0.95, "", transform=self.ax.transAxes)

    def update(self, i: int):
        self.wave.update()
        self.line.set_ydata(self.wave.u)
        self.time_text.set_text(f"Time: {i * self.wave.dt:.2f}")
        return self.line, self.time_text

    def animate(self):
        anim = FuncAnimation(
            self.fig,
            self.update,
            frames=self.frames,
            interval=1,
            repeat=False,
            blit=True,
        )

        if self.video:
            anim.save(self.video, fps=60, extra_args=["-vcodec", "libx264"])
        else:
            plt.show()


class Wave2DAnim:
    def __init__(self, wave, frames: int, video: str = ""):
        """
        Parameters
        ----------
        wave : Wave2D
            Wave object.
        frames : int
            Number of frames for the animation.
        interval : int
            Delay between frames in milliseconds.
        is_video : bool
            If True, save the animation as a video.
        """
        self.wave = wave
        self.frames = frames
        self.video = video

        self.umin, self.umax = self.wave.u.min(), self.wave.u.max()

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlim(-self.wave.a, self.wave.a)
        self.ax.set_ylim(-self.wave.a, self.wave.a)
        self.ax.set_zlim(self.umin, self.umax)
        self.ax.set_title("Wave Equation Free-Boundary", fontsize=16)
        self.ax.text2D(
            0.05, 0.95, f"Time: {0:.2f}", transform=self.ax.transAxes
        )

        self.norm = Normalize(vmin=self.umin, vmax=self.umax)
        self.colormap = cm.viridis
        self.surf = self.ax.plot_surface(
            self.wave.x, self.wave.y, self.wave.u, cmap=self.colormap, norm=self.norm
        )
        self.fig.colorbar(
            cm.ScalarMappable(norm=self.norm, cmap=self.colormap),
            ax=self.ax,
            shrink=0.5,
            aspect=5,
        )

    def update(self, i: int):
        self.wave.update()
        self.u = self.wave.u
        self.ax.clear()
        self.ax.set_xlim(-self.wave.a, self.wave.a)
        self.ax.set_ylim(-self.wave.a, self.wave.a)
        self.ax.set_zlim(self.umin, self.umax)
        self.surf = self.ax.plot_surface(
            self.wave.x, self.wave.y, self.wave.u, cmap=self.colormap, norm=self.norm
        )
        self.ax.set_title("Wave Equation Free-Boundary", fontsize=16)
        self.ax.text2D(
            0.05, 0.95, f"Time: {i * self.wave.dt:.2f}", transform=self.ax.transAxes
        )

    def animate(self):
        anim = FuncAnimation(
            self.fig,
            self.update,
            frames=self.frames,
            interval=1,
            repeat=False,
        )
        
        if self.video:
            anim.save(self.video, fps=60, extra_args=['-vcodec', 'libx264'])
            return

        plt.show()
