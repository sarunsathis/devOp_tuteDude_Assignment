import writeToFile as wtf

def function_checker(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
    
if __name__ == "__main__":
    test_grade = int(input("Enter grade separated by spaces: "))
    fileContent = "Assignment 2 Grade Checker\n"
    fileContent += "Grade is: " + function_checker(test_grade)
    wtf.writeto_file("gradeChecker.txt", fileContent)