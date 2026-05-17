# Task 007 Summary

## What changed

- Added `scipy` to `requirements.txt`.
- Added `src/spherical_well.py` with spherical Bessel zero and spherical well energy functions.
- Added `tests/test_spherical_well.py` with tests for known low-angular-momentum roots and the default energy formula.

## Command run

```powershell
python -m pytest
```

## Output

```text
============================= test session starts =============================
platform win32 -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: C:\Users\gasta\Documents\codex-toy-project
collected 3 items

tests\test_oscillator.py .                                               [ 33%]
tests\test_spherical_well.py ..                                          [100%]

============================== 3 passed in 4.88s ==============================
```

## Tests passed

Yes.

## Unresolved issues

None.
