#    Students and raw data
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#    averaging the raw data
def average(numbers):
    total = sum(numbers)
    total = float(total) / float(len(numbers))
    return total

#   Weighted Averages Calculations
def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6
    avrg = homework + quizzes + tests
    return avrg

#   converting grade average into letter grade
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#     printing the letter grade per student
print("Lloyds's Letter Grade: ", get_letter_grade(get_average(lloyd)))
print("Alice's Letter Grade: ", get_letter_grade(get_average(alice)))
print("Tyler's Letter Grade: ", get_letter_grade(get_average(tyler)))

students = [lloyd, alice, tyler]

#     getting the class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

#     printing the class average and class letter grade average
print("Classes's Avg Grade: ", get_class_average(students))
print("Classes's Avg Letter Grade: ", get_letter_grade(get_class_average(students)))


## Exam Grades
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("1st Exam Grades:"), grades

def print_grades(grades):
    c = []
    for i in grades:
        c.append(i)
        print(i)

print_grades(grades)

def grades_sum(scores):
    total = 0
    for n in scores:
        total = total + n
    return total


print("1st Exam Total Score: ", grades_sum(grades))

def grades_average(grades):
    grades_sum(grades)
    avrg = grades_sum(grades) / float(len(grades))
    return avrg

print("1st Exam Avg Score: ", grades_average(grades))

def grades_variance(grades):
    variance = 0
    for g in grades:
        variance += ((grades_average(grades) - g) ** 2)
    return variance / len(grades)
print("1st Exam Variance Score: ", grades_variance(grades))

def grades_std_deviation(variance):
    return (variance) ** 0.5
    variance = grades_variance(grades)

print("1st Exam Deviations Score: ", grades_std_deviation(grades_variance(grades)))
