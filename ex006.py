raio_str = input('Raio do círculo: ')

try:
    raio_float = float(raio_str)
    area = 3.14 * raio_float**2
    print(
        f'Um círculo com a area de {raio_float}, tem uma área de {area}'
)
except:
    print('Informe apenas números.')