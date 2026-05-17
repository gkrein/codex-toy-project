# Task 005: Update README with project instructions

## Goal

Update `README.md` so that it clearly explains the current toy project.

The README should describe that this is a small Codex tutorial project using the one-dimensional quantum harmonic oscillator as an example.

## Requirements

Update `README.md` to include:

1. A short project description.
2. The formula for the energy levels:

```text
E_n = hbar * omega * (n + 1/2)
```

3. Instructions for running the main script:

```powershell
python hello.py
```

4. Instructions for running the tests:

```powershell
python -m pytest
```

5. Instructions for regenerating the plot:

```powershell
python plot_energy_levels.py
```

6. A short explanation of the project structure, including:

```text
src/
tests/
figures/
tasks/
```

7. Mention that the `tasks/` folder stores the task specifications and summaries used to supervise Codex.

## Important instructions for Codex

- Read `AGENTS.md` before making changes.
- Explain the plan before editing.
- Modify only `README.md` and `tasks/task_005_summary.md`.
- After editing, run:

```powershell
python hello.py
python -m pytest
python plot_energy_levels.py
```

- Create a summary file named:

```text
tasks/task_005_summary.md
```

The summary should include:

- what changed,
- what commands were run,
- the output of the commands,
- whether the task passed,
- any unresolved issues.

- Do not commit anything.
- Show the diff before stopping.