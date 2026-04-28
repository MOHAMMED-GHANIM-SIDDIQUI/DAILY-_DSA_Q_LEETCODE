# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

A collection of daily LeetCode problem solutions. Each file is a standalone solution to a single LeetCode problem — there is no build system, shared libraries, or inter-file dependencies.

## File Naming Convention

Files follow the pattern: `{problemNumber}-LEETCODE.{ext}` (e.g., `2033-LEETCODE.py`, `1007-LEETCODE.cpp`). Occasionally a second approach is stored as `{problemNumber}-2nd-LEETCODE.{ext}`.

## Languages

- **Python** (~109 files): Solutions use LeetCode's `Solution` class pattern with type hints from `typing` (e.g., `List`, `Optional`). No imports are included for LeetCode-provided types.
- **C++** (~54 files): Solutions use LeetCode's `Solution` class/struct pattern with standard library types (`vector`, `string`, etc.).

## Running Solutions

There is no test framework. To verify a solution locally, add a `main` function or test harness manually:
- Python: `python {problemNumber}-LEETCODE.py`
- C++: `g++ -o sol {problemNumber}-LEETCODE.cpp && ./sol`

## When Adding New Solutions

- Use the existing naming convention: `{problemNumber}-LEETCODE.py` or `{problemNumber}-LEETCODE.cpp`
- Use the LeetCode `Solution` class pattern — do not add `main()` unless specifically asked
- Each file should be self-contained with only the solution class
