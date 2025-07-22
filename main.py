class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")

# Create list of students
students = []

# Add 2 students manually
students.append(Student("Sandeep", 101, 85))
students.append(Student("Sanu", 102, 92))

# Display student records
print("Student Records:\n")
for student in students:
    student.display()
    print("-----------")
