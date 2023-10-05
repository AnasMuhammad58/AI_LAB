def calculate_gpa(students):
    def calculate_grade_points(marks):
        if marks >= 85:
            return 4.00
        elif marks >= 80:
            return 3.66
        elif marks >= 75:
            return 3.33
        elif marks >= 71:
            return 3.00
        elif marks >= 68:
            return 2.66
        elif marks >= 64:
            return 2.33
        elif marks >= 61:
            return 2.00
        elif marks >= 58:
            return 1.66
        elif marks >= 54:
            return 1.30
        elif marks >= 50:
            return 1.00
        else:
            return 0.00

    result = []
    for student in students:
        name = student['name']
        marks = student['marks']
        total_grade_points = sum([calculate_grade_points(mark) for mark in marks])
        gpa = total_grade_points / len(marks)
        grades = [calculate_grade_points(mark) for mark in marks]

        result.append({
            'name': name,
            'grades': grades,
            'grade_points': total_grade_points,
            'gpa': gpa
        })

    return result

# Example usage:
students = [
    {'name': 'Anas', 'marks': [90, 88, 76, 95, 82]},
    {'name': 'Ashir', 'marks': [78, 85, 92, 71, 65]},
    {'name': 'Faheem', 'marks': [55, 62, 58, 49, 73]}
]

gpa_results = calculate_gpa(students)
for result in gpa_results:
    print(f"Name: {result['name']}, GPA: {result['gpa']}, Grades: {result['grades']}, Grade Points: {result['grade_points']}")