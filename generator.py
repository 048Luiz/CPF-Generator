#  Gerador e Validador de CPF

import random

qtd_cpf = int(input('Quantos CPFs deseja gerar: '))

for _ in range(qtd_cpf):
    digitos_cpf = ''
    for i in range(9):
        digitos_cpf += str(random.randint(0, 9))

    # Primeiro dígito
    contagem_1 = 10
    resultado_1 = 0

    for digito in digitos_cpf:
        resultado_1 += int(digito) * contagem_1
        contagem_1 -= 1

    digito_1 = (resultado_1 * 10 % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0
    digitos_cpf_2 = digitos_cpf + str(digito_1)

    # Segundo dígito
    contagem_2 = 11
    resultado_2 = 0

    for digito in digitos_cpf_2:
        resultado_2 += int(digito) * contagem_2
        contagem_2 -= 1

    digito_2 = (resultado_2 * 10 % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_formatado = f'{digitos_cpf}{digito_1}{digito_2}'

    cpf_valido = cpf_formatado[:9]
    contagem_1 = 10
    resultado_1 = 0

    for digito in cpf_valido:
        resultado_1 += int(digito) * contagem_1
        contagem_1 -= 1

    digito_1 = (resultado_1 * 10 % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0
    cpf_valido += str(digito_1)

    contagem_2 = 11
    resultado_2 = 0

    for digito in cpf_valido:
        resultado_2 += int(digito) * contagem_2
        contagem_2 -= 1

    digito_2 = (resultado_2 * 10 % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_valido += str(digito_2)

    print(f'CPF: {cpf_valido[0:3]}.{cpf_valido[3:6]}.{cpf_valido[6:9]}-{cpf_valido[9:]}')

