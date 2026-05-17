# Task 003: Add tests for the harmonic oscillator energy function

## Goal

Add simple tests for the function

```python
harmonic_oscillator_energy(n, hbar=1.0, omega=1.0)
```

defined in:

```text
src/oscillator.py
```

The tests should verify that, for `hbar = 1` and `omega = 1`,

```text
E_0 = 0.5
E_1 = 1.5
E_4 = 4.5
```

using the formula

```text
E_n = hbar * omega * (n + 1/2)
```

## Requirements

1. Create a new folder:

```text
tests/
```

2. Create a new test file:

```text
tests/test_oscillator.py
```

3. Use `pytest`.

4. Add tests for:

```text
n = 0
n = 1
n = 4
```

5. After editing, run:

```powershell
python -m pytest
```

6. If `pytest` is not installed, report that clearly in the summary file. Do not install packages unless asked.

7. Create a summary file named:

```text
tasks/task_003_summary.md
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