altura_str = input('Altura em metros: ')

try:
    altura_float = float(altura_str)
    peso_ideal = (72.7 * altura_float) - 58

    print(f'Seu peso ideal é {peso_ideal:.2f}')
except:
    print('Informe seu peso em números apenas.')