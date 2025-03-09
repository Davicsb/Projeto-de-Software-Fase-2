from abc import ABC, abstractmethod
from model.User import *
from coursemanager import *
from usermanager import *
from certificate import *
import os
from colorama import init, Fore, Back, Style
from getpass import getpass

# Inicializando o colorama
init(autoreset=True)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

user_manager = UserManager()
course_manager = CourseManager()
course_manager.add_course("Java", "Davi", 100, True)
course_manager.add_course("Python", "Davi", 100, False)
user_manager.add_student("Davi", "estudante", "00", "Java", True)
user_manager.add_student("Mariana", "1234", "00", "Python", False)
user_manager.update_progress("Mariana", "100")
user_manager.add_teacher("Davi", "professor")
user_manager.add_super_user("adm", "adm")

class View(ABC):
    def check_password(self, username, password):
        print(f"Checking password for {username} {password}")
        for user_list in [user_manager.teacher_list, user_manager.student_list, user_manager.super_user_list]:
            for user in user_list:
                if user.username == username and user.password == password:
                    return user
        return None
    
    def get_user_type(self, user):
        for userType in user_manager.teacher_list:
            if user.id == userType.id and user.username == userType.username and user.password == userType.password:
                return TeacherView()
        for userType in user_manager.student_list:
            if user.id == userType.id and user.username == userType.username and user.password == userType.password:
                return StudentView()
        for userType in user_manager.super_user_list:
            if user.id == userType.id and user.username == userType.username and user.password == userType.password:
                return SuperUserView()
        return None
    
    def get_username(self, user_list, user_id):
        for user in user_list:
            if user.id == user_id:
                return user.username
            else:
                return False
 
    def update_user(self, username, password):
        user_id = self.check_password(username, password).id
        if user_id:
            new_username = input(Fore.GREEN + "Enter the new username (leave empty to keep current): ") or None
            new_password = input(Fore.GREEN + "Enter the new password (leave empty to keep current): ") or None
            print(f"{user_id} acabou de receber os dados para atualizar: {new_username} {new_password}\n")
            user_manager.update_account(user_id, username, password, new_username, new_password)
        else:
            choice = input(Fore.RED + "Incorrect password!\n1 - Try again.\n2 - Back\n>>> ")
            match choice:
                case "1":
                    self.update_teacher()
                case "2":
                    self.view()

    @abstractmethod
    def view(self):
        pass

class EnterView(View):
    def view(self):
        print(Fore.CYAN + "Welcome to E-Learning Platform login!")
        username = input(Fore.YELLOW + "Enter your name: ")
        password = getpass(Fore.YELLOW + "Enter your password: ")
        user = self.check_password(username, password)
        if user:
            user_type = self.get_user_type(user)
            print(user)
            if user_type:
                print(Fore.GREEN + f"{user_type}")
                user_type.view(user.id)
            else:
                print(Fore.RED + "Invalid Id!")
                FirstView().view()
        else:
            choice = input(Fore.RED + "Incorrect password!\n1 - Try again.\n2 - Back\n>>> ")
            match choice:
                case "1":
                    self.view()
                case "2":
                    FirstView().view()

class RegisterView(View):
    def view(self):
        print(Fore.CYAN + "Welcome to the register view!")
    
        username = input(Fore.YELLOW + "Enter your username: ")
        password = getpass(Fore.YELLOW + "Enter your password: ")
        age = input(Fore.YELLOW + "Enter your age: ")
        
        paid = input(Fore.YELLOW + "Do you want to pay for paid courses?\n1 - Yes\n2 - No\n>>>  ")
        paid = self.option_error(["1", "2"], paid) 
        paid = paid == "1"

        clear_terminal()
        print(Fore.GREEN + "You're almost there. Here is the list of available courses in your plan:")
        course_manager.list_courses(paid, None)
        
        course_title = input(Fore.YELLOW + "Enter the name of the course that you want to enroll in: ")
        while course_title not in course_manager.courses:
            course_title = input(Fore.RED + "Invalid course. Please enter the course title again: ")
        course = course_manager.courses[course_title]

        user_manager.add_student(username, password, age, course, paid)
    
        clear_terminal()
        print(Fore.GREEN + "Congrats! You're registered on our platform!")
        EnterView().view()

