from random import randint

def corte(p,n):
  r = {}
  r[0] = 0
  for j in range(1,n+1):
    q = -1
    for i in range(1,j+1):
      q = max(q,p[i]+r[j-i])
    r[j] = q
  return r[n]


p = dict()

tam = 994

for i in range(1, tam+1):
     p[i] = randint(5, 10)
print(corte(p,tam))

# A complexidade dessa questão é n^2 pois são realizadas duas iterações aninhadas:
