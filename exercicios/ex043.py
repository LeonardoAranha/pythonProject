import pygame
peso = float(input('Qual o seu peso: '))
altura = int(input('Qual a sua altura em cm: '))
imc = peso / ((altura * 0.01) * (altura * 0.01))
if imc <= 18.5:
    print(f'Seu IMC é {imc:.0f} e  você está em Baixo Peso, precisa se alimentar melhor!')
elif imc > 18.6 and imc <= 24.9:
    print(f'seu IMC é {imc:.0f} e você está no peso normal!')
elif imc >= 25 and imc <= 29.9:
    print(f'seu IMC é {imc:.0f} e você está com excesso de peso! se exercite mais!')
elif imc >= 30 and imc <= 34:
    print(f'seu IMC é {imc:.0f} e você está obeso, você precisa de exercícios e uma'
          f' dieta mais balanceada. Tome cuidado!')
elif imc > 35:
    print(f'seu IMC é {imc:.0f}, você se qualifica em obesidade extrema, isso pode afetar a sua'
          f' saúde,\né melhor começar a fazer exercícios logo, e melhora essa alimentação ai boi.\n'
          f'\033[30;41mTu vai morrer corno!!\033[m')
    pygame.init()
    pygame.mixer.music.load('barata (ex 043).mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()