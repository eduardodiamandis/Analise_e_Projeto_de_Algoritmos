#Busca Binaria - eficiente 

n = int(input("Informe o valor de n: "))                #1 Vez
i = 0                           #1 Vez
while i < n:                    #n+1 Vez
    print(f'Passo {i}: ', n)    #n vezes
    i += 1                      #n vezes

#Total de passos: 1 + 1 + n+1 + n + n 
#f(n) = 3n+3

#Uma busca tem dois objetivos
#   - identificar se o elemento está em um conjuto
#   - localizar o elemento caso esteja no conjunto

#Vamos procurar 85 na lista L:
lista_L = [1,5,8,6,3,5,4,41,2,55,211,85]

def busca(lista_L,M=85):
    i = 0
    while i < len(lista_L):
       if lista_L[i] == M:
           return True
       i+=1
    return False
#Total: 1 + 1 n + 1 + n + n +1
 
# Vantagem da Busca sequencial : facíl ímplementação, serve para listas não ordenadas
# Desvantangens: não é muito eficiente: necessita que seja comparado TODOS OS ELEMENTOS da lista.


def busca_binaria(lista,alvo):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if lista[meio] == alvo:
            return True
        elif lista[meio] > alvo:
            fim = meio-1
        else:
            inicio = meio+1
    return False
