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


class SuperUser(User):

    def __init__(self, username, password):
        super().__init__(username, password)  # Chama o construtor de User para atribuir o ID

    def register_super_user(self, super_user_username, super_user_password):
        from view import user_manager
        user_manager.add_super_user(super_user_username, super_user_password)

    def register_teacher(self, teacher_username, teacher_password):
        from view import user_manager
        user_manager.add_teacher(teacher_username, teacher_password)

    def __str__(self):
        return f"SuperUser(ID: {self.id}, username: {self.username}, password: {self.password})"