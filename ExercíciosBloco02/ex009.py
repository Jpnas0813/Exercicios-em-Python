# Média de notas com situação do aluno.

n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
n3 = float(input('Qual a terceira nota? '))
media = (n1 + n2 + n3)/3

print('-' * 50)


if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10 : 
    print('Primeira nota: {:.1f}'.format(n1))
    print('Segunda nota: {:.1f}'.format(n2))
    print('Terceira nota: {:.1f}'.format(n3))
    print('Média: {:.1f}'.format(media))

    if media >= 7:
        print('Situação: Aprovado.')

    elif media >= 5:
        print('Situação: Recuperação.')

    else:
        print('Situação: Reprovado.')
else:
    print('Notas inválidas. Use valores de 0 a 10.')

print('-' * 50)
