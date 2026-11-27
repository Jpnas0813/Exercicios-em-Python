# Calculadora de gorjeta e divisão de conta.

valor_conta = float(input('Qual o valor da conta? R$'))
numero_pessoas = int(input('Qual o número de pessoas para dividir a conta? '))
gorjeta = float(input('Qual a porcentagem da gorjeta? '))

print('-' * 50)
if valor_conta > 200:
    desconto = valor_conta * 0.05
    conta_desconto = valor_conta - desconto
    valor_gorjeta = conta_desconto * (gorjeta / 100)
    conta_total = conta_desconto + valor_gorjeta
    conta_dividida = conta_total / numero_pessoas
    print('Valor conta: R${:.2f}'.format(valor_conta))
    print('Número de pessoas: {}'.format(numero_pessoas))
    print('Desconto aplicado: R${:.2f}'.format(desconto))
    print('Total com gorjeta: R${:.2f}'.format(conta_total))
    print('Valor por pessoa: R${:.2f}'.format(conta_dividida))

else:
    valor_gorjeta = valor_conta * (gorjeta / 100)
    conta_total = valor_conta + valor_gorjeta
    conta_dividida = conta_total / numero_pessoas
    print('Valor conta: R${:.2f}'.format(valor_conta))
    print('Número de pessoas: {}'.format(numero_pessoas))
    print('Total com gorjeta: R${:.2f}'.format(conta_total))
    print('Valor por pessoa: R${:.2f}'.format(conta_dividida))

print('-' * 50)
