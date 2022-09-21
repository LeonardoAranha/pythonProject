nome = input('digite seu nome completo: ')
nome = nome.title()
dividido = nome.split()
print(f'seu primeiro nome é {dividido[0]}, e o último {dividido[-1]}')