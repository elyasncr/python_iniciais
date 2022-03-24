real = float(input('Quanto de dinheiro você tem na carteira? R$'))
# estamos utilizando a cotação do dolar no dia 23/02/2022
dolar = real/4.83
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))