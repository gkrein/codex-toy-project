# Codex Toy Project Workflow

This project uses a task-based workflow inspired by supervised research-agent work.

The goal is not only to write code, but to keep every change small, documented, testable, and easy to inspect.

## Basic loop

For each new task, follow this loop:

```text
1. Create a task specification in tasks/
2. Commit the task specification
3. Ask Codex to execute the task
4. Manually inspect the changes
5. Run the relevant checks
6. Commit the result only if everything looks correct
```

## Step 1: Create a task file

Each task should be written as a markdown file inside `tasks/`.

Example:

```text
tasks/task_006_add_workflow.md
```

The task file should include:

- the goal,
- the files Codex is allowed to modify,
- the commands Codex should run,
- the expected output or behavior,
- the required summary file,
- an instruction not to commit anything.

## Step 2: Commit the task specification

Before asking Codex to execute the task, commit the task file.

Example:

```powershell
git add tasks/task_006_add_workflow.md
git commit -m "Add workflow documentation task"
```

This creates a clean checkpoint before Codex changes anything.

## Step 3: Ask Codex to execute the task

In the Codex sidebar, use a prompt like:

```text
Read AGENTS.md and tasks/task_006_add_workflow.md.

Execute the task exactly as specified.

Before editing, briefly explain your plan.

Then:
1. Modify only the necessary files.
2. Run the requested checks.
3. Create the requested summary file.
4. Show me the diff.
5. Do not commit anything.
```

## Step 4: Inspect the changes

After Codex finishes, inspect the repository manually.

Useful commands:

```powershell
git status
git diff
```

For new files, inspect them directly:

```powershell
type path\to\file.md
```

Do not commit until the changes have been reviewed.

## Step 5: Run checks manually

Even if Codex says it ran the checks, run them yourself.

For this project, common checks are:

```powershell
python hello.py
python -m pytest
python plot_energy_levels.py
```

The expected behavior is:

- `hello.py` prints the greeting and harmonic oscillator energy levels,
- `pytest` passes,
- `plot_energy_levels.py` regenerates the plot in `figures/`.

## Step 6: Commit the result

If the changes are correct, commit them.

Example:

```powershell
git add modified_file.py tasks/task_006_summary.md
git commit -m "Describe the completed task"
```

Then confirm the repository is clean:

```powershell
git status
```

The desired result is:

```text
nothing to commit, working tree clean
```

## Important rules

- Codex should not commit changes.
- Codex should not install packages unless explicitly asked.
- Codex should not modify unrelated files.
- Each task should create a summary file.
- Every summary file should record:
  - what changed,
  - what commands were run,
  - the output of the commands,
  - whether the task passed,
  - unresolved issues, if any.
- Git is the safety mechanism: inspect before committing.

## Project-specific files

```text
AGENTS.md
```

Instructions for Codex.

```text
README.md
```

Overview of the project for humans.

```text
WORKFLOW.md
```

Description of the supervised Codex workflow.

```text
tasks/
```

Task specifications and task summaries.

```text
src/
```

Reusable source code.

```text
tests/
```

Automated tests.

```text
figures/
```

Generated figures.