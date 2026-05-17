# Task 007: Add spherical infinite well energy levels

## Goal

Add a second quantum mechanics model: a particle in a three-dimensional spherical infinite well.

The potential is

```text
V(r) = 0       for r < R
V(r) = infinity for r >= R
```

The radial wave function involves spherical Bessel functions:

```text
j_l(k r)
```

The boundary condition at the wall is

```text
j_l(k R) = 0
```

Therefore the allowed momenta are determined by the zeros of the spherical Bessel function:

```text
k_{l,n} = alpha_{l,n} / R
```

where `alpha_{l,n}` is the `n`-th positive root of

```text
j_l(alpha) = 0
```

The energy levels are

```text
E_{l,n} = hbar^2 alpha_{l,n}^2 / (2 m R^2)
```

Use default values:

```text
hbar = 1.0
mass = 1.0
radius = 1.0
```

## Requirements

1. Create a new file:

```text
src/spherical_well.py
```

2. In that file, define a function:

```python
def spherical_bessel_zero(l, n):
    ...
```

where:

- `l` is the angular momentum quantum number,
- `n` is the root index, starting from `n = 1`,
- the function returns the `n`-th positive zero of the spherical Bessel function `j_l(x)`.

3. Use SciPy for the numerical computation:

```python
from scipy.special import spherical_jn
from scipy.optimize import brentq
```

4. Also define:

```python
def spherical_well_energy(l, n, hbar=1.0, mass=1.0, radius=1.0):
    ...
```

which returns:

```text
E_{l,n} = hbar^2 alpha_{l,n}^2 / (2 mass radius^2)
```

5. Add `scipy` to:

```text
requirements.txt
```

6. Add a new test file:

```text
tests/test_spherical_well.py
```

7. Add tests checking known roots for low angular momentum.

Use the following reference values:

```text
j_0 first root = pi
j_0 second root = 2 pi
j_1 first root approximately 4.493409
```

The tests should verify approximately that:

```text
spherical_bessel_zero(0, 1) ≈ pi
spherical_bessel_zero(0, 2) ≈ 2 pi
spherical_bessel_zero(1, 1) ≈ 4.493409
```

8. Add tests for the energy function using the default values.

For example, for `l = 0`, `n = 1`, with `hbar = mass = radius = 1`,

```text
E_{0,1} = pi^2 / 2
```

9. Use `pytest.approx` for floating-point comparisons.

10. Do not modify the existing harmonic oscillator code unless necessary.

11. After editing, run:

```powershell
python -m pytest
```

12. Create a summary file named:

```text
tasks/task_007_summary.md
```

The summary should include:

- what changed,
- what command was run,
- the output of the command,
- whether the tests passed,
- any unresolved issues.

## Important instructions for Codex

- Read `AGENTS.md` before making changes.
- Explain the plan before editing.
- Modify only the files needed for this task.
- Do not commit anything.
- Show the diff before stopping.