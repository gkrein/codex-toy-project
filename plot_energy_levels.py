from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.oscillator import harmonic_oscillator_energy


def main():
    levels = list(range(6))
    energies = [harmonic_oscillator_energy(n) for n in levels]

    plt.plot(levels, energies, marker="o")
    plt.xlabel("n")
    plt.ylabel("E_n")
    plt.title("Harmonic oscillator energy levels")

    output_path = Path("figures") / "energy_levels.png"
    output_path.parent.mkdir(exist_ok=True)
    plt.savefig(output_path)


if __name__ == "__main__":
    main()
