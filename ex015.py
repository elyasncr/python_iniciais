dias = int(input('Quantos dias você ficou com o carro? '))
km = int(input('Percorreu quantos quilometros? '))
aluguel = (dias * 60)+(km * 0.15)
print('O aluguel a ser pago é: R${}'.format(aluguel))