class FirstView(View):
    def view(self):
        while True:
            print(Fore.CYAN + "Welcome to E-Learning Platform!\nWhat do you want to do?")
            choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Enter.\n2 - Register.\n>>> ")
            match choice:
                case "1":
                    clear_terminal()
                    EnterView().view()
                    break
                case "2":
                    clear_terminal()
                    RegisterView().view()
                    break
                case "0":
                    exit()
                case _:
                    print(Fore.RED + "Invalid option! Please try again\n")

class StudentView(View):
    def view(self, user_id):
        username = None
        for student in user_manager.student_list:
            if student.id == user_id:
                username = student.username
                break
        
        print(Fore.GREEN + f"Welcome {username} to student dashboard! What you wanna do?")
        choice = input(Fore.YELLOW + "1 - Update account.\n2 - View course lessons\n3 - View quizzes\n4 - Enter Forum\n5 - Emit certificate.\n6 - Quit.\n>>> ")
        
        match choice:
            case "1":
                self.update_user(user_id)
            case "2":
                print(Fore.GREEN + "Viewing lessons for the course...")
                course_manager.view_classes(user_manager.get_course(self.get_username(user_manager.student_list, user_id)))
                self.view(user_id)
                
            case "3":
                print(Fore.GREEN + "Viewing quizzes...")
                course_manager.view_quizzes(user_manager.get_course(self.get_username(user_manager.student_list, user_id)))
                self.view(user_id)
                
            case "4":
                print(Fore.GREEN + "Entering forum...")
                self.forum(user_id)
                
            case "5":
                username = input("Confirm your username: ")
                password = getpass("Confirm your password: ")
                user = user_manager.get_user(username, password)
                if user.progress == "100":
                    fill_and_generate_certificate(user)
                else:
                    print(Fore.RED + "You are not able to emit your certificate!")
                self.view(user_id)
                
            case "6":
                print(Fore.GREEN + "Goodbye!")
                FirstView().view()
            case _:
                print(Fore.RED + "Invalid option! Please try again")
                self.view(user_id)
    
    def forum(self, user_id):
        action = input("0 - Back.\n1 - View fórum.\n2 - Add comment.\n>>> ")
        match action:
            case "0":
                self.view(user_id)
                
            case "1":
                course_manager.view_comments_in_forum(user_manager.get_course(self.get_username(user_manager.student_list, user_id)))
                self.forum(user_id)
            
            case  "2":
                comment = input("Enter your comment: ")
                course_manager.add_comment_in_forum(user_manager.get_course(self.get_username(user_manager.student_list, user_id)), self.get_username(user_manager.teacher_list, user_id), comment)
                self.forum(user_id)
            
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.forum(user_id)
    
    def update_user(self, user_id):
        password = getpass(Fore.YELLOW + "Enter your current password: ")
        if self.check_password(user_id, password):
            new_username = input(Fore.GREEN + "Enter the new username (leave empty to keep current): ") or None
            new_password = input(Fore.GREEN + "Enter the new password (leave empty to keep current): ") or None
            new_age = input(Fore.GREEN + "Enter the new age (leave empty to keep current): ") or None
            new_paid = input(Fore.GREEN + "Enter the new paid condition (leave empty to keep current): ") or None
            new_course = input(Fore.GREEN + "Enter the new course (leave empty to keep current): ") or None
            user_manager.update_account(user_id, new_username, new_password, new_age, new_course, new_paid)

        else:
            choice = input(Fore.RED + "Incorrect password!\n0 - to force Stop the System" + Fore.YELLOW + "1 - Try again.\n2 - Back\n>>> " + Style.RESET_ALL)
            match choice:
                case "0":
                    print(Fore.RED + "System out\n")
                    exit()
                case "1":
                    self.update_user()
                case "2":
                    self.view(user_id)
        self.view(user_id)

