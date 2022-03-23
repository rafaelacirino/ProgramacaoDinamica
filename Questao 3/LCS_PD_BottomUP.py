from random import randint

def gerarString(n):
    l = []
    s = ''
    for i in range(n):
        s+=str(randint(2,5))
    return s

def lcs_bottom_up(primeira_seq, segunda_seq):

  tam_primeira = len(primeira_seq)
  tam_segunda = len(segunda_seq)

  memoria = [[-1]*(tam_segunda + 1) for i in range(tam_primeira + 1)]
  
  for i in range(tam_primeira + 1):
        for j in range(tam_segunda + 1):
            if primeira_seq[i - 1] == segunda_seq[j - 1]:
                memoria[i][j] = memoria[i-1][j-1]+1
            else:
                memoria[i][j] = max(memoria[i-1][j], memoria[i][j-1])

  return memoria[tam_primeira][tam_segunda]

primeira = gerarString(1000)
segunda = gerarString(1000)

print(lcs_bottom_up(primeira, segunda), primeira, segunda) 