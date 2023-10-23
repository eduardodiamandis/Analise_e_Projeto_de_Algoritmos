def maximo(lista):
 valor_maximo = lista[0]
 for i in range(1, len(lista)):
    if lista[i] > valor_maximo:
     valor_maximo = lista[i]
 return valor_maximo

# memso algoritimo utilizado Dividir e Conquistar

def maximo(lista, inicio, fim):
	if inicio == fim:
		return lista[inicio]
	else:
		meio = (inicio + fim) // 2
		m1 = maximo(lista, inicio, meio)
		m2 = maximo(lista, meio+1, fim)
		if m1 > m2:
			return m1
		else:
			return m2

# Programa principal
conjunto = [10, 20, 60, 1, 5, 55, 15, 9]
m = maximo(conjunto, 0, len(conjunto)-1)
print(f"Maior elemento: {m}")

#Dado dois valores b e n >= 0, escreva um algoritimo que calcule p = b^n

def potencia(b,n):
  valor = 1
  for i in range(n):
    valor *=b
  return valor 

def potencia(b, e):
	if e == 0:
		return 1
	elif e % 2 == 0: # testa se e é par
		valor = potencia(b, e//2)
		return valor*valor
	else: # se e é ímpar
		return b * potencia(b, e-1)

# Programa principal
base = 2
exp = 16
p = potencia(base, exp)
print(f"{base}^{exp} = {p}")