class TeacherView(View):
    def view(self, user_id):
        username = None
        for teacher in user_manager.teacher_list:
            if teacher.id == user_id:
                username = teacher.username
                break
            
        clear_terminal()
        print(Fore.GREEN + f"Welcome {username} to teacher dashboard! What you wanna do?")
        choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Update account.\n2 - Manage your courses.\n3 - Manage your students.\n4 - Quit\n>>> ")
        match choice:
            case "0":
                print(Fore.RED + "System out\n")
                exit()
            case "1":
                self.update_user(user_id)
            case "2":
                print(Fore.GREEN + "Managing courses...")
                self.manage_courses(user_id)
                
            case "3":
                print(Fore.GREEN + "Viewing your students...")
                self.manage_students(user_id)
            case "4":
                print(Fore.GREEN + "Goodbye\n")
                FirstView().view()
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.view(user_id)
    
    def manage_students(self, user_id):
        action = input(Fore.YELLOW + "0 - Back.\n1 - List your students.\n2 - Track student progress.\n>>> ")
        match action:
            case "0":
                self.view(user_id)
            
            case "1":
                course = input("Which course do you want to filter: ")
                user_manager.filter_students(course)
                self.manage_students(user_id)
            
            case "2":
                self.track_progress(user_id)
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_courses(user_id)
    
    def track_progress(self, user_id):
        action = input(Fore.YELLOW + "0 - Back.\n1 - View progress.\n2 - Update progress.\n>>> ")
        match action:
            case "0":
                self.manage_students(user_id)
                
            case "1":
                name = input("Enter the student's username: ")
                user_manager.get_progress(name)
                self.track_progress(user_id)
            
            case "2":
                name = input("Enter the student's username: ")
                new_progress = input("Enter the new progress: ")
                user_manager.update_progress(name, new_progress)
                self.track_progress(user_id)
    
    def manage_courses(self, user_id):
        action = input(Fore.YELLOW + "0 - Back.\n1 - List your courses.\n2 - Update your courses.\n3 - Quizzes.\n4 - Fórum\n>>> ")
        match action:
            case "0":
                self.view(user_id)
            
            case "1":
                clear_terminal()
                course_manager.list_courses(True, self.get_username(user_manager.teacher_list, user_id))
                self.manage_courses(user_id)
            
            case "2":
                clear_terminal()
                old_title = input("Enter the course title to update: ")
                new_title = input("Enter the new title (leave empty to keep current): ") or None
                new_hours = input("Enter the new hours (leave empty to keep current): ") or None
                new_teacher = input("Enter the new teacher (leave empty to keep current): ") or None
                course_manager.update_course(old_title, new_title, new_hours, new_teacher)
                self.manage_courses(user_id)
                
            case "3":
                self.quizzes(user_id)
            
            case "4":
                self.forum(user_id)
            
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_courses(user_id)
                
            
    def quizzes(self, user_id):
        action = input("0 - Back.\n1 - View quizzes.\n2 - Add quizzes\n3 - Delete a quiz.\n>>> ")
        match action:
            case "0":
                self.manage_courses(user_id)
                
            case "1":
                title = input("Enter the course title: ")
                course_manager.view_quizzes(title)
                self.quizzes(user_id)
            
            case  "2":
                title = input("Enter the course title: ")
                amount_of_quizzes = int(input("How manny quizzes do you wanna add: "))
                for i in range(amount_of_quizzes):
                    quiz = input("Enter the question: ")
                    answer = input("Enter the quiz answer: ")
                    course_manager.add_quiz(title, quiz, answer)
                self.quizzes(user_id)
            
            case "3":
                title = input("Enter the course title: ")
                question = input("Enter the question that youn wanna delete: ")
                course_manager.remove_quiz(title, question)
                self.quizzes
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.quizzes(user_id)
                
    def forum(self, user_id):
        action = input("0 - Back.\n1 - View fórum.\n2 - Add comment.\n3 - Delete a comment.\n>>> ")
        match action:
            case "0":
                self.manage_courses(user_id)
                
            case "1":
                title = input("Enter the course title: ")
                course_manager.view_comments_in_forum(title)
                self.forum(user_id)
            
            case  "2":
                title = input("Enter the course title: ")
                comment = input("Enter your comment: ")
                course_manager.add_comment_in_forum(title, self.get_username(user_manager.teacher_list, user_id), comment)
                self.forum(user_id)
            
            case "3":
                title = input("Enter the course title: ")
                username = input("Enter the username of the comment: ")
                comment = input("Enter the comment that you wanna delete: ")
                course_manager.remove_comment(title, username, comment)
            
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.forum(user_id)

    def update_user(self, user_id):
        username = input(Fore.YELLOW + "Enter your current username: ")
        password = getpass(Fore.YELLOW + "Enter your current password: ")
        super().update_user(username, password)
        self.view(user_id)

