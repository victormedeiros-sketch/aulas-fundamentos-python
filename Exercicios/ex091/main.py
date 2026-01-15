# Adicione um método à classe desenvolvida
# no exercício anterior Livro que imprime
# uma descrição do livro no formato:
# “O livro com o titulo X foi escrito pelo autor Y".

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def mostra(self):
        return f'O livro {self.titulo} foi escrito pelo autor {self.autor}'


livro1 = livro('Dom Casmurro', 'Machado de assis')
livro2 = livro('Ensaio sobre a cegueira', 'José Saramago')
livro3 = livro('O hobbit', 'J.R.R. Tolkien')

print(livro1.mostra())
print(livro2.mostra())
print(livro3.mostra())