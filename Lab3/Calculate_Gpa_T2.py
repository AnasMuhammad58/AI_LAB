def calculate_gpa(student_list):
    # Define a dictionary to map percentage ranges to grade points
    grade_points_mapping = {
        (85, 100): 4.00,
        (80, 84): 3.66,
        (75, 79): 3.33,
        (71, 74): 3.00,
        (68, 70): 2.66,
        (64, 67): 2.33,
        (61, 63): 2.00,
        (58, 60): 1.66,
        (54, 57): 1.30,
        (50, 53): 1.00,
        (0, 49): 0.00,
    }

    # Initialize a list to store the results for each student
    results = []

    for student in student_list:
        # Extract student information
        student_name = student['name']
        student_marks = student['marks']

        # Calculate grade points for each course
        course_grade_points = [grade_points_mapping.get(mark, 0) for mark in student_marks]

        # Calculate GPA by averaging grade points
        gpa = sum(course_grade_points) / len(course_grade_points)

        # Determine the corresponding letter grades
        grades = []
        for mark in student_marks:
            for (min_mark, max_mark), grade_point in grade_points_mapping.items():
                if min_mark <= mark <= max_mark:
                    grades.append((mark, grade_point))
                    break

        # Append the student's result to the results list
        results.append({
            'name': student_name,
            'grades': grades,
            'grade_points': course_grade_points,
            'gpa': gpa
        })

    return results

# Example usage with a list of dictionaries representing student data
student_data = [
    {'name': 'Alice', 'marks': [88, 75, 92, 68, 78]},
    {'name': 'Bob', 'marks': [76, 81, 70, 62, 55]},
    {'name': 'Charlie', 'marks': [94, 89, 91, 85, 78]},
    # Add more student data here
]

# Calculate GPA for each student
gpa_results = calculate_gpa(student_data)

# Print the results
for result in gpa_results:
    print("Name:", result['name'])
    print("Grades:", result['grades'])
    print("Grade Points:", result['grade_points'])
    print("GPA:", result['gpa'])
    print()
