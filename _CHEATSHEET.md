# Python Codeforces Cheatsheet 🚀

Quick reference for common patterns during contests.

## 📥 Input/Output

```python
# Single integer
n = int(input())

# Multiple integers
a, b, c = map(int, input().split())

# Array of integers
arr = list(map(int, input().split()))

# Multiple lines of integers
data = [int(input()) for _ in range(n)]

# String without newline
s = input().strip()

# Fast I/O (for large inputs)
import sys
input = sys.stdin.readline
```

## 📊 Data Structures

```python
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

# Counter - frequency count
freq = Counter([1,2,2,3,3,3])  # {3:3, 2:2, 1:1}

# defaultdict - auto-initialize
graph = defaultdict(list)
graph[1].append(2)  # No KeyError

# deque - efficient queue
q = deque([1,2,3])
q.append(4)      # Add right
q.appendleft(0)  # Add left
q.pop()          # Remove right
q.popleft()      # Remove left

# Min heap
heap = [3,1,4,1,5]
heapify(heap)
heappush(heap, 2)
smallest = heappop(heap)

# Max heap (negate values)
heap = [-x for x in [3,1,4,1,5]]
heapify(heap)

# Binary search
idx = bisect_left(arr, target)   # Leftmost position
idx = bisect_right(arr, target)  # Rightmost position
```

## 🔢 Math

```python
import math
from math import gcd

# GCD & LCM
g = gcd(a, b)
lcm = abs(a * b) // gcd(a, b)

# Power with modulo
MOD = 10**9 + 7
result = pow(base, exp, MOD)

# Square root
sqrt_n = int(n ** 0.5)

# Factorial
fact = math.factorial(n)

# Combinations & Permutations
from math import comb, perm
c = comb(n, k)  # nCk
p = perm(n, k)  # nPk

# Prime check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Prime factorization
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
```

## 🔄 Sorting & Searching

```python
# Sort list
arr.sort()                          # In-place
arr.sort(reverse=True)              # Descending
sorted_arr = sorted(arr)            # New list

# Sort with key
arr.sort(key=lambda x: x[0])        # By first element
arr.sort(key=lambda x: (x[0], -x[1]))  # Multiple keys

# Binary search on answer
def binary_search(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## 🎯 String Operations

```python
# Check if palindrome
is_palindrome = s == s[::-1]

# Count occurrences
count = s.count('a')

# Split and join
parts = s.split()
joined = ' '.join(parts)

# Character codes
ord_a = ord('a')  # 97
char = chr(97)    # 'a'

# Alphabet
import string
lowercase = string.ascii_lowercase  # 'abc...xyz'
uppercase = string.ascii_uppercase  # 'ABC...XYZ'
```

## 🌲 Graph Algorithms

```python
# BFS
from collections import deque

def bfs(start, graph):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

# DFS (recursive)
def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

# DFS (iterative)
def dfs_iter(start, graph):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return visited
```

## 🎲 Dynamic Programming

```python
# Memoization (top-down)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Tabulation (bottom-up)
def fib_tab(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 2D DP
dp = [[0] * cols for _ in range(rows)]
```

## 🔧 Useful Tricks

```python
# Infinity
INF = float('inf')
NEG_INF = float('-inf')

# Swap values
a, b = b, a

# Min/max of list
min_val = min(arr)
max_val = max(arr)

# Sum of list
total = sum(arr)

# Check if all/any satisfy condition
all_positive = all(x > 0 for x in arr)
any_negative = any(x < 0 for x in arr)

# Enumerate with index
for i, val in enumerate(arr):
    print(f"{i}: {val}")

# Zip multiple lists
for a, b in zip(list1, list2):
    print(a, b)

# Range tricks
range(n)         # 0 to n-1
range(1, n+1)    # 1 to n
range(n, 0, -1)  # n to 1 (descending)

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Nested list (2D array)
matrix = [[0] * cols for _ in range(rows)]
# DON'T: [[0] * cols] * rows  # This creates shallow copies!

# Get max/min with key
max_element = max(arr, key=lambda x: x[1])

# Rotate list
arr = arr[k:] + arr[:k]  # Rotate left by k

# Remove duplicates (maintain order)
unique = list(dict.fromkeys(arr))

# Flatten 2D list
flat = [item for sublist in nested for item in sublist]
```

## ⚡ Performance Tips

```python
# Fast modulo
MOD = 10**9 + 7
result = (a + b) % MOD

# Avoid repeated calculations
# Bad:
for i in range(len(arr)):  # Calls len() every iteration

# Good:
n = len(arr)
for i in range(n):

# String concatenation in loop
# Bad:
s = ""
for c in chars:
    s += c  # O(n²)

# Good:
s = "".join(chars)  # O(n)

# Multiple conditions
# Use 'and' short-circuit
if condition1 and expensive_condition2:
    pass
```

## 🎮 Contest Checklist

- [ ] Read ALL problems first
- [ ] Identify easiest problems
- [ ] Check input/output format carefully
- [ ] Test with sample inputs
- [ ] Test edge cases (n=1, n=max, all same, all different)
- [ ] Remove debug prints
- [ ] Check time complexity
- [ ] Submit!

## 🐛 Common Errors

```python
# Integer division
a // b  # Floor division
a / b   # Float division

# Deep copy vs shallow copy
import copy
deep = copy.deepcopy(nested_list)

# String immutability - use list for modifications
chars = list(s)
chars[0] = 'a'
s = ''.join(chars)

# List index out of range - always check bounds
if i < len(arr):
    value = arr[i]
```

Good luck! 🍀
