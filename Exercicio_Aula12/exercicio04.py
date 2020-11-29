#######################################################################################################

# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

#######################################################################################################

lista_primos = []

numero = int(input('NUMERO: '))

def numeros_primos(numero):
    for i in range(numero + 1):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        if divisor == 2:
            lista_primos.append(i)

    print(f'LISTA NÚMEROS PRIMOS: {lista_primos}')


if __name__ == "__main__":
    
 numeros_primos(numero)