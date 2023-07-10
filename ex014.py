peso_str = input('Peso de peixes em quilos: ')

try:
    peso_float = float(peso_str)
    peso_excedido = peso_float - 50
    multa = 4.00 * peso_excedido

    print(f'{peso_float}kg de peixe.')
    print(f'Peso excedido: {peso_excedido:.2f}kg')
    print(f'Valor a pagar por quilo excedido: R${multa:.2f}')
except:
    print('Informe o peso em números.')
