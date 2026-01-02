import writeToFile as wtf

studentGrade = {}

def add_student(name, grade):
    studentGrade[name] = grade

def get_grade():
    for name, grade in studentGrade.items():
        print(f"{name}: {grade}")

if __name__ == "__main__":
    while True:
        name = input("Enter student name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        grade = input(f"Enter grade for {name}: ")
        add_student(name, grade)

    print("\nStudent Grades:")
    get_grade()

    content = "Student Grades:\n"
    for name, grade in studentGrade.items():
        content += f"{name}: {grade}\n"
    wtf.writeto_file("studentGrades.txt", content)

