from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from datetime import datetime
from reportlab.lib import colors
import PyPDF2

class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, title, teacher, hours):
        if title in self.courses:
            print("This course is already registered!")
        else:
            self.courses[title] = Course(title, hours, teacher)
            print(f"{title} has been successfully registered")

    def delete_course(self, title):
        if title in self.courses:
            del self.courses[title]
            print(f"Course '{title}' deleted successfully!")
        else:
            print("Course not found!")

    def update_course(self, old_title, new_title=None, new_hours=None, new_teacher=None):
        if old_title in self.courses:
            course = self.courses[old_title]
            if new_title:
                self.courses[new_title] = self.courses.pop(old_title)
                course.title = new_title
            if new_hours:
                course.hours = new_hours
            if new_teacher:
                course.teacher = new_teacher
            print(f"'{old_title}' has been updated successfully!")
        else:
            print("Course not found!")

    def add_class(self, course_title, class_title, url):
        if course_title in self.courses:
            lesson = Lesson(class_title, url)
            self.courses[course_title].classes.append(lesson)
            print(f"Class '{class_title}' added to course '{course_title}'")
        else:
            print("Course not found!")

    def view_classes(self, course_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            if not course.classes:
                print("No classes found!")
            else:
                print(f"Classes in {course.title}:")
                for lesson in course.classes:
                    print(lesson.list_class())
        else:
            print("Course not found!")

    def remove_class(self, course_title, class_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            course.classes = [lesson for lesson in course.classes if lesson.title != class_title]
            print(f"Class '{class_title}' removed successfully!")
        else:
            print("Course not found!")

    def add_quiz(self, course_title, question, answer):
        if course_title in self.courses:
            quiz = Quiz(question, answer)
            self.courses[course_title].quizzes.append(quiz)
            print(f"Quiz added to course '{course_title}'")
        else:
            print("Course not found!")

    def view_quizzes(self, course_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            if not course.quizzes:
                print("No quizzes found!")
            else:
                print(f"Quizzes in {course.title}:")
                for quiz in course.quizzes:
                    print(quiz.list_quiz())
        else:
            print("Course not found!")

    def remove_quiz(self, course_title, question):
        if course_title in self.courses:
            course = self.courses[course_title]
            course.quizzes = [quiz for quiz in course.quizzes if quiz.question != question]
            print(f"Quiz '{question}' removed successfully!")
        else:
            print("Course not found!")

    def list_courses(self):
        if not self.courses:
            print("No courses available!")
        else:
            for course in self.courses.values():
                print(f"Title: {course.title}, Teacher: {course.teacher}, Hours: {course.hours}")

    def add_comment_in_forum(self, course_title, name, comment):
        if course_title in self.courses:
            new_comment = Forum(name, comment)
            self.courses[course_title].forum.append(new_comment)
            print(f"Comment added to forum of '{course_title}'")
        else:
            print("Course not found!")

    def view_comments_in_forum(self, course_title):
        if course_title in self.courses:
            course = self.courses[course_title]
            if not course.forum:
                print("No comments found!")
            else:
                print(f"Forum in {course.title}:")
                for comment in course.forum:
                    print(comment.list_comment())
        else:
            print("Course not found!")

    def remove_comment(self, course_title, name, comment):
        if course_title in self.courses:
            course = self.courses[course_title]
            course.forum = [c for c in course.forum if c.name != name or c.comment != comment]
            print(f"Comment from '{name}' removed successfully!")
        else:
            print("Course not found!")

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id, age, course_title, paid, course_manager):
        if name in self.students:
            print("This student is already registered!")
        else:
            if course_title not in course_manager.courses:
                print("Course not found!")
                return
            course = course_manager.courses[course_title]
            self.students[name] = Student(name, student_id, age, course, paid)
            print(f"{name} has been successfully registered")

    def update_student(self, name, new_name=None, new_age=None, new_course=None, new_paid = None, new_progress = None):
        if name in self.students:
            student = self.students[name]
            if new_progress:
                student.progress = new_progress
            if new_name:
                self.students[new_name] = self.students.pop(name)
                student.name = new_name
            if new_age:
                student.age = new_age
            if new_paid:
                student.paid = new_paid
            if new_course:
                if new_course not in course_manager.courses:
                    print("Course not found!")
                    return
                student.course = course_manager.courses[new_course]
            print(f"Student '{name}' has been updated!")
        else:
            print("Student not found!")

    def track_student_progress(self, name):
        if name in self.students:
            print(f"Current progress: {self.students[name].progress}%")
        else:
            print("Student not found!")

    def list_students(self):
        if not self.students:
            print("No students registered!")
        else:
            for student in self.students.values():
                print(f"Name: {student.name}, ID: {student.id}, Course: {student.course.title}")

    def analytics_and_reporting(self, name):
        if name in self.students:
            print(f"Student: {name}, id: {self.students[name].id}, age: {self.students[name].age}, course: {self.students[name].course.title}, progress: {self.students[name].progress}, paid condition: {self.students[name].paid}!")
        else:
            print("Student not found!")
        
    def payment_condition(self, name):
        if name in self.students:
            print(f"Paid condition: {self.students[name].paid}!")
        else:
            print("Student not found!")

    def check_course_access(self, name, course):
        if name in student_manager.students:
            student_courses = student_manager.students[name].course
            if isinstance(student_courses, list) and course in student_courses:
                print("The student has access to this course!")
            elif course == student_courses:
                print("The student has access to this course!")
            else:
                print("The student has not access to this course")
        else:
            print("Student not found!")

    def get_student(self, name):
        return self.students.get(name, None)


class Student:
    def __init__(self, name, student_id, age, course, paid, progress=0):
        if not isinstance(course, Course):
            raise ValueError("Course not found! Student registration failed.")
        self.name = name
        self.id = student_id
        self.age = age
        self.course = course
        self.progress = progress
        self.paid = paid

class Course:
    def __init__(self, title, hours, teacher):
        self.title = title
        self.hours = hours
        self.teacher = teacher
        self.classes = []
        self.quizzes = []
        self.forum = []

class Lesson:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def list_class(self):
        return f"Class: {self.title} - {self.url}"

class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def list_quiz(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"

class Forum:
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

    def list_comment(self):
        return f"{self.name}: {self.comment}"
    
course_manager = CourseManager()
student_manager = StudentManager()

def fill_and_generate_certificate(student_manager):
    name = input("Enter the student's name: ")
    student = student_manager.get_student(name)
    if student is None:
        print("Student not found!")
        return None
    
    course_name = student.course.title
    student_id = student.id
    date = datetime.now().strftime("%B %d, %Y")
    
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    c.setFillColor(colors.lightgrey)
    c.rect(30, 550, 550, 250, fill=1)
    c.setFillColor(colors.black)
    c.rect(30, 550, 550, 250, fill=0)
    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 800, "Certificate of Completion")
    
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 740, f"Student: {name}")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 710, f"Course: {course_name}")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 680, f"Student ID: {student_id}")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 650, f"Date: {date}")
    
    c.line(100, 600, 500, 600)
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(100, 590, "Instructor's Signature")
    
    c.save()
    packet.seek(0)
    
    output_pdf = PyPDF2.PdfWriter()
    new_pdf = PyPDF2.PdfReader(packet)
    page = new_pdf.pages[0]
    output_pdf.add_page(page)
    
    output_filename = f"{name}_certificate_filled.pdf"
    
    with open(output_filename, "wb") as output_file:
        output_pdf.write(output_file)
    
    print(f"Certificate generated successfully: {output_filename}")
    return output_filename