numero_1_str = input('Digite um número inteiro: ')
numero_2_str = input('Digite outro número inteiro: ')
numero_3_str = input('Digite um número real: ')

try:
    numero_1_int = int(numero_1_str)
    numero_2_int = int(numero_2_str)
    numero_3_float = float(numero_3_str)

    print((numero_1_int * 2) * (numero_2_int / 2))
    print((numero_1_int * 3) + numero_3_float)
    print(f'{numero_3_float**3:.2f}')
except:
    print(
        f'Digite apenas números inteiros nas duas primeiras opções '
        f'e um número real na terceira.'
)
    