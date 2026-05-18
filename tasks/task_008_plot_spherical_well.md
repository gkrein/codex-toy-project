# Task 008: Plot spherical-well eigenvalues as a function of radius

## Goal

Create a plot of several energy eigenvalues of the three-dimensional spherical infinite well as functions of the well radius `R`.

The energy levels are

```text
E_{l,n}(R) = hbar^2 alpha_{l,n}^2 / (2 m R^2)
```

where `alpha_{l,n}` is the `n`-th positive zero of the spherical Bessel function `j_l(x)`.

Use the functions already implemented in:

```text
src/spherical_well.py
```

## Requirements

1. Create a new script at the project root:

```text
plot_spherical_well_radius.py
```

2. The script should plot the energy levels for:

```text
(l, n) = (0, 1)
(l, n) = (0, 2)
(l, n) = (1, 1)
(l, n) = (1, 2)
```

3. Use:

```text
hbar = 1.0
mass = 1.0
```

4. Plot the energy levels as functions of radius over the range:

```text
R = 0.5 to 3.0
```

5. Use `matplotlib`.

6. The plot should have:

```text
horizontal axis: R
vertical axis: E_{l,n}(R)
title: Spherical infinite well energy levels
legend: labels for each (l,n)
```

7. Save the figure as:

```text
figures/spherical_well_radius_dependence.png
```

8. After editing, run:

```powershell
python plot_spherical_well_radius.py
python -m pytest
```

9. Create a summary file named:

```text
tasks/task_008_summary.md
```

The summary should include:

- what changed,
- what commands were run,
- the output of the commands,
- whether the plot was created,
- any unresolved issues.

## Important instructions for Codex

- Read `AGENTS.md` before making changes.
- Explain the plan before editing.
- Modify only the files needed for this task.
- Do not commit anything.
- Show the diff before stopping.