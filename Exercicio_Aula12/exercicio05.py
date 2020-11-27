#######################################################################################################

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados 
# em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) 
# e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 

######################################################################################################


from random import randint

lista = []

def gerador_numero ():
    for dados in range(100):

        lista.append(randint(1,6))

    for i in range(1,7):
        print(f'O NÚMERO {i} REPETIU {lista.count(i)}')

    print('\nVETOR DE NÚMEROS = {}'.format(lista))

if __name__ == "__main__":

    gerador_numero()
    
# Revisão Karla
# colocar um print informando que o algoritmo simula jogadas de um dado.
# tá ótimo