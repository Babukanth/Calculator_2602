def calculator(num1, num2, op):
    # Perform the calculation
    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2

    else:
        return "Invalid operator"

  # Determine if the result is positive, negative, or zero
    if result > 0:
        sign = "Positive"
    elif result < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    return f"Result = {result}\n{sign}"

result = calculator(10, 5, "+")
print("Result =", result)

result = calculator(10, 5, "-")
print("Result =", result)

result = calculator(10, -5, "/")
print("Result =", result)

result = calculator(10, 5, "*")
print("Result =", result)

result = calculator(10, 0, "/")
print("Result =", result)

result = calculator(10, 5, "**")
print("Result =", result)
