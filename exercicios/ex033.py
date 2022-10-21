a = int(input('Digite o primeiro número:'))
b = int(input('O segundo: '))
c = int(input('Agora o último: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor número é {menor}')
maior = b
if a > b and a > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"E o maior número é {maior}")
