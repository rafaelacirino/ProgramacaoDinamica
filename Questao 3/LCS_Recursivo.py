from random import randint

def gerarString(n):
    l = []
    s = ''
    for i in range(n):
        s+=str(randint(2,5))
    return s


def lcs_recursivo(primeira_sequencia, segunda_sequencia, tamanho_primeira = None, tamanho_segunda = None):
  if tamanho_primeira == None or tamanho_segunda == None:
    tamanho_primeira = len(primeira_sequencia)
    tamanho_segunda = len(segunda_sequencia)

  if tamanho_primeira == 0 or tamanho_segunda == 0:
    return 0
  elif(primeira_sequencia[tamanho_primeira - 1] == segunda_sequencia[tamanho_segunda - 1]):
    return 1 + lcs_recursivo(primeira_sequencia, segunda_sequencia, tamanho_primeira - 1, tamanho_segunda - 1)
  else:
    return max(lcs_recursivo(primeira_sequencia, segunda_sequencia, tamanho_primeira, tamanho_segunda - 1),
               lcs_recursivo(primeira_sequencia, segunda_sequencia, tamanho_primeira - 1, tamanho_segunda))



primeira = gerarString(50)
segunda = gerarString(50)
print(lcs_recursivo(primeira,segunda))