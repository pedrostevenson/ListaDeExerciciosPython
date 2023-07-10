str_numero_1 = input('Digite um número: ')
str_numero_2 = input('Digite outro número: ')

try:
    float_numero_1 = float(str_numero_1)
    float_numero_2 = float(str_numero_2)
    soma = float_numero_1 + float_numero_2
    print(f'{str_numero_1} + {str_numero_2} = {soma}')
except:
    print('Você não digitou um número válido.')