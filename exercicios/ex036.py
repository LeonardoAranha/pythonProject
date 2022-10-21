casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto você recebe no mês? '))
anos = int(input('Em quantos anos você planeja pagar?'))
prest = casa/(anos*12)
if prest < salario*30/100:
    print('Parabéns seu empréstimo imobiliário foi aprovado!')
else:
    print('Que pena, não foi possível aprovar seu empréstimo.')