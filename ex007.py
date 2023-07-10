lado_str = input('Informe o tamanho do lado do quadrado: ')

try:
    lado_float = float(lado_str)
    area_quadrado = lado_float**2

    print(f'Área do quadrado: {area_quadrado}')
    print(f'O dobro da sua área é {area_quadrado * 2}')
except:
    print('Informe apenas números.')