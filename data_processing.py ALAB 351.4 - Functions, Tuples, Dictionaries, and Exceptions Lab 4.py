# data_processing.py
# Uses functions, tuples, dictionaries, and exception handling.


def get_average_grade(grades_tuple):
    try:
        average = sum(grades_tuple) / len(grades_tuple)
        return average
    except ZeroDivisionError:
        print("Warning: No grades available.")
        return None


course_grades = {
    "Math": (90, 85, 88),
    "Science": (95, 80, 90),
    "History": (88, 84, 92),
    "Art": ()  # Empty tuple for edge case
}


for course, grades in course_grades.items():
    average = get_average_grade(grades)

    if average is not None:
        print(f"The average grade for {course} is {average:.2f}")
    else:
        print(f"No average available for {course}")
