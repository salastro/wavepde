import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize
from rich.progress import Progress


class WaveAnimBase:
    def __init__(self, wave, frames: int, video: str = ""):
        """
        Base class for wave animation.

        Parameters
        ----------
        wave : Wave1D or Wave2D
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

    def update(self, i: int):
        raise NotImplementedError("Subclasses should implement this method.")

    def animate(self):
        with Progress() as progress:
            task = progress.add_task("Animating...", total=self.frames)

            def update_frame(i):
                self.update(i)
                progress.advance(task)
                return []

            anim = FuncAnimation(
                self.fig,
                update_frame,
                frames=self.frames,
                interval=1,
                repeat=False,
            )

            if self.video:
                anim.save(self.video, fps=60, extra_args=["-vcodec", "libx264"])
            else:
                plt.show()


class Wave1DAnim(WaveAnimBase):
    def __init__(self, wave, frames: int, video: str = ""):
        super().__init__(wave, frames, video)
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


class Wave2DAnim(WaveAnimBase):
    def __init__(self, wave, frames: int, video: str = ""):
        super().__init__(wave, frames, video)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.plot_surface()
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

    def plot_surface(self, i: int = 0):
        self.ax.set_xlim(-self.wave.a, self.wave.x.max())
        self.ax.set_ylim(-self.wave.a, self.wave.y.max())
        self.ax.set_zlim(self.umin, self.umax)
        self.ax.set_title("Wave Equation", fontsize=18)
        self.ax.text2D(
            0.05, 0.95, f"Time: {i * self.wave.dt:.2f}", transform=self.ax.transAxes
        )

    def update(self, i: int):
        self.wave.update()
        self.ax.clear()
        self.plot_surface(i)
        self.surf = self.ax.plot_surface(
            self.wave.x, self.wave.y, self.wave.u, cmap=self.colormap, norm=self.norm
        )


# Example usage:
# wave1d = Wave1D()  # Assuming Wave1D is defined elsewhere
# anim1d = Wave1DAnim(wave1d, frames=100, video='wave1d.mp4')
# anim1d.animate()

# wave2d = Wave2D()  # Assuming Wave2D is defined elsewhere
# anim2d = Wave2DAnim(wave2d, frames=100, video='wave2d.mp4')
# anim2d.animate()
