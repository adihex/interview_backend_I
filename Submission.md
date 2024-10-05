# Implementation of Basic Calculator With Python

`Name: Aditya Balakrishnan`

I have tried to implement the calculator as close to the given problem description as possible.
I am using a Stack based approach. It is a variation of Djikstra's Shunting Yard algorithm with a difference that,
we are able to evaluate the infix expression on the go itself as opposed to first converting it into its postfix form and then evaluating the postfix expression using another stack. 

## Brief explanation of the algorithm:

1. We parse through the string and if we find an empty space, we ignore it.
2. Whenever we find that the current character is a digit, we keep checking until we find a non-digit character. We convert whatever digits we have obtained in that interval to their numeric representation.
3. We are keeping a flag called `unary_minus` to check if we have encountered a `-` symbol. If we have, we multiply the number in the previous step with -1.
4. We use a `sign` variable to keep track of whether the next number should be added or subtracted. It's initialized to 1 and changes to -1 when we encounter a minus sign.
5. The `value` variable keeps track of the current result as we parse through the expression.
6. We use a stack to handle parentheses. When we encounter an opening parenthesis, we push the current `value`, `sign`, and `unary_minus` state onto the stack and reset our variables.
7. When we encounter a closing parenthesis, we pop the previous state from the stack and combine it with the current value.
8. We keep track of the `last_token_type` to ensure the expression is valid (e.g., we can't have two operators in a row).
9. The algorithm handles unary minus operations by using an `unary_minus` flag. This allows us to differentiate between binary minus (subtraction) and unary minus (negation).
10. Throughout the process, we perform various error checks:
    - Ensure operators are not at the beginning or end of the expression
    - Check for mismatched parentheses
    - Validate that numbers follow operators and vice versa
    - Catch any invalid characters in the expression
11. After parsing the entire string, we return the final `value`, which represents the result of the calculation.

## Steps to run the code

1. You can run the calculator directly and test by adding inputs from stdin
```bash
   python3 main.py
```

2. I have written a test file which you can invoke using `unittest` library in python. Add the desired test cases in the `test.py` file. Then run:
```bash
    python3 -m unittest test.py
```

This is a problem I had done a long time back using C++. Thank you for giving me an opportunity to go through it again and solve it in Python. This time the developer experience was much better for sure :)