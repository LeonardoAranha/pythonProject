preco = float(input('qual o preço do produto? '))
avista = preco - (preco * 5 / 100)
taxa = preco * 5 / 100
print(f'os valores com descontos e taxas ficam:\n________________________ \n'
      f' no dinheiro ou débito:\n {avista:.2f}\n crédito:\n 1x  {preco:.2f} - {preco:.2f}\n 2x  {preco+taxa:.2f}'
      f' - {(preco+taxa)/2:.2f}\n 3x  {preco+taxa*2:.2f} - {(preco+taxa*2)/3:.2f}\n 4x  {preco+taxa*3:.2f} - '
      f'{(preco+taxa*3)/4:.2f}\n 5x  {preco+taxa*4:.2f} - {(preco+taxa*4)/5:.2f}\n 6x  {preco+taxa*5:.2f} - '
      f'{(preco+taxa*5)/6:.2f}\n 7x  {preco+taxa*6:.2f} - {(preco+taxa*6)/7:.2f}\n 8x  {preco+taxa*7:.2f} - '
      f'{(preco+taxa*7)/8:.2f}\n 9x  {preco+taxa*8:.2f} - {(preco+taxa*8)/9:.2f}\n 10x {preco+taxa*9:.2f} - '
      f'{(preco+taxa*9)/10:.2f}\n 11x {preco+taxa*10:.2f} - {(preco+taxa*10)/11:.2f}\n 12x {preco+taxa*11:.2f}'
      f' - {(preco+taxa*11)/12:.2f}')
