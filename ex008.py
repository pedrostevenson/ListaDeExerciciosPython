dinhero_por_hora_str = input('Informe o valor de R$ por hora: R$')
horas_trabalhadas_mês_str = input('Informe quantas hora você trabalha por mês: ')

try:
    dinhero_por_hora_float = float(dinhero_por_hora_str)
    horas_trabalhadas_mês_float = float(horas_trabalhadas_mês_str)

    total_salario = dinhero_por_hora_float * horas_trabalhadas_mês_float

    print(f'Seu salário é de R${total_salario:.2f}')
except:
    print('Informe os valores pedidos em números.')


