import argparse

import numpy as np

from wavepde.Plot import Wave1DAnim, Wave2DAnim
from wavepde.Wave import Wave1D, Wave2D


def parse_arguments():
    parser = argparse.ArgumentParser(description="2D Wave Equation Animation")
    parser.add_argument("-a", type=float, default=1, help="Length of the domain")
    parser.add_argument(
        "-n", type=int, default=50, help="Number of grid points along each axis"
    )
    parser.add_argument("-c", type=float, default=1, help="Wave speed")
    parser.add_argument(
        "-t", type=float, default=2**0.5, help="Factor for calculating the time step"
    )
    parser.add_argument(
        "-T", type=float, default=1, help="Final time for the simulation"
    )
    parser.add_argument(
        "-f", type=str, default="np.cos(np.pi*x)", help="Initial condition"
    )
    parser.add_argument(
        "-g", type=str, default="np.zeros_like(x)", help="Initial velocity condition"
    )
    parser.add_argument(
        "--video",
        type=str,
        default="",
        help="Name of the video file. If not provided, the animation will be displayed.",
    )
    parser.add_argument(
        "--bndry",
        type=float,
        nargs=4,
        default=[0, 0, 0, 0],
        help="Boundary conditions [left, right, bottom, top]",
    )
    parser.add_argument(
        "--dim",
        type=int,
        default=2,
        help="Dimension of the wave equation (1 or 2)",
    )
    return parser.parse_args()


def init_wave_sim(args) -> tuple:
    h = 2 * args.a / args.n
    dt = h / (args.c * args.t)
    frames = int(args.T / dt) + 1

    if args.dim == 1:
        initial_condition = lambda x: eval(args.f)
        initial_velocity = lambda x: eval(args.g)
        
        return (
            Wave1D(initial_condition, initial_velocity, args.a, h, args.c, dt, args.bndry),
            frames,
            args.video,
        )
    elif args.dim == 2:
        initial_condition = lambda x, y: eval(args.f)
        initial_velocity = lambda x, y: eval(args.g)

        return (
            Wave2D(initial_condition, initial_velocity, args.a, h, args.c, dt),
            frames,
            args.video,
        )
    else:
        raise ValueError("Dimension must be 1 or 2")


def main():
    try:
        args = parse_arguments()
        wave_simulation, frames, video_filename = init_wave_sim(args)
        if args.dim == 1:
            animation = Wave1DAnim(wave_simulation, frames, video_filename)
        elif args.dim == 2:
            animation = Wave2DAnim(wave_simulation, frames, video_filename)
        else:
            raise ValueError("Dimension must be 1 or 2")
        animation.animate()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
