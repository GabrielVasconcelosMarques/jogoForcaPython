from typing import Counter
from operator import itemgetter

#Lista que armazena palavra escolhida
palavra = ['fogao']

#Lista que irá ter as letras separadas uma por uma da palavra acima
lista = []
for c in palavra[0]:
    lista.append(c)

#Lista tracejada a ser exibida
listaTraco = []
for c in lista:
    listaTraco.append('_ ')


# Criando dicionario para armazenar as tuplas de repetição
dic = Counter(lista)

#ordenando dicionario para o maior valor ser exibido primeiro
variavel = sorted(dic.items(), key=itemgetter(1), reverse=True)

#calculando numero maximo que uma letra é repetida
numeroRepeticoes = variavel[0][1]

erro = 0

print("================================================")
print("========== Bem-Vindo ao Jogo da Forca ==========")
print("================================================\n")

print("Sua palavra é: ")
print(*listaTraco)
print()

# loop até errar 3x ou acertar a palavra
while True:
    letra = input("Digite uma letra: ")
    if letra not in lista:
        print('\nVocê errou, tente de novo \n')
        erro +=1
        print(*listaTraco)
        print('\n')
    else:
        #iterando a quantidade de vezes em que houve mais letras repetidas
        for c in range(numeroRepeticoes):
            if letra in lista:
                
                listaTraco[lista.index(letra)] = letra
                lista[lista.index(letra)] = ''
                print('\nparabens, acertou \n')
                print(*listaTraco)
                print('\n')
    if erro == 3:
        print("Tentativa de acertos excedido, o jogo acabou")
        break
    if '_ ' not in listaTraco:
        print("Você venceu")
        break

            

    





    




