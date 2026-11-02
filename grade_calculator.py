
name = input("Enter your name: ")

def get_marks(subject):
    while True:
        marks = float(input(f"Enter your {subject} marks (0-100): "))
        if 0 <= marks <= 100:
            return marks
        else:
            print("Invalid marks! Please enter between 0 and 100.")

maths = get_marks("Maths")
python = get_marks("Python")
english = get_marks("English")

total = maths + python + english
average = total / 3

print("\n  STUDENT REPORT ")
print("Student Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
