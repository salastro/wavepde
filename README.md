# WavePDE

## Overview

WavePDE is a Python project that simulates and animates the wave equation in one
or two dimensions. Users can customize various parameters, including domain
size, grid resolution, wave speed, boundary conditions, initial conditions, and
more.

## Features

- Supports both 1D and 2D wave equations.
- Customizable domain size and grid resolution.
- Adjustable wave speed and time step.
- Different boundary conditions, Dirichlet and Neumann.
- Custom initial conditions and velocity profiles.
- Option to save the animation as a video file.

## Requirements

- Python 3.12 or higher
- numpy
- matplotlib
- argparse

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/salastro/wavepde.git
    cd wavepde
    ```

2. Install the required packages:
    ```sh
    pip install -e .
    ```

## Usage

Run the script with desired parameters from the command line:

```sh
wavepde.py [OPTIONS]
```

### Options

- `--dim`: Dimension of the wave equation (1 or 2). Default is `2`.
- `-a`: Length of the domain. Default is `1`.
- `-n`: Number of grid points along each axis. Default is `50`.
- `-c`: Wave speed. Default is `1`.
- `-t`: Factor for calculating the time step. Default is `sqrt(2)`.
- `-T`: Final time for the simulation. Default is `1`.
- `-f`: Initial condition as a string expression. Default is
`"np.zeros_like(x)"`.
- `-g`: Initial velocity condition as a string expression. Default is
`"np.zeros_like(x)"`.
- `--bndry`: Boundary condition for 2D simulations (`dirichlet` or `neumann`).
Default is `neumann`.
- `--source`: Amplitude and angular frequency of the source for 2D simulations.
Default is `[0.5, 2]`.
- `--video`: Name of the video file to save the animation. If not provided, the
animation will be displayed instead.

### Example

To run a 2D wave simulation with default settings:

```sh
wavepde --dim 2
```

To run a 1D wave simulation with custom initial conditions and save the
animation as `wave1d.mp4`:

```sh
wavepde --dim 1 -f "np.sin(np.pi * x)" -g "np.zeros_like(x)" --source 0 --video wave1d.mp4
```

## Project Structure

- `src/wavepde/`: Main package directory.
  - `Plot.py`: Contains `Wave1DAnim` and `Wave2DAnim` classes for animating the
  simulations.
  - `Wave.py`: Contains `Wave1D` and `Wave2D` classes for setting up the wave
  equations.
- `main.py`: Main script for running the simulations and animations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an
issue if you have any suggestions or improvements. Remember to follow the
[Contribution](CONTRIBUTING.md) guidelines.

## Issues

If you encounter any problems or have any suggestions, please open an issue
along with a detailed description.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.

---
