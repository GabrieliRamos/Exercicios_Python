######################################################################################################

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
#     sempre arredonde os valores para cima, isto é, considere latas cheias.
#

######################################################################################################


tamanho_metros = int(input('QUAL É O TAMANHO DA PAREDE EM M²: '))

litro_nec = tamanho_metros/6
valor_galao = 25
litro_galao = 3.6
valor_lata = 80
litro_lata = 18

def lata(litro_lata, litro_nec, valor_lata):
 
    quant_lata = round(litro_nec/litro_lata)

    print('\nLATAS DE TINTA: {}'.format(quant_lata))
    print('TOTAL : {:.2f}\n'.format(quant_lata*valor_lata))

def galao(litro_nec, litro_galao, valor_galao):

    quant_galao = round(litro_nec/litro_galao)

    print('GALOES DE TINTA: {}'.format(quant_galao))
    print('TOTAL : {:.2f}\n'.format(quant_galao*valor_galao))

def lata_galao(litro_lata, litro_nec, valor_lata, litro_galao, valor_galao):

    quant_lata = round(litro_nec//litro_lata)
    resto = litro_nec%litro_lata
    quant_galao = round(resto/litro_galao)

    total = (quant_lata * valor_lata) + (quant_galao * valor_galao)

    print('OU {} LATA(S) E(OU) {} GALÃO(ÕES) NO VALOR DE: R$ {:.2f}'.format(quant_lata, quant_galao, total))


    

if __name__ == "__main__":

    lata(litro_lata, litro_nec, valor_lata)
    galao(litro_nec, litro_galao, valor_galao)
    lata_galao(litro_lata, litro_nec, valor_lata, litro_galao, valor_galao)


# Revisão
# não é necessário usar o round ali pois a divisão com \\ já retorna um valor inteiro
