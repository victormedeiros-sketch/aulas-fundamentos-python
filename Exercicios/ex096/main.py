# Crie uma classe chamada “Aluno” que
# possua atributos para armazenar o nome e
# as notas de um aluno. Adicione métodos
# para calcular a média das notas e
# verificar a situação do aluno (aprovado
# ou reprovado).


class Aluno:

    @property
    def nome(self):
        return self.__nome


    def __init__(self, nome, *notas):
        self.__nome = nome
        self.__notas = notas


    def calcula_media(self):
        if not self.__notas:
            return 0
        else:
            return sum(self.__notas) / len(self.__notas)


    def situacao(self):
        media = self.calcula_media()
        if media >= 7:
            return 'Aprovado'
        else:
            return 'Reprovado'


aluno1 =  Aluno('Victor', 10,7,7.5,7.8,9,8.2 )
print(f'A media do aluno {aluno1.nome} é {aluno1.calcula_media():.1f}')
print(f'A sua situação é {aluno1.situacao()}')
