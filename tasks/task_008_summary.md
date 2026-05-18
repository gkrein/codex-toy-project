# Task 008 Summary

## What changed

- Added `plot_spherical_well_radius.py`.
- The script plots spherical infinite well energy levels for `(l, n) = (0, 1)`, `(0, 2)`, `(1, 1)`, and `(1, 2)` over `R = 0.5` to `R = 3.0`.
- Generated `figures/spherical_well_radius_dependence.png`.

## Commands run

```powershell
python plot_spherical_well_radius.py
python -m pytest
```

## Output

### `python plot_spherical_well_radius.py`

```text
```

### `python -m pytest`

```text
============================= test session starts =============================
platform win32 -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: C:\Users\gasta\Documents\codex-toy-project
collected 3 items

tests\test_oscillator.py .                                               [ 33%]
tests\test_spherical_well.py ..                                          [100%]

============================== 3 passed in 0.35s ==============================
```

## Plot created

Yes. The file `figures/spherical_well_radius_dependence.png` was created.

## Unresolved issues

None.
