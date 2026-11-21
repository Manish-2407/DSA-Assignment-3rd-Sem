# Data Structures and Python Assignments

This repository contains coursework covering Python programming fundamentals, algorithm analysis, recursion, and fundamental data structures.

## Student Information

- **Name:** Manish Singh
- **Roll No.:** 25BEC057
- **Institution:** IIITDM Jabalpur

## Contents

| File | Description |
| --- | --- |
| [Assignment_1.ipynb](Assignment_1.ipynb) | Python basics covering arithmetic operations, list and tuple operations, strings and palindromes, sets and dictionaries, and SGPA/GPA calculation. |
| [Assignment_2.py](Assignment_2.py) | Algorithm benchmarking covering indexing, searching, merge sort, pair counting, subset enumeration, and two prefix-average implementations. |
| [Assignment_3.py](Assignment_3.py) | Recursive functions and implementations of a stack, circular queue, and circular deque. |
| [lab1_execution_times.png](lab1_execution_times.png) | Execution-time comparison for the algorithms benchmarked in Assignment 2. |
| [lab1_normalized_times.png](lab1_normalized_times.png) | Normalized timing plots comparing measured growth with common asymptotic growth functions. |
| [lab2_prefix_averages.png](lab2_prefix_averages.png) | Comparison of quadratic and linear prefix-average implementations. |

## Assignment Details

### Assignment 1: Basics of Python Programming

The notebook demonstrates:

- Sum, difference, product, quotient, and remainder of two numbers
- Adding, removing, and inserting list elements
- Finding list maximum and minimum values and converting lists to tuples
- Character, vowel, and consonant counting
- String reversal and palindrome checking
- Set union, intersection, difference, and symmetric difference
- Selecting the student with the highest marks from a dictionary
- Calculating SGPA/GPA from course grade points and credits

### Assignment 2: Algorithm Analysis and Benchmarking

The script implements and benchmarks:

- List indexing
- Binary and linear search
- Merge sort
- Nested pair counting
- Subset mask enumeration
- Nested-loop and running-sum prefix-average algorithms

It validates the implemented functions, performs repeated timing trials, and generates the benchmark charts stored in this repository. The Lab 2 prefix-average experiments compare the `O(n^2)` implementation with the `O(n)` implementation.

### Assignment 3: Recursion and Data Structures

The script contains recursive implementations of:

- Factorial
- Sum of the first `n` natural numbers
- Integer power calculation
- Checking whether a sequence is in non-decreasing order

It also implements:

- **Stack:** `push`, `pop`, `top`, `is_empty`, and length
- **Circular Queue:** `enqueue`, `dequeue`, `first`, `display`, `is_empty`, and length
- **Circular Deque:** add/delete operations at both ends

The recursive and queue-related functions validate inputs through implemented exceptions. Negative or non-integer values for `n` raise `ValueError`, invalid stack or queue access raises `IndexError`, and operations on full structures raise `OverflowError`.

## Requirements

- Python 3
- Matplotlib
- Jupyter Notebook or Jupyter-compatible environment

Install the required Python packages with:

```powershell
python -m pip install matplotlib jupyter
```

## Running the Assignments

### Run Assignment 2

From the repository folder:

```powershell
python Assignment_2.py
```

The script prints timing measurements and saves `lab1_execution_times.png`, `lab1_normalized_times.png`, and `lab2_prefix_averages.png` in the current folder.

### Run Assignment 3

From the repository folder:

```powershell
python Assignment_3.py
```

The script runs demonstration code for the recursive functions, stack, circular queue, and circular deque.

### Open Assignment 1

Open [Assignment_1.ipynb](Assignment_1.ipynb) in Jupyter Notebook:

```powershell
jupyter notebook Assignment_1.ipynb
```

The notebook can also be uploaded to Google Colab or opened in a Jupyter-compatible editor.

## Benchmark Results and Plots

### [lab1_execution_times.png](lab1_execution_times.png)

Compares measured execution time with scaled growth models for indexing, searching, merge sort, pair counting, and subset enumeration.

### [lab1_normalized_times.png](lab1_normalized_times.png)

Displays normalized timing plots used to assess whether each algorithm follows its expected growth trend.

### [lab2_prefix_averages.png](lab2_prefix_averages.png)

Compares the nested-loop prefix-average algorithm with the running-sum algorithm and illustrates quadratic versus linear growth.

## Example Output

`Assignment_3.py` prints:

- Factorial, natural sum, and power calculation results
- Results of the non-decreasing-order checks
- Stack top, popped values, length, and empty state
- Circular queue contents and wrapped storage state
- Circular deque contents after additions and deletions

`Assignment_2.py` prints validation timing trials, median execution values, normalized timing tables, and messages indicating which plot files were saved.
