idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('O atleta está na categoria Mirim')
elif idade > 9 and idade <= 14:
    print('O atelta está na categoria Infantil')
elif idade > 14 and idade <= 18:
    print('O atleta está na categoria Junior')
elif idade >= 19 and idade <= 20:
    print('O atleta está na categoria Senior')
elif idade > 20:
    print('O atleta está na categoria Master')
