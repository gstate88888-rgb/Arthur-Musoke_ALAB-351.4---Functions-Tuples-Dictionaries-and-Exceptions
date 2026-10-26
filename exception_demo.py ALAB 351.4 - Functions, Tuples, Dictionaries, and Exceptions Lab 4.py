# exception_demo.py
# Demonstrates raising and handling exceptions.


def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


# Test safe_divide function
try:
    result = safe_divide(10, 0)
    print("Result:", result)

except ValueError as e:
    print("Error:", e)

finally:
    print("Division operation completed")


# Demonstrating a generic exception
try:
    number = int("hello")
    print(number)

except Exception as e:
    print("Generic exception caught:", e)
