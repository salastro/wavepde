import argparse

import numpy as np

from wavepde.plot import Wave1DAnim, Wave2DAnim
from wavepde.wave import Wave1D, Wave2D


def parse_arguments():
    parser = argparse.ArgumentParser(description="2D Wave Equation Animation")
    parser.add_argument(
        "--dim",
        type=int,
        default=2,
        help="Dimension of the wave equation (1 or 2)",
    )
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
        "-f", type=str, default="np.zeros_like(x)", help="Initial condition"
    )
    parser.add_argument(
        "-g", type=str, default="np.zeros_like(x)", help="Initial velocity condition"
    )
    parser.add_argument(
        "--bndry",
        dest="bndry",
        type=str,
        choices=["dirichlet", "neumann"],
        default="neumann",
        help="Boundary condition (only for 2D)",
    )
    parser.add_argument(
        "--source",
        nargs="+",
        type=float,
        default=[0.5, 2],
        help="Amplitude and angular frequency of the source (only for 2D)",
    )
    parser.add_argument(
        "--video",
        type=str,
        default="",
        help="Name of the video file. If not provided, the animation will be displayed.",
    )

    args = parser.parse_args()

    if args.bndry not in ["dirichlet", "neumann"]:
        parser.error("Boundary condition must be 'dirichlet' or 'neumann'")

    if args.source[0] == 0:
        args.source = None
    elif len(args.source) != 2:
        parser.error("Source must have two values: amplitude and angular frequency")

    if args.dim > 2 or args.dim < 1:
        parser.error("Dimension must be 1 or 2")

    return args


def init_wave_sim(args) -> tuple:
    h = 2 * args.a / args.n
    dt = h / (args.c * args.t)
    frames = int(args.T / dt) + 1

    if args.dim == 1:
        initial_condition = lambda x: eval(args.f)
        initial_velocity = lambda x: eval(args.g)

        return (
            Wave1D(initial_condition, initial_velocity, args.a, h, args.c, dt),
            frames,
            args.video,
        )
    elif args.dim == 2:
        initial_condition = lambda x, y: eval(args.f)
        initial_velocity = lambda x, y: eval(args.g)

        return (
            Wave2D(
                initial_condition,
                initial_velocity,
                args.a,
                h,
                args.c,
                dt,
                args.bndry,
                args.source,
            ),
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
