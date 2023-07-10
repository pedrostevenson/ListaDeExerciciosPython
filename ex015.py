dinhero_por_hora_str = input('Quanto você ganha por hora: R$')
horas_trabalhadas_str = input('Horas trabalhadas por mês: ')

try:
    dinhero_por_hora_float = float(dinhero_por_hora_str)
    horas_trabalhadas_float = float(horas_trabalhadas_str)
    salario_bruto = dinhero_por_hora_float * horas_trabalhadas_float
    desconto_inss = salario_bruto * 0.08
    desconto_sindicato =  salario_bruto * 0.05
    imposto_de_renda = salario_bruto * 0.11
    salario_liquido = salario_bruto - desconto_inss - desconto_sindicato - imposto_de_renda

    print(f'+ Salário Bruto: R${salario_bruto}')
    print(f'- IR (11%): R${imposto_de_renda}')
    print(f'- INSS (8%): R${desconto_inss}')
    print(f'- Sindicato: R${desconto_sindicato}')
    print(f'= Salário líquido: R${salario_liquido}')
except:
    print('Digite os valores em números.')
    