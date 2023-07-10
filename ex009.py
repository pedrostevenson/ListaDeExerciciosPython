temperatura_fahrenheit_str = input('Temperatura em Fahrenheit: ')

try:
    temperatura_fahrenheit_float = float(temperatura_fahrenheit_str)

    converter_celsius = 5 * ((temperatura_fahrenheit_float - 32) / 9)
    print(f'Temperatura em Celsius: {converter_celsius:.1f}C°')
except:
    print('Informe a temperatura em números.')