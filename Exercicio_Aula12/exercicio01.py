# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto - valor cheio
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido - valor com descontos
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$


def salario(ganha_hora, num_horas):

    salario_bruto = (ganha_hora * num_horas)* 31
    print(f'SALARIO BRUTO: R$ {salario_bruto}')

    imposto_renda = salario_bruto * 0.11
    salario_bruto -= imposto_renda
    print(f'IMPOSTO DE RENDA: R$ {imposto_renda}')

    inss = salario_bruto * 0.08
    salario_bruto -= inss
    print(f'INSS: R$ {inss}')

    sindicato = salario_bruto * 0.05
    salario_bruto -= sindicato
    print(f'SINDICATO: R$ {sindicato}')

    salario_liquido = salario_bruto
    print('SALARIO LIQUIDO: R$ %.2f'%salario_liquido)

if __name__ == "__main__":

    ganha_hora = float(input('QUANTO VOCÊ GANHA POR HORA: '))
    num_horas = int(input('HORAS TRABALHADAS NO MÊS: '))
    
    salario(ganha_hora, num_horas)
    
# Revisão Karla
# variáveis auto explicativas
# o salário bruto está sendo multiplicado por 31, suponho que tenha sido engano da programadora.
# fora isso está certinho