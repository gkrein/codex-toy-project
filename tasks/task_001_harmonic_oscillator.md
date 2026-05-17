# Task 001: Harmonic oscillator energy levels

## Goal

Modify `hello.py` so that it still prints:

```text
Hello from Codex toy project!
```

and then also prints the first five energy levels of a one-dimensional quantum harmonic oscillator.

The energy levels are given by

```text
E_n = hbar * omega * (n + 1/2)
```

Use the values

```text
hbar = 1
omega = 1
n = 0, 1, 2, 3, 4
```

So the expected output should be approximately:

```text
Hello from Codex toy project!
n = 0, E_n = 0.5
n = 1, E_n = 1.5
n = 2, E_n = 2.5
n = 3, E_n = 3.5
n = 4, E_n = 4.5
```

## Requirements

1. Keep the code simple and readable.
2. Do not use external packages.
3. Preserve the original greeting message.
4. After editing `hello.py`, run:

```powershell
python hello.py
```

5. Create a summary file named:

```text
tasks/task_001_summary.md
```

The summary file should include:

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