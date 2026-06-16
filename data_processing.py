# data_processing.py
# Demonstrates functions, tuples, dictionaries, loops, and exception handling

def get_average_grade(grades_tuple):
    """
    Takes a tuple of grades and returns the average.
    Returns None if the tuple is empty.
    """
    try:
        average = sum(grades_tuple) / len(grades_tuple)
        return average
    except ZeroDivisionError:
        print(" ")
        print("Warning: Cannot calculate average for the course because the grade list is empty.")
        return None


# Dictionary of courses and their grades
course_grades = {
    "Math": (87, 91, 89, 90),
    "Science": (75, 83, 80, 84),
    "History": (96, 93, 89),
    "English": ()  # Edge case: empty tuple
}

# Process each course and display the average grade
for course, grades in course_grades.items():
    try:
        average = get_average_grade(grades)

        if average is not None:
            print(f"The average grade for {course} is {average:.1f}")
        else:
            print(f"No grades available for {course}.")
            
    except Exception as e:
        print(f"An error occurred while processing {course}: {e}")