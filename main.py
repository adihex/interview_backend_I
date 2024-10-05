def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = 1
    value = 0
    i = 0
    last_token_type = None
    unary_minus = False  # New flag to handle unary minus

    while i < len(s):
        char = s[i]
        if char == ' ':
            i += 1
            continue
        if char.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            value += sign * num
            if unary_minus:
                value = -value
                unary_minus = False
            i -= 1
            last_token_type = 'number'
        elif char == '+':
            if i == 0 or last_token_type in [None, 'operator', 'open_paren']:
                raise ValueError(f"Invalid '+' at position {i}")
            sign = 1
            last_token_type = 'operator'
        elif char == '-':
            if last_token_type in ['number', 'close_paren']:
                sign = -1
                last_token_type = 'operator'
            else:
                unary_minus = True
                last_token_type = 'operator'
        elif char == '(':
            stack.append(value)
            stack.append(sign)
            stack.append(unary_minus)  # Save unary_minus state
            value = 0
            sign = 1
            unary_minus = False
            last_token_type = 'open_paren'
        elif char == ')':
            if not stack:
                raise ValueError(f"Mismatched parenthesis at position {i}")
            if last_token_type in ['operator', 'open_paren']:
                raise ValueError(f"Invalid expression before ')' at position {i}")
            if unary_minus:
                value = -value
            prev_unary_minus = stack.pop()
            value *= stack.pop()
            value += stack.pop()
            if prev_unary_minus:
                value = -value
            unary_minus = False
            last_token_type = 'close_paren'
        else:
            raise ValueError(f"Invalid character '{char}' at position {i}")
        i += 1

    if stack:
        raise ValueError(f"Mismatched parenthesis: unclosed '(' found")
    if last_token_type == 'operator':
        raise ValueError("Expression cannot end with an operator")

    if unary_minus:
        value = -value

    return value


# Main program
if __name__ == "__main__":
    while True:
        expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break
        try:
            result = calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        print()  # Print a blank line for readability

