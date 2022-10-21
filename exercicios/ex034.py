salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    print(f'Com o aumento o salário será de R${salario*10/100+salario:.2f}')
else:
    print(f'O salário com o aumento será de R${salario*15/100+salario:.2f}')
