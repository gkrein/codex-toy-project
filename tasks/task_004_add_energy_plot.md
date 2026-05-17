# Task 004: Plot harmonic oscillator energy levels

## Goal

Create a simple plot of the first six energy levels of the one-dimensional quantum harmonic oscillator.

Use the function

```python
harmonic_oscillator_energy(n, hbar=1.0, omega=1.0)
```

from:

```text
src/oscillator.py
```

Plot the values for:

```text
n = 0, 1, 2, 3, 4, 5
```

with:

```text
hbar = 1
omega = 1
```

## Requirements

1. Create a new folder if it does not already exist:

```text
figures/
```

2. Create a new script:

```text
plot_energy_levels.py
```

3. The script should generate a plot and save it as:

```text
figures/energy_levels.png
```

4. Use `matplotlib`.

5. The plot should have:
   - horizontal axis labeled `n`,
   - vertical axis labeled `E_n`,
   - title `Harmonic oscillator energy levels`.

6. After editing, run:

```powershell
python plot_energy_levels.py
```

7. If `matplotlib` is not installed, report that clearly in the summary file. Do not install packages unless asked.

8. Create a summary file named:

```text
tasks/task_004_summary.md
```

The summary should include:

- what changed,
- what command was run,
- the output of the command,
- whether the plot was created,
- any unresolved issues.

## Important instructions for Codex

- Read `AGENTS.md` before making changes.
- Explain the plan before editing.
- Modify only the files needed for this task.
- Do not commit anything.
- Show the diff before stopping.