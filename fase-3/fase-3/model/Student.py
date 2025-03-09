import itertools

class User:
    id_counter = itertools.count(1)  

    def __init__(self, username, password):
        self.id = next(User.id_counter) 
        self.username = username
        self.password = password

    def __str__(self):
        return f"User(ID: {self.id}, username: {self.username}, password: {self.password})"

    def update_account(self, new_username=None, new_password=None):
        if new_username:
            self.username = new_username
            print(f"Usuário atualizado com sucesso para '{self.username}'!")
        if new_password:
            self.password = new_password
            print(f"Senha do usuário '{self.username}' foi alterada com sucesso!")


class Student(User):
    def __init__(self, username, password, age, course, paid, progress = 0):
        super().__init__(username, password)
        self.age = age
        self.course = course
        self.paid = paid
        self.progress = progress

    def update_account(self, new_username=None, new_password=None):
        print(f"Atualizando o estudante: {new_username}, {new_password}")
        super().update_account(new_username, new_password)

    def __str__(self):
        return f"Student(ID: {self.id}, username: {self.username}, age: {self.age}, course: {self.course}, paid: {self.paid})"