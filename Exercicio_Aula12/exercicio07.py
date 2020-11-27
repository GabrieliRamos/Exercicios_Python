#######################################################################################################

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
#  conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 

######################################################################################################


contador = 0
lista_vogais = []
lista = []

frase = input('DIGITE UMA FRASE: ')

def vogais(frase):

    for vogais in frase:

        if vogais == 'a' or vogais == 'e' or vogais == 'i' or vogais == 'o' or vogais == 'u':
            
            lista_vogais.append(vogais)

            quantidade = len(lista_vogais)
        else:
            quantidade = 0

    print('\nQUANTIDADES DE VOGAIS: {}\n'.format(quantidade))

def espaços(frase, contador):
    for espacos in frase:
        
        if espacos == ' ': 
            lista.append(espacos)

            contador = len(lista)

    print('QUANTIDADES DE ESPAÇOS: {}'.format(contador))

if __name__ == "__main__":

    vogais(frase)
    espaços(frase, contador)

    
