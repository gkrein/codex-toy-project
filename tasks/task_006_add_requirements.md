# Task 006: Add Python requirements file

## Goal

Add a `requirements.txt` file that lists the external Python packages needed by this project.

The project currently uses:

```text
pytest
matplotlib
```

`pytest` is used to run the tests.

`matplotlib` is used to generate the energy-level plot.

## Requirements

1. Create a new file at the project root:

```text
requirements.txt
```

2. The file should contain:

```text
pytest
matplotlib
```

3. Update `README.md` to include a short section explaining how to install the requirements:

```powershell
python -m pip install -r requirements.txt
```

4. After editing, run:

```powershell
python hello.py
python -m pytest
python plot_energy_levels.py
```

5. Create a summary file named:

```text
tasks/task_006_summary.md
```

The summary should include:

- what changed,
- what commands were run,
- the output of the commands,
- whether the task passed,
- any unresolved issues.

## Important instructions for Codex

- Read `AGENTS.md` before making changes.
- Explain the plan before editing.
- Modify only `requirements.txt`, `README.md`, and `tasks/task_006_summary.md`.
- Do not install packages unless explicitly asked.
- Do not commit anything.
- Show the diff before stopping.