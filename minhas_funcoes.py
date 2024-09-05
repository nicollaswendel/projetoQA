# minhas_funcoes.py
def remover_duplicatas(nums):
    seen = set()
    nova_lista = []
    for n in nums:
        if n not in seen:
            nova_lista.append(n)
            seen.add(n)
    return nova_lista

# minhas_funcoes.py
def calcular_fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# minhas_funcoes.py
def verificar_ordenacao(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))
