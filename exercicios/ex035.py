l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l3 + l2 and l2 < l3 + l1 and l3 < l1 + l2:
    print('Os segmento acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')