kmh = float(input('Digite quantos KmH você estava: '))
if kmh > 80:
    print(f'HAHA!!! Você foi multado! deverá pagar R${(kmh-80)*7:.2f}')
else:
    print('Você não foi multado!')
