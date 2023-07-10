tamanho_area_str = input('Tamanho da área a ser pintada em metros quadrados: ')
valor_lata_tinta = 80
litros_da_lata_tinta = 18

try:
    tamanho_area_float = float(tamanho_area_str)
    tamanho_area_float **= 2
    litros_total = tamanho_area_float / 3
    total_de_latas = litros_total / 18
    valor_total = total_de_latas * 80


    print(f'Quantidades de latas a serem compradas: {total_de_latas:.0f}')
    print(f'Preço total: R${valor_total:.2f}')
except:
    print('Digite apenas números.')
