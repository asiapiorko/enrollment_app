from student import Student
from course import Course

class Main:
    global students
    students = []

    def print_menu():
        print("1. create a student")
        print("2. create a course")
        print("q. exit the app")

    def print_student_menu():
        student = Student()
        name = input("Enter student name ")
        last_name = input("Enter student last name ")
        students.append(student.create_student(name, last_name))#remove and recreate in student class and the same things with course class
        # student.create_student(name, last_name)
        # student.show_students_list()
        print(students)
    
    def print_course_menu():
        course_name = input("Enter course name")
        students_name = input("Enter student name ")

    while True:
        print_menu()
        option = input("Enter an option: ")

        if (option == '1'):
            print_student_menu()
        elif (option == '2'):
            print_course_menu()
        elif (option == 'q'):
            break
        else:
            print("Not a valid option")
    # student = Student()

    # student.test()