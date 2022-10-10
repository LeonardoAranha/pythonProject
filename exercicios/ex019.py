import random
print('sorteio da sala 8b')
n1 = str(input('primeiro aluno: ')).title()
n2 = str(input('segundo aluno: ')).title()
n3 = str(input('terceiro aluno: ')).title()
n4 = str(input('quarto aluno: ')).title()
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido}')