# Codex Toy Project

## Short project description

This is a small Codex tutorial project using the one-dimensional quantum
harmonic oscillator as an example. It prints energy levels, includes a reusable
calculation function, tests the function, and can generate a simple plot.

## Harmonic oscillator formula

The energy levels are calculated with:

```text
E_n = hbar * omega * (n + 1/2)
```

## Install requirements

```powershell
python -m pip install -r requirements.txt
```

## Run the main script

```powershell
python hello.py
```

## Run the tests

```powershell
python -m pytest
```

## Regenerate the plot

```powershell
python plot_energy_levels.py
```

## Project structure

- `src/` contains the harmonic oscillator calculation code.
- `tests/` contains pytest tests for the calculation.
- `figures/` contains generated plot files.
- `tasks/` stores the task specifications and summaries used to supervise Codex.
