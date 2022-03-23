from random import randint

def gerarString(n):
    l = []
    s = ''
    for i in range(n):
        s+=str(randint(2,5))
    return s



def lcs_recursivo_memorizado(primeira_sequencia, segunda_sequencia, tamanho_primeira = None, tamanho_segunda = None, memoria = None):
    if tamanho_primeira == None or tamanho_segunda == None:
        tamanho_primeira = len(primeira_sequencia)
        tamanho_segunda = len(segunda_sequencia)
        memoria = [[-1]*(tamanho_segunda + 1) for i in range(tamanho_primeira + 1)]

    if (tamanho_primeira == 0 or tamanho_segunda == 0):
        return 0

    if (memoria[tamanho_primeira - 1][tamanho_segunda - 1] != -1):
        return memoria[tamanho_primeira - 1][tamanho_segunda - 1]

    if (primeira_sequencia[tamanho_primeira - 1] == segunda_sequencia[tamanho_segunda - 1]):

        memoria[tamanho_primeira - 1][tamanho_segunda - 1] = 1 + lcs_recursivo_memorizado(primeira_sequencia, segunda_sequencia, tamanho_primeira - 1, tamanho_segunda - 1, memoria)

        return memoria[tamanho_primeira - 1][tamanho_segunda - 1]

    else:

        memoria[tamanho_primeira - 1][tamanho_segunda - 1] = max(lcs_recursivo_memorizado(primeira_sequencia, segunda_sequencia, tamanho_primeira, tamanho_segunda - 1, memoria),
                                                                 lcs_recursivo_memorizado(primeira_sequencia, segunda_sequencia, tamanho_primeira - 1, tamanho_segunda, memoria))

        return memoria[tamanho_primeira - 1][tamanho_segunda - 1]


primeira = gerarString(100)
segunda = gerarString(100)
print(lcs_recursivo_memorizado(primeira,segunda))