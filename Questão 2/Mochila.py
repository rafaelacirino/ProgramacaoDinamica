from item import itemMochila
from random import randint

def inicioMatriz(m,n,W):
  for i in range(W+1):
    m.append(list())
    for j in range(n+1):
      if i == 0 or j == 0:
        m[i].append(0)
      else:
        m[i].append('_')

def mochila(S=dict(),n=0,W=0):
  m = list()
  inicioMatriz(m,n,W)
  for i in range(1,n+1):
    for w in range(1,W+1):
      if S[i].peso > w:
        m[w][i]= m[w][i-1]
      else:
        m[w][i] = max(m[w-S[i].peso][i-1]+S[i].valor,m[w][i-1])
  return m[W][n]

S = dict()

S[1] = itemMochila(6,30)
S[2] = itemMochila(3,14)
S[3] = itemMochila(4,16)
S[4] = itemMochila(2,9)
print(mochila(S,len(S),10))