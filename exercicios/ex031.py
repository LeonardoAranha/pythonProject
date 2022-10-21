'''km = float(input('De quantos Km será a viagem? '))
if km <= 200:
    preço = km*0.5
else:
    preço = km*0.45
print(f'Sua viagem ira custar R${preço:.2f}')''' #primeiro jeito de fazer e o jeito que fiz sozinho
km = float(input('De quantos Km será sua viagem? '))
preço = km*0.5 if km<=200 else km*0.45
print(f'Sua viagem irá custar R${preço:.2f}') #jeito simplificado
