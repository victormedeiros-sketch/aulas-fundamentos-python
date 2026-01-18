# Crie uma classe chamada Livro que tenha
# os atributos: titulo, ano, autor e
# disponibilidade. Utilize getters e
# setters para manipular as propriedades.

class Livro:
    def __init__(self, titulo, ano, autor, disponibilidade):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__disponibilidade = disponibilidade

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def autor(self):
        return self.__autor

    @property
    def disponibilidade(self):
        return self.__disponibilidade


livro1 = Livro('Dom Casmurro', 1899, 'Machado de Assis', 'Sim')
print(f'Titulo: {livro1.titulo} | Ano: {livro1.ano} | Autor: {livro1.autor} | Disponivel: {livro1.disponibilidade}')