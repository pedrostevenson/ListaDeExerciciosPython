metros_str = input('Metros: ')

try:
    metros_float = float(metros_str)
    convercao = metros_float * 100

    print(f'{metros_float}m equivalem a {convercao}cm')
except:
    print('Digite apenas números.')