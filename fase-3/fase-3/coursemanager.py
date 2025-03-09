class CourseManager:
    def __init__(self):
        self.courses = {}

    def add_course(self, title, teacher, hours, ispaid):
        if title in self.courses:
            print("This course is already registered!")
        else:
            self.courses[title] = Course(title, hours, teacher, ispaid)

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

    def list_courses(self, student_paid_condition, teacher = None):
        if not self.courses:
            print("No courses available!")
        elif student_paid_condition == True:
            for course in self.courses.values():
                if teacher:
                    if course.teacher == teacher:
                        print(f"Title: {course.title}, Teacher: {course.teacher}, Hours: {course.hours}")
                else:
                    print(f"Title: {course.title}, Teacher: {course.teacher}, Hours: {course.hours}")
        else:
            for course in self.courses.values():
                if course.paid == False:
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

class Course:
    def __init__(self, title, hours, teacher, paid):
        self.title = title
        self.hours = hours
        self.teacher = teacher
        self.paid = paid
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