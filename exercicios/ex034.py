salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    salario = salario*10/100+salario
else:
    salario = salario*15/100+salario
print(f"Com o aumento o funcionário irá receber {salario}")
