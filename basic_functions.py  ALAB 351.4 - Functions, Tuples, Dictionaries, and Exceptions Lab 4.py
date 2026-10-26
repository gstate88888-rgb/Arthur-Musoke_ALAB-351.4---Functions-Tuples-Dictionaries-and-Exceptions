basic_functions.py

# basic_functions.py
# Demonstrates creating and using simple functions.


# Function that greets a user
def greet_user(name=""):
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")


# Function that returns the sum of two numbers
def add_two_numbers(a, b):
    return a + b


# Function that checks if a number is even
def is_even(num):
    return num % 2 == 0


# Main program

# Call greet_user with a name
greet_user("Arthur")

# Call greet_user without a name
greet_user()

# Call add_two_numbers and store result
sum_result = add_two_numbers(10, 5)
print("Sum:", sum_result)

# Call is_even and print results
print("4 is even:", is_even(4))
print("7 is even:", is_even(7))
