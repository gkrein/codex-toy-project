from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.spherical_well import spherical_well_energy


def main():
    radii = [0.5 + index * 0.05 for index in range(51)]
    levels = [(0, 1), (0, 2), (1, 1), (1, 2)]

    for l, n in levels:
        energies = [
            spherical_well_energy(l, n, hbar=1.0, mass=1.0, radius=radius)
            for radius in radii
        ]
        plt.plot(radii, energies, label=f"(l={l}, n={n})")

    plt.xlabel("R")
    plt.ylabel("E_{l,n}(R)")
    plt.title("Spherical infinite well energy levels")
    plt.legend()

    output_path = Path("figures") / "spherical_well_radius_dependence.png"
    output_path.parent.mkdir(exist_ok=True)
    plt.savefig(output_path)


if __name__ == "__main__":
    main()
