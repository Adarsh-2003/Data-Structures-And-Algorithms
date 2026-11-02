### Quick-reference table

| Code behaviour | Likely time complexity |
|---|---|
| Direct index or variable access | `O(1)` |
| One pass through `n` items | `O(n)` |
| Two full nested loops | `O(n²)` |
| Three full nested loops | `O(n³)` |
| Repeatedly halve/double a value | `O(log n)` |
| `O(n)` work across `O(log n)` levels | `O(n log n)` |
| Two recursive branches per level, depth `n` | `O(2ⁿ)` |
| Generate every permutation | `O(n!)` |

> **Core principle:** Analyse what the code does as the input grows. Count iterations, inspect the cost inside each iteration, account for recursion and built-ins, then simplify. Never decide complexity from the visual appearance of code alone.
"""

## 1. The Big-O ladder

| Complexity | Name | Typical behaviour |
|---|---|---|
| `O(1)` | Constant | Fixed amount of work |
| `O(log n)` | Logarithmic | Repeatedly halves or multiplies the search space by a constant factor |
| `O(n)` | Linear | Processes each element once |
| `O(n log n)` | Linearithmic | Performs linear work across logarithmically many levels |
| `O(n²)` | Quadratic | Compares or processes pairs |
| `O(n³)` | Cubic | Three full input-sized loops |
| `O(2ⁿ)` | Exponential | Explores two choices per input element |
| `O(n!)` | Factorial | Generates every possible ordering |

**Growth intuition:** `O(1)` and `O(log n)` scale very well. `O(n)` is usually manageable. Quadratic and higher growth can become expensive quickly as `n` increases.

## 2. How to recognise each complexity

### `O(1)` — Constant

The work does not grow with the input size.

```python
value = numbers[2]
```

Typical examples: list index access, reading a variable, `len(numbers)`.

**Clue:** A fixed number of operations, independent of `n`.

### `O(log n)` — Logarithmic

The problem size is repeatedly divided or multiplied by a constant factor.

```python
while n > 1:
    n //= 2
```

Typical examples: binary search; repeatedly dividing by 2, 10, or another constant.

**Clue:** The input shrinks (or a counter grows) geometrically each iteration. The logarithm's base is omitted in Big-O: `O(log₂ n) = O(log n)`.

### `O(n)` — Linear

The code processes `n` elements once.

```python
for item in items:
    print(item)
```

Typical examples: traversing a list, finding a maximum, counting elements.

**Clue:** One complete pass over the input.

### `O(n log n)` — Linearithmic

The algorithm does `O(n)` work across `O(log n)` levels.

Typical example: merge sort. It splits the input into halves, creating logarithmically many levels, while each level processes a total of `n` elements.

**Clue:** Often appears in efficient comparison sorting and divide-and-conquer algorithms.

### `O(n²)` — Quadratic

Two independent loops each run `n` times.

```python
for i in range(n):
    for j in range(n):
        work()
```

Total work: `n × n = n²`.

Typical examples: comparing every pair; simple nested-loop pair checks.

**Clue:** Two full input-sized nested loops.

### `O(n³)` — Cubic

Three independent loops each run `n` times.

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            work()
```

Total work: `n × n × n = n³`.

**Clue:** Three full input-sized nested loops.

### `O(2ⁿ)` — Exponential

Each input element creates two possible choices, such as include or exclude.

```python
def explore(i, n):
    if i == n:
        return
    explore(i + 1, n)
    explore(i + 1, n)
```

Typical examples: generating all subsets; brute-force include/exclude recursion.

**Clue:** A branching process with roughly two recursive choices at each of `n` levels.

### `O(n!)` — Factorial

The algorithm generates all possible orderings of `n` elements.

For example, three distinct items have `3! = 6` permutations.

Typical example: generating all permutations.

**Clue:** Every possible ordering is explored. The number of outputs alone is `n!`; the full runtime may include additional work per output.

## 3. Rules for analysing code

### Rule 1 — Sequential loops are added

```python
for i in range(n):
    work()

for j in range(n):
    work()
```

`O(n) + O(n) = O(2n) = O(n)`.

### Rule 2 — Nested loops are multiplied

Two independent loops of `n` iterations each: `O(n × n) = O(n²)`.

### Rule 3 — A fixed inner loop does not add another `n`

```python
for i in range(n):
    for j in range(5):
        work()
```

This is `O(5n) = O(n)`, not `O(n²)`.

### Rule 4 — Repeated doubling or halving suggests logarithmic time

```python
i = 1
while i < n:
    i *= 2
```

The values grow as `1, 2, 4, 8, ...`, so the loop runs `O(log n)` times.

### Rule 5 — Keep the dominant term

Drop constant factors and lower-order terms:

| Expression | Simplified result |
|---|---|
| `O(5)` | `O(1)` |
| `O(5n)` | `O(n)` |
| `O(n + 100)` | `O(n)` |
| `O(n² + n)` | `O(n²)` |
| `O(3n² + 5n + 10)` | `O(n²)` |
| `O(4 log n)` | `O(log n)` |

### Rule 6 — Nested loops do not always mean quadratic

Count how many times each loop actually runs. A loop over a fixed range, such as `range(5)`, contributes only a constant factor.

## 4. Common Python operation costs

Typical average or amortised costs:

| Operation | Time complexity |
|---|---|
| `items[i]` | `O(1)` |
| `len(items)` | `O(1)` |
| `items.append(x)` | `O(1)` amortised |
| `items.pop()` (last item) | `O(1)` |
| `items.insert(0, x)` | `O(n)` |
| `x in items` (list) | `O(n)` |
| `x in set_items` | `O(1)` average |
| `x in dict_items` | `O(1)` average |
| `sorted(items)` | `O(n log n)` |
| `items.reverse()` | `O(n)` |
| `str(num)` | `O(d)`, where `d` is the number of digits |

These are typical costs, not guarantees for every possible case. For example, set and dictionary lookups can degrade in pathological collision cases.
