# Basic Calculator with Python

## Problem Description

Implement a basic calculator to evaluate a given mathematical expression represented as a string. The expression can contain non-negative integers, the operators `+`, `-`, and parentheses `(`, `)`. You must not use any built-in function that evaluates strings as mathematical expressions, such as `eval()`.

## Requirements

- Implement a function that takes a string expression and returns the evaluated result as an integer.

## Examples

### Example 1
**Input:**
```python
s = "1 + 1"
```
**Output:**
```python
2
```

### Example 2
**Input:**
```python
s = "2 - 1 + 2"
```
**Output:**
```python
3
```

### Example 3
**Input:**
```python
s = "(1 + (4 + 5 + 2) - 3) + (6 + 8)"
```
**Output:**
```python
23
```

## Constraints

- The length of `s` will be in the range: `1 <= s.length <= 3 * 10^5`
- The string `s` consists of digits, `+`, `-`, `(`, `)`, and spaces.
- The expression is guaranteed to be valid.
- The operator `+` is not used as a unary operation (i.e., "+1" and "+(2 + 3)" are invalid).
- The operator `-` could be used as a unary operation (i.e., "-1" and "-(2 + 3)" are valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit within a signed 32-bit integer.

## Function Signature

```python
def calculate(s: str) -> int:
    pass
```

## Implementation Notes

- Ensure that you correctly handle operator precedence and parentheses.
- Utilize a stack to manage the evaluation of the expression, especially for handling nested parentheses.
- Consider how you will parse numbers and operators as you iterate through the string.
- Be careful with whitespace in the input string, and ensure it does not affect the evaluation.

## Testing

Make sure to test your implementation with various edge cases, including:

1. Large expressions with multiple operators and parentheses.
2. Expressions with single numbers and unary operations.
3. Inputs with varying amounts of whitespace.

## Submission

Fork the Repository: Click on the "Fork" button at the top right of this repository to create your own copy.

Implement the Solution: Work on the problem in your forked repository. Make sure to follow the problem description and constraints provided.

Testing: Test your implementation thoroughly to ensure it works for all specified cases.

Share Your Work: Once you are satisfied with your implementation, push your changes to your forked repository and share the link with us.


