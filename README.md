# E-Learning Platform
# Classes usadas:
Classe View (Abstract Class): Classe base abstrata para todas as visualizações da plataforma. Fornece métodos comuns para manipulação de usuários e senha;\
Classe EnterView: Responsável pela tela de login, verifica as credenciais e direciona o usuário para a visualização correspondente;\
Classe RegisterView: Gerencia o registro de novos alunos, solicitando informações do usuário e inscrevendo-o em um curso;\
Classe FirstView: Tela inicial que permite ao usuário escolher entre login, registro ou sair do sistema;\
Classe StudentView: Interface para alunos, permitindo acessar aulas, quizzes, fórum e emitir certificados;\
Classe TeacherView: Interface para professores, possibilitando gerenciamento de cursos, alunos, quizzes e fórum;\
Classe SuperUserView: Interface para super usuários (administradores), permitindo gerenciamento de usuários e cursos;\
Classe CourseManager: usado para gerenciar todos os cursos;\
Classe UserManager: usado para gerenciar todos os usuários;\
Classe Student: Cada estudante individual. (Nome do aluno, senha, identificação do aluno, idade do aluno, classe Curso que pertence, progresso do aluno e situação de pagamento do aluno);\
Classe Teacher: Cada professsor individual. (Nome do professor, senha, identificação);\
Classe SuperUser: O usuário que tem aceso a tudo. (Nome do superusuário, senha, identficação);\
Classe Curso: Cada curso individual. (Título do curso, quantidade de horas do curso, professor do curso, uma lista da classes Leasson para assistir do curso, uma lista da classe Quiz, uma lista do fórum do curso);\
Classe Lesson: Aulas que podem ser assistidas no curso. (Título da aula e link da aula);\
Classe Quiz: Cada teste do curso. (Pergunta e resposta);\
Classe Forum: Cada comentário do fórum. (Nome de quem fez o comentário e comentário)\\
# Funções implementadas:
• Course Creation and Management: Instructors can create, update, and manage online courses;\
• Student Enrollment and Tracking: Managing student enrollments and tracking their progress;\
• Interactive Learning Tools: Incorporating quizzes, assignments, and interactive content;\
• Video Streaming: Streaming educational videos with support for various formats (integrado na criação do curso);\
• Discussion Forums and Chat: Facilitating student and instructor interactions through forums and
chat;\
• Certification and Badging: Issuing certificates or badges upon course completion;\
• Analytics and Reporting: Providing detailed analytics on student performance and course
engagement;\
• Content Access Control: Managing access permissions for different types of content;\
• Payment and Subscription Management: Handling course fees, subscriptions, and financial
transactions.\
As the code is being run on the terminal, the mobile compatibility function has been ignored for now
