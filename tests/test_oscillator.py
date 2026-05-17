from src.oscillator import harmonic_oscillator_energy


def test_harmonic_oscillator_energy_default_values():
    assert harmonic_oscillator_energy(0) == 0.5
    assert harmonic_oscillator_energy(1) == 1.5
    assert harmonic_oscillator_energy(4) == 4.5
