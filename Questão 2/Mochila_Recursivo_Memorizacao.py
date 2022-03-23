from item import itemMochila
from random import randint

D = dict()

for i in range(0,900):
  D[i] = itemMochila(randint(1,6),randint(10,15))

n = len(D)
w = 100

memoria = [[-1 for i in range(w + 1)] 
               for j in range(n + 1)]

def mochila_recursiva_memorizacao(w = 0, D = dict(), n = 0):
  if (n == 0 or w == 0):
    return 0
  if (memoria[n][w]) != -1:
    return memoria[n][w]

  if (D[n-1].peso) <= w:
    memoria[n][w] = max(D[n-1].valor+mochila_recursiva_memorizacao(w - D[n-1].peso, D, n-1), mochila_recursiva_memorizacao(w, D, n-1))
    return memoria[n][w]


  elif(D[n-1].peso > w):
    memoria[n][w] = mochila_recursiva_memorizacao(w, D, n-1)
    return memoria[n][w]


print(mochila_recursiva_memorizacao(w, D, len(D)))