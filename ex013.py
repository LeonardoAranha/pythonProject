salário = float((input('qual salário do funcionário atualmente?  ')))
aumento = salário + (salário*15/100)
print('seu salário de {:.2f} com um aumento de 15% será: {:.2f}'.format(salário, aumento))
print(f'o seu funcionário receberá {aumento} com o aumento de 15%')
