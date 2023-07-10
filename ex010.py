temperatura_celsius_str = input('Temperatura em Celsius: ')

try:
    temperatura_celsius_float = float(temperatura_celsius_str)
    converter_fahrenheit = (temperatura_celsius_float * 9/5) + 32

    print(f'Temperatura em Fahrenheit: {converter_fahrenheit:.1f}F°')
except:
    print('Informe a temperatura em números.')
    