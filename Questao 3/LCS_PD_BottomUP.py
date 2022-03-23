from random import randint

def gerarString(n):
    l = []
    s = ''
    for i in range(n):
        s+=str(randint(2,5))
    return s

def lcs_bottom_up(primeira_sequencia, segunda_sequencia):
  tamanho_primeira = len(primeira_sequencia)
  tamanho_segunda = len(segunda_sequencia)

  memoria = [[-1]*(tamanho_segunda + 1) for i in range(tamanho_primeira + 1)]
  for i in range(tamanho_primeira + 1):
        for j in range(tamanho_segunda + 1):
            if primeira_sequencia[i - 1] == segunda_sequencia[j - 1]:
                memoria[i][j] = memoria[i-1][j-1]+1
            else:
                memoria[i][j] = max(memoria[i-1][j], memoria[i][j-1])
  return memoria[tamanho_primeira][tamanho_segunda]
primeira = gerarString(1000)
segunda = gerarString(1000)
print(lcs_bottom_up(primeira,segunda),primeira,segunda)