class SuperUserView(View):
    def view(self, user_id):
        username = None
        for super_user in user_manager.super_user_list:
            if super_user.id == user_id:
                username = super_user.username
                break
        
        clear_terminal()
        print(Fore.GREEN + f"Welcome {username} to super user view! What you wanna do?")
        choice = input(Fore.RED + "0 - To force Stop the system\n" + Fore.YELLOW + "1 - Manage users.\n2 - Manage courses.\n3 - Quit.\n>>> ")
        match choice:
            case "0":
                print(Fore.RED + "System out\n")
                exit()
                
            case "1":
                self.manage_users(user_id)
                
            case "2":
                self.manange_courses(user_id)
                
            case "3":
                print(Fore.GREEN + "Goodbye\n")
                FirstView().view()
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.view(user_id)

    def update_user(self, user_id):
        password = getpass(Fore.YELLOW + "Enter your current password: ")
        super().update_user(user_id, password)
        self.view(user_id)
        
    def manage_users(self, user_id):
        print(Fore.GREEN + "Managing users...")
        action = input(Fore.YELLOW + "0 - Back.\n1 - List users.\n2 - Delete a user.\n>>> ")
        match action:
            case "0":
                clear_terminal()
                self.view(user_id)
            
            case "1":
                clear_terminal()
                user_manager.list_users()
                self.manage_users(user_id)
                
            case "2":
                clear_terminal()
                username = input(Fore.YELLOW + "Please confirm your usename: ")
                password = getpass(Fore.YELLOW + "Please confirm your password: ")
                if self.check_password(username, password):
                    user_username = input("Enter the user username that you wanna delete: ")
                    user_password = input("Enter the user password that you wanna delete: ")
                    user_manager.delete_user(user_username, user_password)
                    print(Fore.YELLOW + "{username} has been deleted!")
                    
                else:
                    choice = input(Fore.RED + "Incorrect password!\n0 - to force Stop the System" + Fore.YELLOW + "1 - Try again.\n2 - Back\n>>> " + Style.RESET_ALL)
                    match choice:
                        case "0":
                            print(Fore.RED + "System out\n")
                            exit()
                        case "1":
                            self.manage_users()
                        case "2":
                            self.view(user_id)
                self.view(user_id)
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_users(user_id) 
        
    def manage_courses(self, user_id):
        print(Fore.GREEN + "Managing courses...")
        action = input(Fore.YELLOW + "0 - Back.\n1 - Create a course.\n2 - Update a couse.\n3 - Delete a course.\n4 - List courses\n5 - List leassons\n>>> ")
        match action:
            case "0":
                clear_terminal()
                self.view(user_id)
                
            case "1":
                clear_terminal()
                title = input("Enter the course title: ")
                teacher = input("Enter the teacher's name: ")
                hours = input("Enter the course hours: ")
                amount_of_classes = int(input("How many classes this course have? "))
                paid = bool(input("This course has only paid access? (True or False) "))
                course_manager.add_course(title, teacher, hours, paid)
                for current in range(amount_of_classes):
                    title_of_class = input(f"Enter the title of the {current + 1}º class: ")
                    url = input(f"Enter the url of the {current + 1}º class: ")
                    course_manager.add_class(title, title_of_class, url)
                self.manage_courses(user_id)
                    
            case "2":
                clear_terminal()
                old_title = input("Enter the course title to update: ")
                new_title = input("Enter the new title (leave empty to keep current): ") or None
                new_hours = input("Enter the new hours (leave empty to keep current): ") or None
                new_teacher = input("Enter the new teacher (leave empty to keep current): ") or None
                course_manager.update_course(old_title, new_title, new_hours, new_teacher)
                self.manage_courses(user_id)
                
            case "3":
                clear_terminal()
                title = input("Enter the course title to delete: ")
                course_manager.delete_course(title)
                self.manage_courses(user_id)
                
            case "4":
                clear_terminal()
                course_manager.list_courses(True, None)
                self.manage_courses(user_id)
            
            case "5":
                clear_terminal()
                title = input("Enter the course title: ")
                course_manager.view_classes(title)
                self.manage_courses(user_id)
                
            case _:
                print(Fore.RED + "Invalid option! Please try again\n")
                self.manage_courses(user_id)    

# Executando o sistema
if __name__ == "__main__":
    FirstView().view()