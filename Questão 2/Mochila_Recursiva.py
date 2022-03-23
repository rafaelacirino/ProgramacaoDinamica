from item import itemMochila
from random import randint

D = dict()

for i in range(0, 90):
  D[i] = itemMochila(randint(1,6),randint(10,15))
  
w = 100
n = len(D)

def mochila_recursivo(w, D, n):

  if (n== 0 or w ==0):
    return 0

  if (D[n-1].peso) <= w:
    return max(D[n-1].valor + mochila_recursivo(w - D[n - 1].peso, D, n - 1), mochila_recursivo(w, D, n - 1))

  else:
    return mochila_recursivo(w, D, n - 1)




print(mochila_recursivo(w, D, n))