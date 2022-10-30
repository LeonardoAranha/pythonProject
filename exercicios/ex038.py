num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 == num2:
    print('Não há maior, os dois são iguais')
elif num1 > num2:
    maior = num1
    menor = num2
    print(f'O maior valor é {maior} e o menor é {menor}')
elif num2 > num1:
    maior = num2
    menor = num1
    print(f'O maior valor é {maior} e o menor é {menor}')
