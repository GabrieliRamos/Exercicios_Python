####################################################################################################### 

# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

######################################################################################################


def triângulo ():
    a = int(input('LADO A: '))
    b = int(input('LADO B: '))
    c = int(input('LADO C: '))
    if(a + b > c) and (a + c > b) and (b + c > a):
        print('É UM TRIÂNGULO!')
        if(a == b == c):
            print('É UM TRIÂNGULO EQUILÁTERO!')
        elif(a == b) or (a == c) or (b == c):
            print('É UM TRIÂNGULO ISÓSCELES!')
        elif(a != b) and (a != c) and (b != c):
            print('É UM TRIÂNGULO ESCALENO')
    else:
        print('NÃO É UM TRIÂNGULO')

if __name__ == "__main__":

    triângulo()
    
    while True:

        opcao = input('\nDESEJA CONTINUAR s/n: ')

        if opcao == 's':
            triângulo()
        
        else:
            print('Obrigado. Volte sempre!')
            break


# Revisão Karla
# gostei do menuzinho.
# bom código