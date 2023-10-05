class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_marks(self, subject, mark):
        self.marks.append((subject, mark))

    def calculate_average(self):
        if not self.marks:
            return 0.0
        total_marks = sum(mark for _, mark in self.marks)
        average = total_marks / len(self.marks)
        return average

# Create an instance of the Student class
student1 = Student("Muhammad Anas", "051")

# Add some marks
student1.add_marks("Math", 90)
student1.add_marks("Science", 90)
student1.add_marks("History", 78)

# Calculate and print the average marks
average_marks = student1.calculate_average()
print(f"{student1.name}'s Average Marks: {average_marks:.2f}")
