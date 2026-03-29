# Codeforces I/O Python Boilerplate Usage Guide
Competitive programming platforms like Codeforces rely on strict and often cumbersome standard input/output handling, which can slow down development and introduce avoidable friction—especially when repeatedly writing parsing logic, formatting outputs, or debugging intermediate states. This boilerplate was designed to abstract away those low-level concerns and provide a consistent, efficient, and developer-friendly interface for I/O operations. By standardizing input parsing, buffering output, and enabling safe debugging through stderr, it allows you to focus entirely on problem-solving logic rather than boilerplate mechanics.

This markdown explains how to correctly use the provided Python boilerplate for competitive programming (especially Codeforces), along with proper configuration of the **CPH (Competitive Programming Helper)** VSCode extension.

---
## Table of Contents

  - [1. Overview of the Boilerplate](#1-overview-of-the-boilerplate)
  - [2. Input Handling](#2-input-handling)
    - [For lists:](#for-lists)
    - [Default behavior:](#default-behavior)
    - [Custom parsing:](#custom-parsing)
  - [3. Output Handling](#3-output-handling)
    - [Internally:](#internally)
    - [Additional behavior:](#additional-behavior)
    - [`sep` and `end` arguments:](#sep-and-end-arguments)
  - [4. Debugging (Local Only)](#4-debugging-local-only)
    - [Purpose of `debprint`:](#purpose-of-debprint)
    - [Behavior:](#behavior)
    - [`sep` and `end` in `debprint`:](#sep-and-end-in-debprint)
    - [Typical use cases:](#typical-use-cases)
  - [5. Local Mode (`--islocal`)](#5-local-mode---islocal)
  - [6. Important Notes](#6-important-notes)
  - [7. VSCode CPH Extension Setup](#7-vscode-cph-extension-setup)
    - [Step 1: Set Default Language to Python](#step-1-set-default-language-to-python)
    - [Step 2: Place Boilerplate File](#step-2-place-boilerplate-file)
    - [Step 3: Set Template Path](#step-3-set-template-path)
    - [Step 4: Ignore STDERR](#step-4-ignore-stderr)
    - [Step 5: Add `--islocal` Argument](#step-5-add---islocal-argument)
  - [8. Workflow Summary](#8-workflow-summary)
    - [When solving locally:](#when-solving-locally)
    - [When submitting to Codeforces:](#when-submitting-to-codeforces)
  - [9. Example Usage](#9-example-usage)
  - [10. Advantages of This Setup](#10-advantages-of-this-setup)


---

## 1. Overview of the Boilerplate

This boilerplate abstracts standard input/output and adds:

* Fast I/O (`sys.stdin.readline`)
* Buffered output (avoids repeated `print()` overhead)
* Debug printing (`debprint`) to `stderr`
* Local testing flag (`--islocal`)
* Safe parsing utilities

You should write all your logic **only between**:

```python
#--START--your code begins here

# your solution

#--STOP--your code ends here
```

---

## 2. Input Handling

You can pass any type as an argument to `input()`:

* `input(int)` → converts full line to `int`
* `input(str)` → returns string (default behavior)
* `input(<type>)` → casts the input into the given type (if valid)

### For lists:

* `input([])` → returns list of strings
* `input([int])` → returns list of integers
* `input([<type>])` → returns list casted to that type

### Default behavior:

* `input()` without arguments returns a string

### Custom parsing:

If you need a custom parsing format (e.g., mixed formats, special delimiters):

```python
raw = input()
```

Then process it manually.

* Returns `None` safely if input ends or parsing fails.

---

## 3. Output Handling

Use the provided `print()` (overridden):

```python
print(ans)
print(a, b, c)
```

### Internally:

* Outputs are buffered in `output_buffer`
* Actually flushed only at program exit

### Additional behavior:

If you print a list or tuple, it is automatically formatted:

```python
print([1, 2, 3, 4])
```

Output:

```
1 2 3 4
```

* You do **not** need to manually format lists for competitive programming output.

### `sep` and `end` arguments:

The overridden `print()` fully supports the standard `sep` and `end` parameters:

```python
print(1, 2, 3, sep='-')
print(1, 2, end='')
```

Behavior:

* `sep` defines how multiple arguments are joined
* `end` defines what is appended at the end of the output

Example:

```python
print(1, 2, 3, sep='-')
```

Output:

```
1-2-3
```

Internally, even lists/tuples respect `sep`:

```python
print([1, 2, 3], sep='-')
```

Output:

```
1-2-3
```

---

## 4. Debugging (Local Only)

Use:

```python
debprint("value:", x)
```

### Purpose of `debprint`:

* Designed specifically for debugging without affecting final output
* Prints to `stderr` instead of `stdout`
* Lets you inspect variables, arrays, intermediate states, etc.
* Keeps your actual output clean for judges like Codeforces

### Behavior:

* Only works if `--islocal` flag is passed
* Completely ignored on Codeforces (safe)
* No need to remove debug debprint statements before submission

### `sep` and `end` in `debprint`:

`debprint()` also supports `sep` and `end`:

```python
debprint(1, 2, 3, sep=' | ', end='\n---\n')
```

This allows flexible formatting of debug output

### Typical use cases:

* Checking array contents
* Verifying loop iterations
* Debugging edge cases
* Tracking logic flow during development


---

## 5. Local Mode (`--islocal`)

When running locally:

```bash
python solution.py --islocal
```

This enables:

* Debug logs
* Execution timestamp
* Program name logging

On Codeforces, this flag is not used, so no extra output is produced.

---

## 6. Important Notes

* Never use built-in `input()` or `print()`
* Always use the overridden versions
* Do not manually flush output
* DO NOT REMOVE `_io.exit()` AT THE BOTTOM

---

## 7. VSCode CPH Extension Setup

To fully leverage this boilerplate, configure the **CPH extension properly**.

---

### Step 1: Set Default Language to Python

1. Open VSCode Settings
2. Search for: `cph.general.defaultLanguage`
3. Set: `python`


---

### Step 2: Place Boilerplate File

* Save the boilerplate (`boilerplate.py` in this repository) as:

```
boilerplate.py
```

* Place it in the same directory as your CP scripts (or a dedicated templates folder)

---

### Step 3: Set Template Path

1. Open Settings
2. Search: `cph.general.defaultLanguageTemplateFileLocation`
3. Set path to your boilerplate
(Note: if it is in the same directory as the CP scripts, just set the path to `boilerplate.py`)

Now every new problem will auto-load this template.

---

### Step 4: Ignore STDERR

This is **critical** because `debprint` uses `stderr`.

1. Search: `cph.general.ignoreSTDERROR`
2. Enable the checkbox

Without this:

* Debug logs will interfere with judging
* Output comparison may fail

---

### Step 5: Add `--islocal` Argument

To enable debug mode during local runs:

1. Search: `cph.language.python.Args`
2. Add:

```
--islocal
```

Now every execution will run as:

```bash
python solution.py --islocal
```

This activates:

* Debug logs (through the `debprint` function)
* Execution metadata

---

## 8. Workflow Summary

### When solving locally:

* Write code using `input()` and `print()` (boilerplate versions)
* Use `debprint()` freely
* Run via CPH → automatically includes `--islocal`

### When submitting to Codeforces:

* Submit as-is
* No need to remove debug statements
* `debprint()` does nothing on Codeforces Judge

---

## 9. Example Usage

```python
t = input(int)
for _ in range(t):
    n = input(int)
    arr = input([int])
    debprint("Array:", arr)
    print(sum(arr))
```

---

## 10. Advantages of This Setup

* Cleaner code (no repetitive parsing)
* Faster I/O
* Safe debugging
* No need to strip logs before submission
* Consistent structure across problems

---

This setup is close to what high-rated competitive programmers use in practice—minimal overhead, maximum control.
