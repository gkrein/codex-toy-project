from src.oscillator import harmonic_oscillator_energy


print("Hello from Codex toy project!")

for n in range(5):
    energy = harmonic_oscillator_energy(n)
    print(f"n = {n}, E_n = {energy}")
