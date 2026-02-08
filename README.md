# Codeforces Python Template

A clean and efficient template for Codeforces competitions in Python.

## 🚀 Quick Setup

### 1. Create Conda Environment

```bash
# Run the setup script
./setup.sh

# Or manually create the environment
conda env create -f _environment.yml
```

### 2. Activate Environment

```bash
conda activate codeforces
```

### 3. Verify Installation

```bash
python --version  # Should show Python 3.11.x
```

## 📁 Project Structure

```
python/
├── A.py, B.py, C.py, D.py, E.py, F.py  # Solution files for each problem
├── main.py                              # Test runner script
├── test.py                              # Unit test template
├── input.txt                            # Input test cases
├── output.txt                           # Expected output (optional)
├── requirements.txt                     # Python dependencies
├── environment.yml                      # Conda environment config
└── setup.sh                             # Setup script
```

## 💻 Usage

### Method 1: Using the Test Runner (Recommended)

1. Copy test cases to `input.txt`
2. Write your solution in the problem file (e.g., `A.py`)
3. Run the test:

```bash
python main.py A        # Test problem A
python main.py B        # Test problem B
```

### Auto-Verification Feature

The test runner automatically compares your output with `output.txt` and shows pass/fail indicators:

```
Verification Results:
==================================================
  #   Got   Expected
--------------------------------------------------
  1   ✓ 6     6
  2   ✓ 10    10
  3   ✗ 15    14       <- Red ✗ for wrong answer
  4   ✓ 0     0
--------------------------------------------------
Failed: 3/4 passed
==================================================
```

**Usage:**
```bash
python main.py A              # Run with auto-verification (default)
python main.py A --no-verify  # Run without verification
```

**How to use:**
1. Copy sample input to `input.txt`
2. Copy expected output to `output.txt`
3. Run `python main.py A` - instantly see which test cases pass or fail

### Method 2: Direct Execution

```bash
python A.py < input.txt
```

### Method 3: Interactive Testing

Modify and run `test.py` for quick unit tests:

```bash
python test.py
```

## 📝 Template Structure

Each problem file (A.py - F.py) follows this structure:

```python
def solve():
    """Main solution function"""
    # Read input
    n = int(input())

    # Your logic here
    result = n

    # Output result
    print(result)

def main():
    """Handle multiple test cases"""
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()  # Or solve() for single test case
```

## 🎯 Best Practices for Codeforces

### 1. Input/Output Tips

```python
# Fast I/O for large inputs
import sys
input = sys.stdin.readline

# Multiple values on one line
a, b, c = map(int, input().split())

# List of integers
arr = list(map(int, input().split()))

# Multiple lines
n = int(input())
data = [input().strip() for _ in range(n)]
```

### 2. Common Patterns

```python
# Binary search
from bisect import bisect_left, bisect_right

# Sorting with custom key
arr.sort(key=lambda x: (x[0], -x[1]))

# Counter for frequency
from collections import Counter
freq = Counter(arr)

# Default dict
from collections import defaultdict
graph = defaultdict(list)

# Deque for efficient queue operations
from collections import deque
q = deque()
```

### 3. Mathematical Helpers

```python
import math

# GCD and LCM
from math import gcd
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Prime checking
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Modular arithmetic
MOD = 10**9 + 7
result = (a + b) % MOD
```

### 4. Time Complexity Tips

- **O(n)**: Linear - usually safe up to n = 10^8
- **O(n log n)**: Sorting - safe up to n = 10^6
- **O(n²)**: Nested loops - safe up to n = 10^4
- **O(2^n)**: Exponential - safe up to n = 20

### 5. Common Mistakes to Avoid

- ❌ Forgetting to handle multiple test cases
- ❌ Not using `strip()` when reading strings
- ❌ Integer overflow (Python handles this well!)
- ❌ Wrong input format (check problem statement carefully)
- ❌ Printing extra spaces or newlines

## 🔧 Quick Commands

```bash
# Activate environment
conda activate codeforces

# Deactivate environment
conda deactivate

# Update environment
conda env update -f environment.yml

# Install new package
pip install <package-name>

# Delete environment (if needed)
conda env remove -n codeforces
```

## 📚 Useful Resources

- [Codeforces](https://codeforces.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Python Competitive Programming Tips](https://codeforces.com/blog/entry/89638)

## 🎮 During Contest

1. **Read all problems first** - identify the easiest ones
2. **Start with easier problems** - build confidence and rating
3. **Use input.txt** for testing - faster than manual input
4. **Test edge cases**:
   - Minimum values (n=1, empty arrays)
   - Maximum values (constraints)
   - Special cases (all same, all different)
5. **Before submitting**:
   - Check input/output format
   - Test with sample cases
   - Check for TLE (time limit)
   - Remove debug prints

## 🐛 Debugging Tips

```python
# Debug print (remove before submission!)
print(f"Debug: n={n}, arr={arr}", file=sys.stderr)

# Assert for validation during development
assert len(arr) == n, "Array length mismatch"

# Timing your code
import time
start = time.time()
# ... your code ...
print(f"Time: {time.time() - start:.3f}s", file=sys.stderr)
```

## 📊 Typical Problem Types

1. **Math/Number Theory**: GCD, LCM, primes, modular arithmetic
2. **Greedy**: Sorting, optimization
3. **DP**: Memoization, tabulation
4. **Graph**: BFS, DFS, shortest paths
5. **Data Structures**: Arrays, hash maps, heaps
6. **Strings**: Pattern matching, manipulation
7. **Binary Search**: On answer space
8. **Combinatorics**: Permutations, combinations

Good luck in your competition! 🚀
