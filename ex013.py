altura_str = input('Altura em metros: ')

try:
    altura_float = float(altura_str)
    peso_ideal_homens = (72.7 * altura_float) - 58
    peso_ideal_mulheres = (62.1 * altura_float) - 44.7

    print(f'Peso ideal para homens: {peso_ideal_homens:.2f}kg')
    print(f'Peso ideal para mulheres: {peso_ideal_mulheres:.2f}kg')
except:
    print('Informe seu peso em números apenas.')