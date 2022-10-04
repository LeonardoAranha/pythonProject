from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hipo = hypot(co, ca)
print(f'o comprimento da hipotenusa deste triangulo retangulo é : {hipo:.3f}')
