str_nota_1 = input('Primeira nota: ')
str_nota_2 = input('Segunda nota: ')
str_nota_3 = input('Terceira nota: ')
str_nota_4 = input('Quarta nota: ')

try:
    float_nota_1 = float(str_nota_1)
    float_nota_2 = float(str_nota_2)
    float_nota_3 = float(str_nota_3)
    float_nota_4 = float(str_nota_4)

    media = (float_nota_1 + float_nota_2 + float_nota_3 + float_nota_4) / 4

    print(f'Sua média é {media:.1f}')

except:
    print('Digite apenas números.')