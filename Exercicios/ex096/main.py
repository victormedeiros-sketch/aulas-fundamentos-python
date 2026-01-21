# Crie uma classe chamada “Aluno” que
# possua atributos para armazenar o nome e
# as notas de um aluno. Adicione métodos
# para calcular a média das notas e
# verificar a situação do aluno (aprovado
# ou reprovado).


class Aluno:
    def __init__(self, nome, *notas):
        self.__nome = nome
        self.__notas = list(notas)


    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            print("Erro: O nome não pode estar vazio.")

    def get_notas(self):
        return self.__notas

    def set_notas(self, novas_notas):
        if isinstance(novas_notas, list):
            self.__notas = novas_notas
        else:
            print("Erro: As notas devem ser fornecidas em uma lista.")

    def calcula_media(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def situacao(self):
        resultado_media = self.calcula_media()
        return 'Aprovado' if resultado_media >= 7 else 'Reprovado'



aluno1 = Aluno('Victor', 10, 7, 7.5, 7.8, 9, 8.2)


print(f"Aluno: {aluno1.get_nome()}")


media = aluno1.calcula_media()
print(f"Média: {media:.1f}")
print(f"Situação: {aluno1.situacao()}")


aluno1.set_nome("Gabriel")
print(f"Nome atualizado: {aluno1.get_nome()}")
