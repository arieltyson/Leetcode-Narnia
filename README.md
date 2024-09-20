# Leetcode-Narnia 🐍

# Subtract Large Numbers Represented as Lists

## Problem Statement:
You are given two lists `A` and `B`, where each list represents a non-negative integer. The digits of the numbers are provided in order, where each digit is a single digit (0 through 9).

Your task is to subtract the number represented by `B` from the number represented by `A`, digit by digit, and return the result as a list of digits. If the result is negative, represent it by negating the most significant digit.

### Constraints:
- `0 <= digit <= 9` for all digits in both lists.
- The lists `A` and `B` may be of different lengths.
- `1 <= len(A), len(B) <= 10^5`

## Function Signature:
```python
def subtract_lists(A: List[int], B: List[int]) -> List[int]:
    pass
```

### Examples:
### 1.
```
Input: A = [1, 0, 2], B = [2, 2, 5]
Output: [-1, 2, 3]
```

```
A represents 102, B represents 225.
102 - 225 = -123, so the result is [-1, 2, 3].
```

### 2.
```
Input: A = [9, 0, 0, 0], B = [1]
Output: [8, 9, 9, 9]
```
```
Explanation: 
A represents 9000, B represents 1.
9000 - 1 = 8999, so the result is [8, 9, 9, 9].
```

### Step 4: **Create the Solution File (`subtract_lists.py`)**

This file will contain the function signature that others will modify. It should be empty initially, so people can implement their own solutions. Here's a sample `subtract_lists.py` file:

```python
from typing import List

def subtract_lists(A: List[int], B: List[int]) -> List[int]:
    # Implement your solution here
    pass
```

## How to Run the Tests:

### Using `unittest`:
1. Make sure you have Python installed.
2. In the terminal, navigate to the project directory.
3. Run the following command:
```bash
python -m unittest test_subtract_lists.py
```

### Using `pytest`:
1. Make sure you have Python installed.
2. In the terminal, navigate to the project directory.
3. Run the following command:
```bash
pip install pytest
pytest test_subtract_lists.py
```

