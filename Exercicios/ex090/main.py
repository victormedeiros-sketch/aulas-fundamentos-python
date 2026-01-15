# Crie uma classe chamada Livro que tenha
# dois atributos: titulo e autor.
# Instancie três objeto dessa classe e
# imprima os valores dos atributos.

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor




livro1 = livro('Dom Casmurro', 'Machado de assis')
livro2 = livro('Ensaio sobre a cegueira', 'José Saramago')
livro3 = livro('O hobbit', 'J.R.R. Tolkien')

print(livro1.titulo)
print(livro1.autor)
print(livro2.titulo)
print(livro2.autor)
print(livro3.titulo)
print(livro3.autor)









