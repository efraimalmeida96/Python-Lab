class Aluno:

    def __init__(self, nome,):
        self.nome = nome
        self.notas = []

    def add_notas(self, notas):
        self.notas.append(notas)
        return self.notas

    def media(self):
        
        soma = 0
        for nota in self.notas:
            soma += nota
        media = soma / 2

        if media >= 7:
            print('Aprovado')
        if 5 < media <= 6:
            print('Recuperação')
        if media < 5:
            print('Reprovado')



aluno  = Aluno('Efraim')
aluno.add_notas(10)
aluno.add_notas(8)
aluno.media()