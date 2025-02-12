from classes import *
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

while True:
        print("\nWelcome to E-Learning Platform!\nWhat do you wanna do?")
        choose = input("1 - Create, update and manage online courses\n2 - Register, update and manage students\n3 - Interactive learning tools\n4 - Quit\n>>> ")
        
        if choose == "1":
            clear_terminal()

            while True:
                print()
                print("What do you wanna do?")
                action = input("1 - Create a course\n2 - Update a course\n3 - Manage a course\n4 - List courses\n5 - Back\n>>> ")

                if action == "1":
                    clear_terminal()
                    title = input("Enter the course title: ")
                    teacher = input("Enter the teacher's name: ")
                    hours = input("Enter the course hours: ")
                    try:
                        amount_of_classes = int(input("How many classes this course have? "))
                    except ValueError:
                        print("Invalid number of classes! Returning to menu.")
                        continue
                    course_manager.add_course(title, teacher, hours)
                    for current in range(amount_of_classes):
                        title_of_class = input(f"Enter the title of the {current + 1}º class: ")
                        url = input(f"Enter the url of the {current + 1}º class: ")
                        course_manager.add_class(title, title_of_class, url)

                elif action == "2":
                    clear_terminal()
                    old_title = input("Enter the course title to update: ")
                    new_title = input("Enter the new title (leave empty to keep current): ") or None
                    new_hours = input("Enter the new hours (leave empty to keep current): ") or None
                    new_teacher = input("Enter the new teacher (leave empty to keep current): ") or None
                    course_manager.update_course(old_title, new_title, new_hours, new_teacher)

                elif action == "3":
                    clear_terminal()
                    action = input("1 - List classes\n2 - Delete a course\n>>> ")
                    if action == "1":
                        title = input("Enter the course title: ")
                        course_manager.view_classes(title)
                    elif action == "2":
                        title = input("Enter the course title to delete: ")
                        course_manager.delete_course(title)

                elif action == "4":
                    clear_terminal()
                    course_manager.list_courses()

                elif action == "5":
                    clear_terminal()
                    break

                else:
                    clear_terminal()
                    print("OPS! Invalid option!\n")
                
        elif choose == "2":
            clear_terminal()
            
            while True:
                print()
                print("What do you wanna do?")
                action0 = input("1 - Manage a student\n2 - Track student progress\n3 - List students\n4 - Back\n>>> ")

                if action0 == "1":
                    clear_terminal()
                    action = input("1 - Register a student\n2 - Update a student\n>>> ")
                    if action == "1":
                        clear_terminal()
                        name = input("Enter the student's name: ")
                        student_id = input("Enter the student's ID: ")
                        age = input("Enter the student's age: ")
                        course_title = input("Enter the student's course: ")
                        paid = input("The student have access to paid content? ")
                        student_manager.add_student(name, student_id, age, course_title, paid)
                    elif action == "2":
                        clear_terminal()
                        name = input("Enter the student's name to update: ")
                        new_name = input("Enter the new name (leave empty to keep current): ")
                        new_age = input("Enter the new age (leave empty to keep current): ")
                        new_course = input("Enter the new course (leave empty to keep current): ")
                        new_paid = input("Enter the new paid condition (leave empty to keep current): ")
                        new_progress = input("Enter the new progress (0-100) (leave empty to keep current): ")
                        student_manager.update_student(name, new_name or None, new_age or None, new_course or None, new_paid or None, new_progress or None)
                    else:
                        clear_terminal()
                        print("OPS! Invalid option!\n")

                elif action0 == "2":
                    clear_terminal()
                    name = input("Enter the student's name: ")
                    student_manager.track_student_progress(name)

                elif action0 == "3":
                    clear_terminal()
                    student_manager.list_students()
                
                elif action0 == "4":
                    clear_terminal()
                    break

                else:
                    clear_terminal()
                    print("OPS! Invalid option!\n")

        elif choose == "3":
            while True:
                print()
                print("What do you wanna do?")
                action = input("1 - Add a quiz\n2 - View quizzes\n3 - Back\n>>> ")
                if action == "1":
                    clear_terminal()
                    title = input("Enter de course title: ")
                    quizzes = int(input("Enter amount of quizzes that you wanna add: "))

                    for current in range(quizzes):
                        question = input(f"Add the {current + 1}º question: ")
                        answer = input(f"Add the {current + 1}º question answer: ")
                        course_manager.add_quiz(title, question, answer)


                elif action == "2":
                    clear_terminal()
                    title = input("Enter de course title: ")
                    course_manager.view_quizzes(title)

                elif action == "3":
                    clear_terminal()
                    break

                else:
                    clear_terminal()
                    print("OPS! Invalid option!\n")
        
        elif choose == "4":
            print("See you soon!")
            break