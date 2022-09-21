frase = 'Curso em Vídeo Python'
'0=C 1=u 2=r 3=s 4=o 5= 6=e 7=m 8= 9=V 10=i 11=d 12=e 13=0 14= ' \
'15=P 16=y 17=t 18=h 19=o 20=n'
#fatiamento (no fatiamento sempre considera a ultima como -1
#no começo, quando ta sem valor significa 0 e no final é sem limite ou seja, vai até o fim
print(frase[:5])
print(frase[13:])
#do 9 até 13 (14-1)
print(frase[9:14])
#pular letras na terceira parte do :
print(frase[9:21:2])
print(frase[9::3])

#Análise
len(frase) #mostra o comprimento
print(frase.count('o')) #mostra quantos 'o' na frase
print(frase.count('o', 0, 13)) #mostra quantos 'o' na frase do 0 até o 12 (13-1)
print(frase.find('deo')) #vai mostrar onde começa p 'deo' que no caso é 11
print(frase.find('Android')) #por não existir a str ele vai mostrar -1
print('Curso' in frase) #existe 'curso' em frase? True (sim)
print('Android' in frase) #existe 'curso' em frase? False (não)

#Transformação
print(frase.replace('Python', 'Android')) #Substitui o Pyhton por Android
print(frase.upper()) #Torna tudo maiúsculo
print(frase.lower()) #Torna tudo minúsculo
print(frase.capitalize()) #Tudo exceto a primeira letra em minúscula
print(frase.title()) #Todas palavras começarão em maiúscula
frase2 = '   Aprenda Python  '
print(frase2.strip()) #strip remove os espaços iniciais e os do final
print(frase2.rstrip()) #r é de right, então strip vai agir só no final (lado direito)
print(frase2.lstrip()) #l é de left, então vai remover só os do começo (lado esquerdo)

#Divisão
print(frase2.split()) #Vai dividir a 'frase' usando os espaços como medida
print('-'.join(frase2)) #vai juntar usando o '-' pra separar as letras
print('-'.join(frase2.split())) #vai juntar usando o '-' pra separar as palavras