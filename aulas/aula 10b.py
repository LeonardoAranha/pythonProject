"""nome = str(input('Qual o seu nome? ')).strip().title()
if nome == 'Leonardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}')"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print(f'A sua média foi {n:.1f}')
if n >= 6.0:
    print('Sua média foi boa!!')
else:
    print('Sua média não foi tão boa.')
print('PARABÉNS' if n >= 6 else 'Estude mais!!')