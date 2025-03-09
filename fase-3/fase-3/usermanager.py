from model.User import *
from model.Teacher import *
from model.Student import *
from model.SuperUser import *
class UserManager:
    def __init__(self):
        self.teacher_list = []  
        self.student_list = []  
        self.super_user_list = []

    def add_student(self, username, password, age, course, paid):
        self.student_list.append(Student(username, password, age, course, paid))
           
    def add_teacher(self, username, password):
        self.teacher_list.append(Teacher(username, password))

    def add_super_user(self, username, password):
        self.super_user_list.append(SuperUser(username, password))
        
    def delete_user(self, username, password):
        for aluno in self.student_list:
            if aluno.username == username and aluno.password == password:
                self.student_list.remove(aluno)
                break
            
        for professor in self.teacher_list:
            if professor.username == username and professor.password == password:
                self.teacher_list.remove(professor)
                break

        for super_user in self.super_user_list:
            if super_user.username == username and super_user.password == password:
                self.super_user_list.remove(super_user)
                break

    def list_users(self):
        for usuario in self.student_list:
            print(f'{usuario}')
        for usuario in self.teacher_list:
            print(f'{usuario}')
        for usuario in self.super_user_list:
            print(f'{usuario}')

    def update_account(self, id, username, password, new_username=None, new_password=None):
        for aluno in self.student_list:
            if aluno.id == id and aluno.username == username and aluno.password == password:
                aluno.update_account(new_username, new_password)
                break
            
        for professor in self.teacher_list:
            if professor.id == id and professor.username == username and professor.password == password:
                professor.update_account(new_username, new_password)
                break

        for super_user in self.super_user_list:
            if super_user.id == id and super_user.username == username and super_user.password == password:
                super_user.update_account(new_username, new_password)
                break
            
    def filter_students(self, course):
        for student in self.student_list:
            if student.course == course:
                print(f'{student}')
            else:
                print("No students found")
                
    def get_progress(self, username):
        for student in self.student_list:
            if student.username == username:
                print(f"Current progress: {student.progress}%")
            else:
                print("Student not found!")
                
    def update_progress(self, username, new_progress):
        for student in self.student_list:
            if student.username == username:
                student.progress = new_progress
            else:
                print("Student not found!")
                
    def get_course(self, username):
        for student in self.student_list:
            if student.username == username:
                return student.course
            else:
                print("Student not found!")
                
    def get_user(self, username, password):
        for aluno in self.student_list:
            if aluno.username == username and aluno.password == password:
                return aluno
            
        for professor in self.teacher_list:
            if professor.username == username and professor.password == password:
                return professor

        for super_user in self.super_user_list:
            if super_user.username == username and super_user.password == password:
                return super_user