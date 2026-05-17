import math

import pytest

from src.spherical_well import spherical_bessel_zero, spherical_well_energy


def test_spherical_bessel_zero_known_roots():
    assert spherical_bessel_zero(0, 1) == pytest.approx(math.pi)
    assert spherical_bessel_zero(0, 2) == pytest.approx(2 * math.pi)
    assert spherical_bessel_zero(1, 1) == pytest.approx(4.493409, rel=1e-6)


def test_spherical_well_energy_default_values():
    assert spherical_well_energy(0, 1) == pytest.approx(math.pi**2 / 2)
