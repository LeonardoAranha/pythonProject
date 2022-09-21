dia = int(input('Por quantos dias o cliente ficou com o carro? '))
km = float(input('e quantos Km ele andou? '))
aluguel = (dia*60) + (km*0.15)
print(f'o alguel que ele deve pagar é de R${aluguel:.2f}')
