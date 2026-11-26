# Jogo de adivinhação
import random

chute = int(input('Qual número você acha que pensei? Entre 1 e 5? '))
numero = random.randint(1, 5)

if chute >= 1 and chute <=5:
    if chute == numero:
        print('Meu Deus! Você acertou! Eu pensei no {} mesmo!'.format(numero))

    else:
        print('Errou!! Eu pensei no {}!!'.format(numero))
else:
    print('Digite um número entre 1 e 5, por favor!')
