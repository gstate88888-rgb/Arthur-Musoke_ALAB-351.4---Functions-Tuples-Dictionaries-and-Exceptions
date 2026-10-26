# tuples_dicts.py
# Demonstrates tuples and dictionaries.


# Tuple of months
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# First and last month
print("First month:", months[0])
print("Last month:", months[-1])

# Demonstrate tuple immutability
try:
    months[0] = "NewMonth"
except TypeError as e:
    print("Tuples are immutable, error:", e)

# Dictionary of students and grades
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 88
}

# Add new student
students["Diana"] = 95

print("\nStudents after adding Diana:")
for name, grade in students.items():
    print(f"{name}: {grade}")

# Update a grade
students["Bob"] = 92

print("\nUpdated grade:")
print("Bob:", students["Bob"])

# Print all students and grades
print("\nAll student grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")
