#Busca Binaria Recursiva chamandou outra funcao
def busca_bin(lista, alvo):
    return busca_bi_rec(lista,alvo,0,len(lista)-1)
    
def busca_bi_rec(lista,alvo,inicio,fim):
    meio = (inicio+fim)//2
    if inicio > fim:
        return False
    elif lista[meio] == alvo:
        return True 
    elif alvo < meio:
        return busca_bi_rec(lista, alvo,inicio,meio-1)
    else:
        return busca_bi_rec(lista,alvo,meio+1,fim)
    
'''
O algoritimo  de busca sequencia e pior que o de busca binaria

o algoritimo de busca binaria nao serve so para busca em listas
'''

