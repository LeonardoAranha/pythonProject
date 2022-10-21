nome = input('qual é o seu nome? ').title().strip()
if nome == 'Leonardo':
    print('que nome bonito!!')
elif nome == 'Maria' or 'João' or 'Pedro':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome comum :/')
print(f'Tenha um bom dia {nome}')