# Task 002: Refactor harmonic oscillator energy into a function

## Goal

Refactor the harmonic oscillator energy calculation into a reusable Python function.

Create a new file:

```text
src/oscillator.py
```

Inside it, define a function:

```python
def harmonic_oscillator_energy(n, hbar=1.0, omega=1.0):
    ...
```

The function should return

```text
E_n = hbar * omega * (n + 1/2)
```

Then modify `hello.py` so that it imports and uses this function.

The output of

```powershell
python hello.py
```

should remain:

```text
Hello from Codex toy project!
n = 0, E_n = 0.5
n = 1, E_n = 1.5
n = 2, E_n = 2.5
n = 3, E_n = 3.5
n = 4, E_n = 4.5
```

## Requirements

1. Create `src/oscillator.py`.
2. Keep `hello.py` simple.
3. Do not use external packages.
4. Preserve the current output.
5. After editing, run:

```powershell
python hello.py
```

6. Create a summary file named:

```text
tasks/task_002_summary.md
```

The summary should include:

- what changed,
- what command was run,
- the output of the command,
- whether the task passed,
- any unresolved issues.

## Important instructions for Codex

- Read `AGENTS.md` before making changes.
- Explain the plan before editing.
- Modify only the files needed for this task.
- Do not commit anything.
- Show the diff before stopping.