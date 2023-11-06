'''
Continuação algoritimos de ordenação

'''

def ordenacao_bolha(lista):
    for i in range(0, len(lista)):
        for j in range(1,len(lista)-i):
            if lista [j-1] > lista [j]:
                temp = lista[j-1]
                lista [j-1] = lista[j]
                lista[j] = temp

def ordenacao_insercao(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i -1
        while j > 0 and lista[j] > temp:
            lista[j+1] = lista[j]
        lista[j+1] = temp



#Programa Principal:
print(f'---Ordenação por bolha---')
numeros = [10,7,33,1,8]
print(f'Lista original: {numeros}')
ordenacao_bolha(numeros)
print(f'Lista ordenada: {numeros}')
print('\n---Ordenação Por insercao---')
numeros = [33,7,10,15,1]
print(f'Lista original: {numeros}')
ordenacao_insercao(numeros)
print(f'Lista ordenada: {numeros}')


